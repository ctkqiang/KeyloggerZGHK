@echo off
REM ################################################

REM Check if pip is installed
where pip >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo pip is not installed. Please install pip to continue.
    pause
    exit /b 1
)

REM Install pyinstaller with verbose output
echo Installing pyinstaller...
pip3 install pyinstaller -v
if %ERRORLEVEL% neq 0 (
    echo Failed to install pyinstaller. Exiting.
    pause
    exit /b 1
)

REM Prompt the user for the name of the Keylogger
set /p name="Enter the name you want to give your Keylogger: "

REM Validate user input
if "%name%"=="" (
    echo No name provided. Exiting.
    pause
    exit /b 1
)

REM Run PyInstaller with the specified name
echo Creating executable with PyInstaller...
pyinstaller --onefile --name "%name%" --noconsole run.py
if %ERRORLEVEL% neq 0 (
    echo Failed to create executable. Please check the PyInstaller output for errors.
    pause
    exit /b 1
)

echo Executable created successfully.

REM Pause to keep the window open (optional)
pause
