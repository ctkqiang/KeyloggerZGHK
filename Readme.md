# 键盘记录器说明文档

## 概述

这个仓库包含一个基础键盘记录器的 Python 脚本。键盘记录器是一种监控和记录用户在计算机上按键的监视软件。该脚本专门捕获键盘输入并通过 webhook URL 将记录的数据发送到远程服务器。

---

## 法律风险与免责声明（务必阅读）

```

【深求科技教育用途软件使用免责声明与法律风险声明】

一、法律依据：

本软件适用下列中华人民共和国法律法规及司法解释，用户必须全面遵守：

1. 《中华人民共和国网络安全法》（2017 年 6 月 1 日实施）
2. 《中华人民共和国刑法》（2015 年修订，2020 年修订版）
3. 《个人信息保护法》（2021 年 11 月 1 日起施行）
4. 《计算机信息网络国际联网安全保护管理办法》（工信部令第 36 号，2000 年）
5. 《网络安全等级保护条例》（2019 年 9 月 1 日起施行）
6. 最高人民法院《审理危害计算机信息系统安全刑事案件具体应用法律若干问题的解释》（法释〔2011〕7 号）

二、用户责任与行为规范：

1. 用户仅限将本软件用于合法的教育研究、技术学习及环境测试，严禁用于任何非法入侵、破坏、数据窃取、恶意攻击等违法犯罪行为。
2. 违反《刑法》第二百八十五条——非法侵入计算机信息系统的，处三年以下有期徒刑或者拘役，并处或者单处罚金；情节严重的，处三年以上七年以下有期徒刑。
3. 违反《刑法》第二百八十六条——制作、传播计算机病毒等破坏性程序，处三年以下有期徒刑、拘役或者罚金；情节严重的，处三年以上七年以下有期徒刑。
4. 违反《刑法》第二百八十七条——非法获取、出售或者提供个人信息，情节严重者可判处五年以下有期徒刑或拘役，并处罚金；情节特别严重的，处五年以上有期徒刑。
5. 违反《个人信息保护法》第六十七条，未采取必要措施导致个人信息泄露，视情节严重，最高可处以 500 万元人民币罚款。
6. 违反《网络安全法》第四十一条规定，擅自提供网络产品、服务存在安全隐患，责任单位依法承担法律责任。

三、免责声明：

1. 本软件仅供合法教育、技术研究及测试使用，开发者不承担任何因用户使用本软件导致的直接或间接损失，包括但不限于数据丢失、系统损坏、经济损失及法律责任。
2. 用户使用本软件即视为已充分理解本声明及法律风险，自愿承担所有责任。
3. 使用本软件请确保已获得目标系统的合法授权，严禁对无授权系统进行任何形式的攻击或测试。

四、风险提示：

1. 网络安全系全社会共同责任，任何非法攻击行为不仅违背法律，更破坏互联网生态环境。
2. 任何违法行为一经发现，将依法追究刑事责任，警方和司法机关可通过技术手段追踪定位违法者。
3. 任何软件滥用后果自负，开发者保留追究相关侵权责任的权利。

五、争议解决：

因使用本软件发生的任何争议，均适用中华人民共和国法律，由软件开发者所在地人民法院管辖。

六、特别声明：

请用户务必慎重下载及使用网络软件，避免因轻率行为导致不可挽回的法律后果。

网络安全不是儿戏，技术学习需守规矩，愿你我共同维护绿色互联网环境。

```


## 功能特点

- **按键捕获**：监听并记录用户按下的每个按键。
- **异步数据传输**：异步发送记录的按键数据到指定服务器。
- **系统信息**：在日志中包含机器名称、IP 地址和时间戳。

## 依赖项

该脚本依赖于几个 Python 库。如果缺少任何这些库，将引发`ImportError`：

- `base64`：用于 base64 格式的数据编码和解码。
- `json`：用于 Python 对象和 JSON 格式之间的转换。
- `asyncio`：用于异步编程和非阻塞操作。
- `socket`：用于网络相关操作，如获取 IP 地址。
- `requests`：用于向远程服务器发送 HTTP 请求。
- `logging`：用于记录信息和错误。
- `datetime`：用于事件时间戳。
- `pynput`：用于捕获键盘输入。

请确保在您的 Python 环境中安装这些依赖项。

## 设置

1. **安装依赖项**

   使用 pip 安装所需库：

   ```bash
   pip install base64 json asyncio socket requests logging pynput
   ```

2. **配置 Webhook URL**

   脚本使用 base64 编码的 webhook URL 发送按键记录。将 base64 编码的 URL 替换为您自己的 webhook 端点。根据需要解码和重新编码 URL 以保持混淆。

3. **更新 Webhook URL**

   在脚本中，找到`__init__`方法中的`self.url`赋值，并用您解码的 webhook URL 更新它：

   ```python
   self.url = base64.b64decode("您的BASE64编码URL").decode("utf-8")
   ```

## 使用方法

1. **运行脚本**

   执行脚本开始记录按键：

   ```bash
   python keylogger.py
   ```

2. **日志记录**

   脚本将开始捕获按键并记录它们。当按键数量超过 20 个时，它会将记录的按键批量发送到远程服务器。

3. **查看日志**

   日志会发送到指定的 webhook URL。检查在此 URL 配置的服务器以查看捕获的按键和其他信息。

# 如何构建 exe？

```bash
pyinstaller --onefile --name {插入名称} --noconsole run.py
```

成功执行后：
![IMG_20240907_204035](https://github.com/user-attachments/assets/7418c025-f408-4e46-bd1f-9b901f66bd96)

## 安全注意事项

- 确保 webhook URL 保密和安全。
- 在部署键盘记录器之前获得用户同意。
- 了解并遵守有关使用键盘记录软件的法律法规。

## 许可证

本项目采用 **木兰宽松许可证 (Mulan PSL)** 进行许可。  
有关详细信息，请参阅 [LICENSE](LICENSE) 文件。  
（魔法契约要保管好哟~）

[![License: Mulan PSL v2](https://img.shields.io/badge/License-Mulan%20PSL%202-blue.svg)](http://license.coscl.org.cn/MulanPSL2)

## 🌟 开源项目赞助计划

### 用捐赠助力发展

感谢您使用本项目！您的支持是开源持续发展的核心动力。  
每一份捐赠都将直接用于：  
✅ 服务器与基础设施维护（魔法城堡的维修费哟~）  
✅ 新功能开发与版本迭代（魔法技能树要升级哒~）  
✅ 文档优化与社区建设（魔法图书馆要扩建呀~）

点滴支持皆能汇聚成海，让我们共同打造更强大的开源工具！  
（小仙子们在向你比心哟~）

---

### 🌐 全球捐赠通道

#### 国内用户

<div align="center" style="margin: 40px 0">

<div align="center">
<table>
<tr>
<td align="center" width="300">
<img src="https://github.com/ctkqiang/ctkqiang/blob/main/assets/IMG_9863.jpg?raw=true" width="200" />
<br />
<strong>🔵 支付宝</strong>（小企鹅在收金币哟~）
</td>
<td align="center" width="300">
<img src="https://github.com/ctkqiang/ctkqiang/blob/main/assets/IMG_9859.JPG?raw=true" width="200" />
<br />
<strong>🟢 微信支付</strong>（小绿龙在收金币哟~）
</td>
</tr>
</table>
</div>
</div>

#### 国际用户

<div align="center" style="margin: 40px 0">
  <a href="https://qr.alipay.com/fkx19369scgxdrkv8mxso92" target="_blank">
    <img src="https://img.shields.io/badge/Alipay-全球支付-00A1E9?style=flat-square&logo=alipay&logoColor=white&labelColor=008CD7">
  </a>
  
  <a href="https://ko-fi.com/F1F5VCZJU" target="_blank">
    <img src="https://img.shields.io/badge/Ko--fi-买杯咖啡-FF5E5B?style=flat-square&logo=ko-fi&logoColor=white">
  </a>
  
  <a href="https://www.paypal.com/paypalme/ctkqiang" target="_blank">
    <img src="https://img.shields.io/badge/PayPal-安全支付-00457C?style=flat-square&logo=paypal&logoColor=white">
  </a>
  
  <a href="https://donate.stripe.com/00gg2nefu6TK1LqeUY" target="_blank">
    <img src="https://img.shields.io/badge/Stripe-企业级支付-626CD9?style=flat-square&logo=stripe&logoColor=white">
  </a>
</div>

---

### 📌 开发者社交图谱

#### 技术交流

<div align="center" style="margin: 20px 0">
  <a href="https://github.com/ctkqiang" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-开源仓库-181717?style=for-the-badge&logo=github">
  </a>
  
  <a href="https://stackoverflow.com/users/10758321/%e9%92%9f%e6%99%ba%e5%bc%ba" target="_blank">
    <img src="https://img.shields.io/badge/Stack_Overflow-技术问答-F58025?style=for-the-badge&logo=stackoverflow">
  </a>
  
  <a href="https://www.linkedin.com/in/ctkqiang/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-职业网络-0A66C2?style=for-the-badge&logo=linkedin">
  </a>
</div>

#### 社交互动

<div align="center" style="margin: 20px 0">
  <a href="https://www.instagram.com/ctkqiang" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-生活瞬间-E4405F?style=for-the-badge&logo=instagram">
  </a>
  
  <a href="https://twitch.tv/ctkqiang" target="_blank">
    <img src="https://img.shields.io/badge/Twitch-技术直播-9146FF?style=for-the-badge&logo=twitch">
  </a>
  
  <a href="https://github.com/ctkqiang/ctkqiang/blob/main/assets/IMG_9245.JPG?raw=true" target="_blank">
    <img src="https://img.shields.io/badge/微信公众号-钟智强-07C160?style=for-the-badge&logo=wechat">
  </a>
</div>

---

致极客与未来的你

> "世界由代码驱动，安全靠你我守护。"

无论你是网络安全研究员、CTF 挑战者、自由极客，还是热爱数学与工程的探索者，这个项目都向你敞开怀抱。
欢迎你 fork、魔改、重构、注入灵感，它是工具，也是信仰。

但请铭记心底：

> **技术本无善恶，使用才有底线。**
> 愿你在这个开源项目中，找到属于自己的价值与乐趣。

> 享受黑客精神，享受学习之旅！—— 你最贴心的代码姐姐 💖
