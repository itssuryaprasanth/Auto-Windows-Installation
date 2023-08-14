# Auto-Windows-Installation
Auto Install Windows Without User Actions
# Windows OS Automated Installation Tool

The **Windows OS Automated Installation Tool** is a user-friendly utility designed to streamline the entire process of installing the Windows operating system. This tool eliminates the need for manual intervention, making OS installation efficient and hassle-free. By combining a Python-based backend with the power of the `autounattend.xml` configuration, the tool ensures a seamless end-to-end experience.

## Features

- **Effortless Installation**: Say goodbye to manual OS installation. This tool automates the entire process, from booting via a USB flash drive to completing the Out-of-Box Experience (OOBE) process.
- **User-Friendly Interface**: The tool boasts a user-friendly interface that accepts crucial user inputs, such as the desired OS language and type (Home/Pro), making the installation process highly customizable.
- **Minimal Setup**: Simply install the tool on the target platform along with a bootable USB flash drive connected to the system and a functioning internet connection.
- **Python-Powered**: The backend of the tool is built using Python, ensuring efficiency, reliability, and flexibility in handling the installation process.
- **Autounattend.xml Integration**: The tool seamlessly integrates the `autounattend.xml` configuration file to efficiently manage the OOBE process, making sure all post-installation tasks are completed without user intervention.

## How It Works

1. **Input Selection**: The user provides input for the desired OS language and type (Home/Pro) through the tool's interface.
2. **Initialization**: The tool's Python backend initiates the OS installation process using the provided inputs.
3. **Bootable USB**: The system boots from the connected bootable USB flash drive, which contains the necessary installation files.
4. **Autounattend.xml Magic**: The `autounattend.xml` configuration file takes charge, automating the OOBE process. This ensures a seamless setup experience.
5. **Completion**: Once the installation and configuration are complete, the system is ready for use without any manual intervention required.

## Requirements

- Target platform with the tool installed.
- Bootable USB flash drive connected to the platform.
- Functional internet connection for necessary downloads.

## Usage

1. Clone this repository to your local machine.
2. Install the Python on the target platform.
3. Launch the tool and provide the required inputs for OS language and type.
4. Sit back and relax as the tool automates the entire OS installation process.

## Getting Started

For detailed instructions on setting up and using the Windows OS Automated Installation Tool
1. Target Machine IP ( Where you store all your ISO's, unattend.xml)
2. Install latest python (Preferable 3.8.10)
3. utilities\network_connection_check.py --> Will help to check your target machine is reachable or not.
4. utilities\local_connection_to_server.py --> Will create a ssh connection between local machine and target machine and brings out ISO file and stash it in local.
5. making_usb_bootable library will help to make create your USB as bootable and also set your USB as first priority for BOOT ORDER.
6. Replace Tester name with your name in autounattend.xml. For more information https://www.windowsafg.com/win10x86_x64_uefi.html

## Contributions

Contributions are welcome! If you have suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

---

By automating the Windows OS installation process, the Windows OS Automated Installation Tool simplifies and enhances the user experience. Enjoy a swift and efficient installation journey with minimal effort!
