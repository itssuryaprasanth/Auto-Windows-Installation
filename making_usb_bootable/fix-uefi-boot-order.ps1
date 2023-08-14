$current_project_location= Get-Location
$current_user_name = [Environment]::UserName
$iso_path = "C:\\Users\\{0}\\Downloads\\OS_HAND_INSTALL_AUTOMATION"
$iso_path = $iso_path.Replace("{0}",$current_user_name)

Set-Location $iso_path
$secondBootEntry = Get-Content -Path "boot.txt"

Write-Host "cmd /c bcdedit $bcdParams /set `"{fwbootmgr}`" displayorder $secondBootEntry /addfirst"
Set-Location $current_project_location