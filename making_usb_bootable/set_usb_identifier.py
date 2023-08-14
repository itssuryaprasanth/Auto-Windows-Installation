# Module will help to set your USB as first priority in BOOT ORDER
import os
from making_usb_bootable.get_usb_identifier import restart_system_get_attached_usb_identifier

folder_location = rf"C:\\Users\\{os.getenv('USERNAME')}\\Downloads\\OS_HAND_INSTALL_AUTOMATION\\boot.txt"


def set_usb_identifier_as_first_boot():
    file_name = "C:\Windows\Temp\make_usb_as_first_priority.txt"
    usb_id = restart_system_get_attached_usb_identifier()
    if not os.path.exists(file_name):
        set_boot_priority(usb_device_id=usb_id)
    else:
        os.mkdir(file_name)
        set_boot_priority(usb_device_id=usb_id)


def set_boot_priority(usb_device_id):
    with open(folder_location, 'w+') as boot_file:
        boot_file.write(usb_device_id)
        boot_file.close()
        cmd = "bcdedit /set ""\"{fwbootmgr}\""" displayorder " + f"{usb_device_id} /addfirst"
        cli_output = os.system(f"cmd /C {cmd}")
        if not cli_output == 0:
            print("PLEASE GO FOR MANUAL BOOT THROUGH BIOS MENU")


set_usb_identifier_as_first_boot()
