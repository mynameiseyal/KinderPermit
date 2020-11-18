from email_client import EmailClient
from sel import Selenium
from cloudinary_management import Cloudinary
from whatsapp import send_message
import os
from pathlib import Path

parent_username = os.getenv("parent_username")
parent_password = os.getenv("parent_password")
email_username = os.getenv("email_username")
email_password = os.getenv("email_password")
to_whatsapp_numbers = os.getenv("to_whatsapp_numbers")
to_email = os.getenv("to_email")

sel = Selenium()
cloud = Cloudinary()
mail = EmailClient(username=email_username, password=email_password,
                   recipients=to_email)


if __name__ == '__main__':
    sel.launch_chrome()
    sel.go_to_decleration_page()
    sel.login(username=parent_username, password=parent_password)
    # sel.sign_health_decleration()
    screenshot = sel.save_screenshot()
    file = Path(__file__).parent / screenshot
    mail.send_mail_with_file(filename=file)
    message_url = cloud.upload_files(file=screenshot)
    send_message(message=screenshot, message_url=message_url, to_whatsapp_numbers=to_whatsapp_numbers)
    sel.quit()