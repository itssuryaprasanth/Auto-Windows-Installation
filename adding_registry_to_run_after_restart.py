import os
import sys
from utilities.file_logger import file_logger

user_selection = sys.argv[1]
folder_location = rf"C:\\Users\\{os.getenv('USERNAME')}\\Downloads\\OS_HAND_INSTALL_AUTOMATION"
log = file_logger()


def adding_exe_to_reg_run_once():
    log.debug("Adding registries to run batch file after restart")
    cwd = os.getcwd() + r'\run_after_restart.bat'
    os.system(
        f'cmd /C "REG ADD "HKLM\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\RunOnce" /v exe /t REG_SZ /d "{cwd}" /f"')
    try:
        os.chdir(folder_location)
        final_path = folder_location + "\\Language"
        os.mkdir(final_path)
        final_path = final_path + "\\" + user_selection
        with open(final_path, 'x') as file_location:
            file_location.close()
        log.info("Successfully added to registry")
    except OSError:
        log.debug(sys.exc_info())
        sys.exit(1)


adding_exe_to_reg_run_once()
