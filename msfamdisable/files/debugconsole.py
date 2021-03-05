import os
import subprocess
import libary
import time
import commandlib

command = 'none'

print("Starting CLI..")
libary.login()
commandlib.screenfetchsimple()

while True:
    command = input("crash@msfamdisable: ")
    commandlib.checkcommand(command)
    