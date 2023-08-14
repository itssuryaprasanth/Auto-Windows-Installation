@setlocal enableextensions
@cd /d "%~dp0"
@echo off

Title Installing Windows
set PYTHONPATH= %PYTHONPATH%;%cd%

echo *************************************************************

pip install paramiko
pip install translate

echo Checking VPN Connection
python utilities/network_connection_check.py
if %ERRORLEVEL% == 1 (
	call:Stop 
) else (
	call:Installation %1
)
: Stop
echo "Please connect to bdcpgnet.connect.dell.com/red cable in global protect and retry"
echo.&pause&goto:eof

: Installation
echo "Removing existing OS_HAND_INSTALL_AUTOMATION directory if exists"

rmdir /s /q "C:\Users\%USERNAME%\Downloads\OS_HAND_INSTALL_AUTOMATION"

echo **************************************************************
call utilities/ssh_server_installation.bat
echo **************************************************************
python utilities/local_connection_to_server.py %~1
echo ****************************************************************
diskpart /s disk_part/get_attached_usb_device_id.txt > C:/Windows/Temp/usb_device.txt
echo ****************************************************************
python formatters/get_usb_device_id.py %~1
echo ****************************************************************
diskpart /s disk_part/clean_usb_device.txt
echo ****************************************************************
echo ****************************************************************
Powershell.exe -ExecutionPolicy Bypass -File making_usb_bootable/making_usb_bootable_with_iso.ps1 %~1
echo ****************************************************************
python making_usb_bootable/get_usb_identifier.py
echo ****************************************************************
if %ERRORLEVEL% ==1 (
    echo ****** Restarting the system to get the usb_identifier ******
    python adding_registry_to_run_after_restart.py %~1
    shutdown -r
) else (
    python making_usb_bootable\set_usb_identifier.py
    echo ****************************************************************
    shutdown -r
    echo.&pause&goto:eof
)


