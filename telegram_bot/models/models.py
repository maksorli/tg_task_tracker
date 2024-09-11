from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TelegramUser(Base):
    __tablename__ = 'tasks_telegramuser'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String(100), nullable=True)   

    def __repr__(self):
        return f"<TelegramUser(id={self.id}, telegram_id={self.telegram_id})>"
