import math
import os
import sys
import paramiko

user_selection = sys.argv[1]
dir_path = "YOUR ISO DIRECTORY PATH EG: D:\\ISO\\English"
main_dir = "YOUR MAIN DIRECTORY EG:D:\\ISO"

folder_location = rf"C:\\Users\\{os.getenv('USERNAME')}\\Downloads\\OS_HAND_INSTALL_AUTOMATION"


def progressbar(x, y):
    bar_len = 60
    filled_len = math.ceil(bar_len * x / float(y))
    percents = math.ceil(100.0 * x / float(y))
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    file_size = f'{math.ceil(y / 1024):,} KB' if y > 1024 else f'{y} byte'
    sys.stdout.write(f'[{bar}] {percents}% {file_size}\r')
    sys.stdout.flush()


if not (os.path.exists(folder_location)):
    os.mkdir(folder_location)

print(user_selection)
ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_connection.connect(hostname="****", username="****", password="*****", port=22)  # for password check with creator
sftp_connection = ssh_connection.open_sftp()
sftp_connection.chdir("YOUR DESIRED DIRECTORY")
sftp_connection.chdir(f"{user_selection}")
print("GETTING ISO FILE FROM REMOTE SERVER")
sftp_connection.get(remotepath=f"{user_selection}" + "_22H2" + ".iso",
                    localpath=folder_location + '\\' + f"{user_selection}" + "_22H2" + ".iso",
                    callback=lambda x, y: progressbar(x, y))
sftp_connection.get(remotepath="autounattend.xml", localpath=folder_location + '\\' + 'autounattend.xml',
                    callback=lambda x, y: progressbar(x, y))
print("SUCCESSFULLY PLACED ISO FILE IN YOUR LOCAL")
sftp_connection.close()
ssh_connection.close()
