# Module help you to get usb identifier from bcdedit
import re
import subprocess
import sys
from utilities.file_logger import file_logger
from formatters.get_usb_device_id import get_usb_device_id_from_disk_part_log

usb_id = get_usb_device_id_from_disk_part_log()
log = file_logger()


def restart_system_get_attached_usb_identifier():
    log.debug("trying to get attached usb identifier")
    try:
        cmd = "bcdedit /enum FIRMWARE"
        cli_output = subprocess.run(cmd, capture_output=True)
        shell_regex = str(cli_output.stdout).replace('\n', '')
        regx_expr = "\W.*\W.*({.*}).*device*\W.*" + f"partition={usb_id[1]}:"
        try:
            usb_identifier = re.search(regx_expr, shell_regex).group(1)
            print(f"USB IDENTIFIER --> {usb_identifier}")
            log.info("Got the usb identifier")
            return usb_identifier
        except AttributeError:
            log.debug("failed to get usb identifier, trying after restart")
            sys.exit(1)
    except subprocess.SubprocessError:
        sys.exit(2)


restart_system_get_attached_usb_identifier()
