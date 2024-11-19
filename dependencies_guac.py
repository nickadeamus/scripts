import subprocess

# List of packages you want to install
packages = [
    'java',
    'cairo-devel',
    'libjpeg-turbo-devel',
    'libpng-devel',
    'libtool',
    'libuuid-devel',
    'freerdp-devel',
    'pango-devel',
    'libssh2-devel',
    'openssl-devel'
]

def install_packages(package_list):
    command = ['sudo', 'dnf', 'install', '-y'] + package_list
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        print("Command output:")
        print(e.output)

if __name__ == "__main__":
    install_packages(packages)
