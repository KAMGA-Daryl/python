import time
from time import timezone

from sinchsms import SinchSMS


def sendTexto():

    phone_number = '+237698322083'
    app_key = '1c915cdb7b074014a583d8364d649725'
    app_secret = 'clé_privee'

    message = 'hello Buddy !'

    client = SinchSMS(app_key, app_secret)

    response = client.send_message(phone_number, message)

    message_id = response['message_id']
    response = client.check_status(message_id)

    while response['status'] != 'successfull':
        print(response['status'])
        time.sleep(1)
        response = client.check_status(message_id)

        print(response['status'])

if __name__ == "__main__ ":
  
    sendTexto()
