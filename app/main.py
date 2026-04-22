from neonize.client import NewClient
from neonize.events import MessageEv, ConnectedEv
from app.repository.message_repository import MessageRepository
from app.database.connection import SessionLocal
from app.models.role import Role
from app.models.context import Context, CONTEXTS
from app.shared.script import handle_contexts

import time
import threading
import sys

client = NewClient("quintessencia")
db = SessionLocal()
msg_repository = MessageRepository(db)

@client.event(ConnectedEv)
def on_connected(client: NewClient, event: ConnectedEv):
    print("bot connected successfully!")

@client.event(MessageEv)
def on_message(client: NewClient, event: MessageEv):
    
    text = event.Message.conversation or event.Message.extendedTextMessage.text
    sender = event.Info.MessageSource.Sender
    name = event.Info.Pushname


    if msg_repository.phone_exists(sender.User):
        idx = CONTEXTS.index(msg_repository.get_current_context(sender.User))
        msg_repository.update_context(sender.User, CONTEXTS[(idx+1)%len(CONTEXTS)])
    else:
        msg_repository.save_message(name, sender.User, text, Role.USER, Context.WAITING_MESSAGE_1)

    if text == "ping":
        client.send_message(sender, "pong")

    reply = handle_contexts(msg_repository.get_current_context(sender.User))
    client.send_message(sender, reply)
    
    print(f"\nsender ({sender.User} | {name}): {text}")
    print(f"bot: {reply}\n")

def main():
    t = threading.Thread(target=client.connect, daemon=True)
    t.start()
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("shutting bot down...")
        sys.exit(0)

if __name__ == "__main__":
    main()
