import pywhatkit as kit
import datetime

def send_whatsapp_message(to_number, message):
    try:
        # Format the phone number as '+<country_code><phone_number>'
        to_number = f'+{to_number}'

        # Send the WhatsApp message
        kit.sendwhatmsg(to_number, message,datetime.datetime.now().hour,datetime.datetime.now().minute+1)  # Sends the message immediately
        return True, None  # Success
    except Exception as e:
        error_message = str(e)
        return False, error_message