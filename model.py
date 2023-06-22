from database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    # テーブル名
    __tablename__ = 'users'
    
    # カラム情報
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age