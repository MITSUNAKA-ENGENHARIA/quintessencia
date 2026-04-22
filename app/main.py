from neonize.client import NewClient
from neonize.events import MessageEv, ConnectedEv

import time
import threading
import sys

client = NewClient("quintessencia")

@client.event(ConnectedEv)
def on_connected(client: NewClient, event: ConnectedEv):
    print("bot connected successfully!")

@client.event(MessageEv)
def on_message(client: NewClient, event: MessageEv):
    
    text = event.Message.conversation or event.Message.extendedTextMessage.text
    sender = event.Info.MessageSource.Sender
    name = event.Info.Pushname

    if text == "ping":
        client.send_message(sender, "pong porra")
        client.send_message(sender, sender.User)
        client.send_message(sender, name)
        print(f"sender ({sender.User}): {text}")
    elif text == "hello":
        client.reply_message("Hello! 👋 How can I help you?", event)

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
