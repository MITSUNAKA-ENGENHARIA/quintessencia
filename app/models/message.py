from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.database.connection import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_name = Column(String(50), nullable=False)
    phone_number = Column(String(15), nullable=False)
    role = Column(String(10), nullable=False) #bot/user
    message_content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


