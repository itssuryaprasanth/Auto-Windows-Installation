$current_user_name = [Environment]::UserName
$list = New-Object Collections.Generic.List[String]

$iso_path = "C:\\Users\\{0}\\Downloads\\OS_HAND_INSTALL_AUTOMATION\\"

$iso_path = $iso_path.Replace("{0}",$current_user_name)
$iso_from_Exe = $args[0]
$iso_from_Exe = $iso_from_Exe -replace ' ',''
$iso_image_name ="{0}_22H2.iso" -f $iso_from_Exe
$temp_iso_path = $iso_path+ $iso_image_name

$iso_unattend = "autounattend.xml"
$attend_xml_path = $iso_path+ $iso_unattend
$alienware_tool_center = "Alienware Tools Center.msi"
$temp_alienware_tool_center = $iso_path+$alienware_tool_center

$windows_desktop = "windowsdesktop-runtime-6.0.11-win-x64.exe"
$temp_windows_desktop = $iso_path+$windows_desktop

$windows_install_bat = "Install.bat"
$temp_windows_install_bat = $iso_path+$windows_install_bat

[string]$Clean_device_txt_file_location = 'disk_part/clean_usb_device.txt'
if (!(Test-Path -Path $Clean_device_txt_file_location))
{
       throw "DISK PART FAILED"
}

$content_data = Get-Content $Clean_device_txt_file_location
foreach($single_line in $content_data)
{
    $list.Add($single_line)
}
$string_regex = $list[4] -match ".*\s([A-Z])+"
$usb_driver = $Matches[1]

if (!($string_regex))
{
   throw "DRIVER ASSIGNMENT IS NOT SET PROPERLY"
}


$Volumes = (Get-Volume).Where({$_.DriveLetter}).DriveLetter
Mount-DiskImage -ImagePath $temp_iso_path
$ISO = (Compare-Object -ReferenceObject $Volumes -DifferenceObject (Get-Volume).Where({$_.DriveLetter}).DriveLetter).InputObject

Set-Location -Path "$($ISO):\boot"
bootsect.exe /nt60 "{0}:" -f $Matches[1]
Copy-Item -Path "$($ISO):\*" -Destination "$($usb_driver):" -Recurse -Verbose
Copy-Item -Path $attend_xml_path -Destination "$($usb_driver):" -Recurse -Verbose
Set-Location -Path "$($usb_driver):"
New-Item -Path "EXE" -ItemType Directory
Copy-Item -Path $temp_alienware_tool_center -Destination "EXE" -Recurse -Verbose
Copy-Item -Path $temp_windows_desktop -Destination "EXE" -Recurse -Verbose
Copy-Item -Path $temp_windows_install_bat -Destination "EXE" -Recurse -Verbose