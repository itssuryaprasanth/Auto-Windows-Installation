$list = New-Object Collections.Generic.List[String]
[string]$Clean_device_txt_file_location = 'Disk_Part/Clean_Device_Through_Bat.txt'
if (!(Test-Path -Path $Clean_device_txt_file_location))
{
       throw "Disk Part Failed"
}

$content_data = Get-Content $Clean_device_txt_file_location
foreach($single_line in $content_data)
{
    $list.Add($single_line)
}
$string_regex = $list[4] -match ".*\s([A-Z])+"
if (!($string_regex))
{
   throw "DRIVER ASSIGNMENT IS NOT SET PROPERLY"
}


$Volumes = (Get-Volume).Where({$_.DriveLetter}).DriveLetter
Mount-DiskImage -ImagePath D:\Win11_22H2_English_x64v1.iso
$ISO = (Compare-Object -ReferenceObject $Volumes -DifferenceObject (Get-Volume).Where({$_.DriveLetter}).DriveLetter).InputObject

Set-Location -Path "$($ISO):\boot"
bootsect.exe /nt60 "{0}:" -f $Matches[1]
Copy-Item -Path "$($ISO):\*" -Destination "G:" -Recurse -Verbose
