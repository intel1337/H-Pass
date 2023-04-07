@echo off

set version=3.x.y

set download_url=https://www.python.org/ftp/python/latest/Python-%version%.tar.xz

bitsadmin /transfer python_downloader %download_url% %CD%\Python-latest.tar.xz

echo Python Sucessfully Installed.

pip install -r requirements.txt
