from app.models.message import Message
from app.models.role import Role
from app.models.context import Context

class MessageRepository:
    def __init__(self, db_session):
        self.db = db_session
        
    def save_message(
        self,
        client_name: str,
        phone_number: str,
        message_content: str,
        role: Role,
        context: Context
    ):
        message = Message(
            client_name = client_name,
            phone_number = phone_number,
            message_content = message_content,
            role = role,
            context = context
        )
        
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)

        return message
    
    def get_current_context(self, phone_number: str):
        message = (
            self.db.query(Message)
            .filter(Message.phone_number == phone_number)
            .order_by(Message.created_at.desc())
            .first()
        )
        
        return message.context if message else None
    
    def update_context(self, phone_number: str, new_context: Context):
        last_message = (
            self.db.query(Message)
            .filter(Message.phone_number == phone_number)
            .order_by(Message.created_at.desc())
            .first()
        )
        
        if last_message:
            last_message.context = new_context
            self.db.commit()
            self.db.refresh(last_message)
            
        return last_message
    
    def get_n_messages(self, phone_number: str, limit: int = 10):
        n_messages = (
            self.db.query(Message)
            .filter(Message.phone_number == phone_number)
            .order_by(Message.created_at.asc())
            .limit(limit)
            .all()
        )
        
        return n_messages
    
    def phone_exists(self, phone_number: str):
        return(
            self.db.query(Message.id)
            .filter(Message.phone_number == phone_number)
            .first() is not None
        )
    
    