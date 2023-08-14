@setlocal enableextensions
@cd /d "%~dp0"
@echo off

echo Installing Open SSH Server

powershell.exe -Command Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

echo Installing Open SSH Client

powershell.exe -Command Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0