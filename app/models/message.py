from sqlalchemy import Column, Integer, String, Text, DateTime, Enum
from datetime import datetime

from app.database.connection import Base
from app.models.role import Role
from app.models.context import Context


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_name = Column(String(50), nullable=False)
    phone_number = Column(String(15), nullable=False, index=True)
    role = Column(Enum(Role), nullable=False)
    message_content = Column(Text, nullable=False)
    context = Column(Enum(Context), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


