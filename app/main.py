from neonize.client import NewClient
from neonize.events import MessageEv, ConnectedEv, event

client = NewClient("quintessencia")

@client.event(ConnectedEv)
def on_connected(client: NewClient, event: ConnectedEv):
    print("✅ Bot connected successfully!")
    print(f"📱 Logged in as: {event.device.User}")

@client.event(MessageEv)
def on_message(client: NewClient, event: MessageEv):
    
    text = event.Message.conversation or event.Message.extendedTextMessage.text
    sender = event.Info.MessageSource.Sender
    name = event.Info.Pushname

    if text == "ping":
        client.send_message(sender, "pong porra")
        client.send_message(sender, sender.User)
        client.send_message(sender, name)
        print(f"sender completo: {sender}")
        print(f"sender.User: {sender.User}")
        print(f"sender raw: {repr(sender)}")
    elif text == "hello":
        client.reply_message("Hello! 👋 How can I help you?", event)

def main():
    client.connect()
    event.wait()


if __name__ == "__main__":
    main()
