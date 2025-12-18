"""
QUESTION:
Create a function `generate_fpm_command` that generates the command for the `fpm` tool to create a Debian package. The function takes the following parameters: 
- `prefix` (string): A prefix to be used in the package name.
- `package_name` (string): The name of the package.
- `version` (string): The version of the package.
- `description` (string): A brief description of the package.
- `email` (string): The email of the package maintainer.
- `local_path` (string): The local path where the package files and scripts are located.

The function should construct the `fpm` command with the following options:
- Source type: `dir`
- Target type: `deb`
- Package name: `hifi-${prefix}${package_name}`
- Version: `${VERSION}` 
- Maintainer: `${EMAIL}`
- Vendor: "High Fidelity Inc"
- URL: "https://highfidelity.com"
- License: "Apache License 2.0"
- Description: `${DESCRIPTION}`
- Dependencies: `libgomp1`, `libtbb2`, `libgl1-mesa-glx`, `libnss3`, `libxi6`, `libxcursor1`, `libxcomposite1`, `libasound2`, `libxtst6`, `libxslt1.1`
- Template scripts and values: `service=hifi-${package_name}`
- Systemd service file: `${LOCAL_PATH}/hifi-${package_name}`
- Before/after install and remove scripts: `${LOCAL_PATH}/${package_name}-before-install.sh`, `${LOCAL_PATH}/after-install.sh`, `${LOCAL_PATH}/before-remove.sh`

The function should return the constructed `fpm` command as a string.
"""

def generate_fpm_command(prefix, package_name, version, description, email, local_path):
    fpm_command = f"fpm -s dir -t deb -n hifi-{prefix}{package_name} -v {version} -m '{email}' --vendor 'High Fidelity Inc' " \
                  f"--url 'https://highfidelity.com' --license 'Apache License 2.0' --description '{description}' " \
                  f"-d libgomp1 -d libtbb2 -d libgl1-mesa-glx -d libnss3 -d libxi6 -d libxcursor1 -d libxcomposite1 " \
                  f"-d libasound2 -d libxtst6 -d libxslt1.1 --template-scripts --template-value 'service'='hifi-{package_name}' " \
                  f"--deb-systemd {local_path}/hifi-{package_name} --before-install {local_path}/{package_name}-before-install.sh " \
                  f"--after-install {local_path}/after-install.sh --before-remove {local_path}/before-remove.sh"
    return fpm_command