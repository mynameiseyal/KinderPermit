from sel import Selenium
from cloudinary_management import Cloudinary
from whatsapp import send_message
import os

sel = Selenium()
cloud = Cloudinary()

username = os.getenv("username")
password = os.getenv("password")
to_whatsapp_numbers = os.getenv("to_whatsapp_numbers")


if __name__ == '__main__':
    sel.launch_chrome()
    sel.go_to_decleration_page()
    # sel.login(username=username, password=password)
    sel.login(username='5184588', password='Eyal1982')
    # sel.sign_health_decleration()
    screenshot = sel.save_screenshot()
    message_url = cloud.upload_files(file=screenshot)
    # send_message(message=screenshot, message_url=message_url, to_whatsapp_numbers=to_whatsapp_numbers)
    send_message(message=screenshot, message_url=message_url, to_whatsapp_numbers='544931233,542087080')
    sel.quit()