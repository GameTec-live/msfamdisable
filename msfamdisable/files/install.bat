@echo off
color 2

:: BatchGotAdmin
::-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"="
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
::--------------------------------------

::ENTER YOUR CODE BELOW:


echo Welcome in the Intall Wizard of msfamdisable. By Gematec_live

reg query "hkcu\software\Python"  
if ERRORLEVEL 1 GOTO NOPYTHON  
goto :HASPYTHON  
:NOPYTHON

echo please install python 3 from the microsoft store!
python
pause



:HASPYTHON  
echo python already installed. skipping installer.


git --version
if ERRORLEVEL 1 GOTO NOGIT
goto :GIT


:NOGIT
echo please install git.

start "" https://git-scm.com/download/win



:GIT
echo Git already installed. skipping installer.


pip install pygame
pip install pygame_gui
pip install gitpython
echo Editing permissions
icacls "C:\Windows\System32\WpcTok.exe" /grant %username%:M
icacls "C:\Windows\System32\WpcMon.exe" /grant %username%:M
echo Part 1 Done!!
echo Launching Part 2!
python installer.py