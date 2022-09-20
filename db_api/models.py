from sqlalchemy import Integer, String, Float, DateTime
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql import func
from database import Base
from dataclasses import dataclass
    
@dataclass
class message(Base):
    __tablename__ = 'message'
    id: int
    username: str
    content: str
    likes: int
    time_posted: DateTime
    
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    content = Column(String(140), nullable=False)
    likes = Column(Integer, default=int(0),nullable=False)
    time_posted = Column(DateTime, nullable=False, server_default=func.now())