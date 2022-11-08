@setlocal enableextensions
@cd /d "%~dp0"
@echo off
Title Installing Windows
set PYTHONPATH= %PYTHONPATH%;%cd%
echo ****************************************************************
diskpart /s Disk_Part/get_attached_usb_device_id.txt > Logs/usb_device.txt
echo ****************************************************************
python Formatters\Get_Usb_Device_id.py
echo ****************************************************************
diskpart /s Disk_Part/Clean_Device_Through_Bat.txt
echo ****************************************************************
Powershell.exe -ExecutionPolicy Bypass -File Usb_Bootable/Usb_boot.ps1
echo ****************************************************************
pause
exit /b
