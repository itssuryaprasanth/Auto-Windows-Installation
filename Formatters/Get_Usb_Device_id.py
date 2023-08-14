# Module will help you to format your USB and recreate it again by assigning a new letter to it
import os
import re
import subprocess
from utilities.file_logger import file_logger

usb_logs = "C:/Windows/Temp/usb_device.txt"
disk_part_bat = rf"{os.getcwd()}\disk_part\clean_usb_device.txt"

log = file_logger()


def get_usb_letter_with_wmic():
    log.info("Getting Usb Letter With WMIC CLI")
    cmd = "wmic logicaldisk where drivetype=2 get description ,deviceid ,volumename"
    cli_output = subprocess.run(cmd, capture_output=True)
    cli_output_with_id = str(cli_output.stdout).strip('\n')
    log.info(cli_output_with_id)
    try:
        usb_letter = re.search("\W+([A-Z]):", cli_output_with_id).group().strip(":").lstrip()
        log.info(f"Got the USB letter -->{usb_letter}")
        return usb_letter
    except AttributeError:
        log.info("Unable to find USB Letter")
        raise Exception("UNABLE TO FIND USB LETTER FROM WMIC")


def get_usb_device_id_from_disk_part_log():
    log.info("Getting USB Volume Id With Diskpart")
    log.debug("Open Disk Part logs, present windows temp folder")
    with open(usb_logs) as usb_file:
        content_file = usb_file.readlines()
        log.info(content_file)
        try:
            attached_usb_letter = get_usb_letter_with_wmic()
            attached_usb_id = re.search(f"Volume\s(\d)\s+({attached_usb_letter}).*",
                                        content_file[-1].strip()).group(1)
            return int(attached_usb_id), str(attached_usb_letter)
        except AttributeError:
            usb_file.close()
            print("USB IS NOT ATTACHED TO THE SYSTEM OR CANNOT ABLE TO RECOGNIZE PROPERLY")


def send_usb_device_id_to_disk_part(usb_device_id):
    log.debug("Sending usb device id to disk part")
    with open(disk_part_bat, mode='w') as usb_file:
        data = f"select volume {usb_device_id[0]} \n" \
               "clean \n" \
               "create partition primary \n" \
               "format quick fs=ntfs \n" \
               f"assign letter= {usb_device_id[1]}"
        usb_file.write(data)
        usb_file.close()
    log.info("Successfully written usb id to disk part code")
    log.debug(data)


usb_id = get_usb_device_id_from_disk_part_log()
send_usb_device_id_to_disk_part(usb_device_id=usb_id)
