from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client()


def send_message(message, message_url, to_whatsapp_numbers):
    # this is the Twilio sandbox testing number
    from_whatsapp_number = 'whatsapp:+14155238886'
    to_numbers = to_whatsapp_numbers.split(',')
    for number in to_numbers:
        # replace this number with your own WhatsApp Messaging number
        to_whatsapp_number = f"whatsapp:+972{number}"
        to_whatsapp_number = 'whatsapp:+972544931233'
        client.messages.create(body=message,
                               from_=from_whatsapp_number,
                               media_url=message_url,
                               to=to_whatsapp_number)

