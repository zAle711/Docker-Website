from flask import Flask, jsonify, request, render_template, make_response
from models import message
from database import get_session
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*')

@app.route('/messages', methods=['GET'])
def get_all_message():
    with get_session() as db:
        all_message = db.query(message).all()
        return jsonify(all_message)

@app.route('/add_message', methods=['POST'])
def add_message():
    #getting post data
    username = request.form.get('username')
    content = request.form.get('message_content')
    print(f"username: {username} - content: {content}")
    #ADD new message to the db
    if username and content:
        with get_session() as db:
            new_message = message(username=username, content=content)
            db.add(new_message)
            db.commit()

            print(f"Un nuovo messaggio è stato correttamente inserito nel db! -> id:{new_message.id} + name:{new_message.username} + text:{new_message.content}")
            
            resp = make_response(jsonify(new_message))
            #resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp

@app.route('/add_like', methods=['POST'])
def add_like():
    
    id = request.form.get('id')
    with get_session() as db:
        db.query(message
            ).filter(message.id == id
            ).update( {
                message.likes: message.likes + 1
            })
        
        return jsonify( db.query(message).filter(message.id == id).all() )
    

@app.route('/edit_message', methods=['POST'])
def edit_message():
    
    id =  request.form.get('id')
    content = request.form.get('content')
    with get_session() as db:
        res = db.query(message
                ).filter(message.id == id
                ).update({
                    message.content: content
                })
        
        print(f"Message with id: {id} has been successfully modified!")
        
        return jsonify( db.query(message).filter(message.id == id).all() )
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
