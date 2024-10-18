import subprocess
import sys

# List of packages you want to install
packages = [
    'cairo-devel', #Cairo
    'libjpeg-turbo-devel', #LibTurboJPEG
    'libpng-devel', #LibPNG
    'libtool' #LibTool
    'libuuid-devel', #LibUUID
    'freerdp-devel', #FreeRDP
    'pango-devel', #Pango
    'libssh2-devel', #LibSSH
    'openssl-devel', #OpenSSL
]

def install_packages(package_list):
    for package in package_list:
        subprocess.check_call([sys.executable, '-m', 'dnf', 'install', package])

if __name__ == "__main__":
    install_packages(packages)