@setlocal enableextensions
@cd /d "%~dp0"
@echo off
Title Installation Of Windows Continues
set PYTHONPATH= %PYTHONPATH%;%cd%
echo ****************************************************************
FOR /R "C:/Users/%USERNAME%/Downloads/OS_HAND_INSTALL_AUTOMATION/Language" %%F in (*.*) do (
    set language= %%~nF
)
python making_usb_bootable\get_usb_identifier.py
if %ERRORLEVEL% ==1 (
    sleep 7
    call:Windows %language%
    call:StatusChange 4
) else (
    call:Windows
    call:StatusChange 2
)
: Windows
echo *******************************************************************
python making_usb_bootable\set_usb_identifier.py
echo ****************************************************************
goto exit /b
: StatusChange
set NUM=0 %1
for %%x in (%NUM%) do (
    for %%y in (%NUM%) do (
        color %%x%%y
        timeout 1 >nul
    )
)
if %1% ==4 (
    echo 			*********************************************************************************************
    echo 			*                                                                                            *
    echo 			*  Failed !! to get usb identifier, select usb from bios menu to start installation          *
    echo 			*                                                                                            *
    echo 			*********************************************************************************************
    shutdown -r
    pause
) else (
  echo 			***********************************************************
  echo 			*                                                         *
  echo				*  Passed !! Starting windows installation after restart  *
  echo 			*                                                         *
  echo 			***********************************************************
  shutdown -r
  pause
)
goto quit