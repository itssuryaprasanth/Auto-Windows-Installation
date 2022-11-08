$list = New-Object Collections.Generic.List[String]
[string]$Clean_device_txt_file_location = 'Clean_Device_Through_Bat.txt'
if (!(Test-Path -Path $Clean_device_txt_file_location))
{
       throw "Disk Part is not cleaned properly"
}

$content_data = Get-Content $Clean_device_txt_file_location
foreach($single_line in $content_data)
{
    $list.Add($single_line)
}

$string_regex = $list[4] -match ".*\s([A-Z])+"
Write-Host $string_regex
if ($string_regex)
{
    Write-Host $Matches[1]
}