import re
import sys
from Utilties.File_Logger import File_Logger

# log = File_Logger()

_usb_logs = r"C:\Users\AWCC\PycharmProjects\Remote Windows\Logs\usb_device.txt"
_disk_part_bat = r"C:\Users\AWCC\PycharmProjects\Remote Windows\Disk_Part\Clean_Device_Through_Bat.txt"


def get_usb_device_id_from_disk_part_log():
    try:
        with open(_usb_logs) as _usb_file:
            content_file = _usb_file.readlines()
            try:
                attached_usb_id = re.search("Volume\s(\d)\s+([A-Z]).*(Removable).*", content_file[-1].strip()).group(1)
                attached_usb_letter = re.search("Volume\s(\d)\s+([A-Z]).*(Removable).*",
                                                content_file[-1].strip()).group(2)
                return int(attached_usb_id), str(attached_usb_letter)
            except AttributeError:
                _usb_file.close()
                print("USB IS NOT ATTACHED TO THE SYSTEM OR CANNOT ABLE TO RECOGNIZE PROPERLY")
    except:
        print(sys.exc_info())


def send_usb_device_id_to_disk_part(usb_id):
    try:
        with open(_disk_part_bat, mode='w') as _usb_file:
            data = f"select volume {usb_id[0]} \n" \
                   "clean \n" \
                   "create partition primary \n" \
                   "format quick fs=ntfs \n" \
                   f"assign letter= {usb_id[1]}"
            _usb_file.write(data)
            _usb_file.close()
    except:
        print(sys.exc_info())


_usb_id = get_usb_device_id_from_disk_part_log()
send_usb_device_id_to_disk_part(usb_id=_usb_id)
