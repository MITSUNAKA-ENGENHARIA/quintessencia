from sqlalchemy.orm import Session
from app.models.message import Message
from app.models.role import Role
from datetime import datetime

class MessageRepository:
     def __init__(self, db: Session):
          self.db = db
     
     def create(self,
                client_name: str,
                phone_number: str,
                role: Role,
                message_content: str,
                context: str,
                created_at: datetime):
          db_message = Message(client_name=client_name,
                               phone_number=phone_number,
                               role=role,
                               message_content=message_content,
                               context=context,
                               created_at=created_at)
          self.db.add(db_message)
          self.db.commit()
          self.db.refresh(db_message)
          return db_message