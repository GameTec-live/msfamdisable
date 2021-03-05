@echo
echo checking for Updates
Ping www.google.nl -n 1 -w 1000
cls
if errorlevel 1 (

echo Not connected to the Internet! Launching Normally!
start.bat

) 
else (

echo connected! Updating! Please wait!
updater.bat
)


