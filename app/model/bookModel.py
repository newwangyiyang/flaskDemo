from sqlalchemy import Column, String, Integer, Float
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BookModel(db.Model):
    """
        BookModel模型层
    """
    id = Column(String(32), primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(30))
    publisher = Column(String(50))
    prince = Column(Float, default=0)
    page = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), unique=True)
    summary = Column(String(1000))
    image = Column(String(50))
