import git
import os
import shutil


os.mkdir('Update')
git.Git("Update").clone("https://github.com/GameTec-live/Python-Family-Disabeler-Update.git")
shutil.copyfile("Update/Python-Family-Disabeler-Update/asci.py","asci.py")
shutil.copyfile("Update/Python-Family-Disabeler-Update/installer.py","installer.py")
shutil.copyfile("Update/Python-Family-Disabler-Update/commandlib.py","commandlib.py")
shutil.copyfile("Update/Python-Family-Disabler-Update/libary.py","libary.py")