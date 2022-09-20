window.onload = () => {
    fill_page()
}


function refresh(event) {
    $('.messages_wrapper').html('')
    fill_page()
}



function post_message(button) {
    
    const form_element = button.parentElement.parentElement
    const username = form_element['username'].value
    const content = form_element['message_content'].value
    
    if (username && content) {
        $.post('http://db_api:5000/add_message', {username:username, message_content:content}, function(response){ 
            $('#username-input').val('')
            $('#message_input').val('')
            alert("Messaggio inviato con successo!");
            const message = {
                username:username,
                content: content,
                likes: 0,
                time_posted: ""
            }
            const div_message = create_element(message)
            $('.messages_wrapper').prepend(div_message)
            // console.log(response)
        });
    }
}

function message_liked(button) {
    const likes = $($(button).parent().children()[0])
    likes.text(parseInt(likes.text()) + 1)
    button.disabled = true
    if (button.value) {
        $.post('http://db_api:5000/add_like', {id:button.value}, function (response) {
            console.log(response)
        })
    }
}

function create_element(message) {
    const div_message = $('<div/>', {class:'message'})

    const user = $('<div/>', {class:'user'})
                .append($('<div/>', {class:'circle'}).attr('style', `background-color:${color(message['username'])}`))
                .append($('<div/>', {class:'username', text:message['username']}))

    const content = $('<div/>', {class:'content', text:message['content']})

    const likes = $('<div/>', {class:'likes'})
                .append($('<p/>', {class:'n_likes', text:message['likes']}))
                .append($('<button/>', {class:'likes_text', text:'likes', type:'button', value:message['id'], onclick:'message_liked(this)'}))
    
    div_message.append([user, content, likes])
    
    return div_message

    }

function fill_page() {

    $.get('http://db_api:5000/messages', {} ,function(data) {
        if (data) {
            for (const message of data) {
                //console.log(message)
                $('.messages_wrapper').prepend(create_element(message))
            }
        }
    })
    
}

const cyrb53 = function(string, seed = 0) {
    let h1 = 0xdeadbeef ^ seed, h2 = 0x41c6ce57 ^ seed;
    for (let i = 0, ch; i < string.length; i++) {
        ch = string.charCodeAt(i);
        h1 = Math.imul(h1 ^ ch, 2654435761);
        h2 = Math.imul(h2 ^ ch, 1597334677);
    }
    h1 = Math.imul(h1 ^ (h1>>>16), 2246822507) ^ Math.imul(h2 ^ (h2>>>13), 3266489909);
    h2 = Math.imul(h2 ^ (h2>>>16), 2246822507) ^ Math.imul(h1 ^ (h1>>>13), 3266489909);
    return 4294967296 * (2097151 & h2) + (h1>>>0);
};

function color(string) {
    return '#' + cyrb53(string).toString().slice(0,6)
}