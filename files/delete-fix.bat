@echo off
set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )
SET mypath=%~dp0
cd C:\Windows\System32\
takeown /f "WpcToknot.exe"
takeown /f "WpcMonnot.exe"
icacls "WpcToknot.exe" /grant %username%:M
icacls "WpcMonnot.exe" /grant %username%:M
del WpcToknot.exe
del WpcMonnot.exe