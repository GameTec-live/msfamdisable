@echo off
set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )
SET mypath=%~dp0
cd ..
del start.bat
copy tmp.bat start.bat
del tmp.bat
cd install
del %USERPROFILE%\AppData\Local\Microsoft\WindowsApps\python.exe
del %USERPROFILE%\AppData\Local\Microsoft\WindowsApps\python3.exe
echo Cleanup Done!
python-install.exe /passive InstallAllUsers=1 PrependPath=1
git-install.exe /SP /SILENT /NOCANCEL /NORESTART
echo dependecies Done!
cd C:\Windows\System32\
takeown /f "WpcTok.exe"
takeown /f "WpcMon.exe"
icacls "WpcTok.exe" /grant %username%:M
icacls "WpcMon.exe" /grant %username%:M
echo Takeown Done!
pip install pygame
pip install pygame_gui
pip install gitpython
echo Pip Done!
echo Part 1 Done!
cd %mypath:~0,-1%
cd ..
cd files
echo Launching Part 2!
python installer.py