"""
QUESTION:
Create a function `generate_spack_package_spec` that generates a Spack package specification based on the given code snippet. The function should take the code snippet as input and return the Spack package specification as a string. The package specification should include the version, SHA256 hash, and variant declarations for each version specified in the code snippet. The code snippet is expected to contain information about different versions of a package, their SHA256 hashes, and various package variants. The function should parse this information and generate a Spack package specification string accordingly. The package specification should be in the format of "spack package add package-name@version sha256=hash" for each version and "spack package add package-name@version +variant" or "spack package add package-name@version ~variant" for each variant.
"""

def generate_spack_package_spec(code_snippet):
    package_spec = ""
    versions = []
    sha256_hashes = {}
    variants = []

    # Parse the code snippet to extract version, sha256, and variant information
    for line in code_snippet.split('\n'):
        if line.startswith("version"):
            version_info = line.split('version(')[1].split(')')[0].replace("'", "").split(',')
            version = version_info[0].strip()
            versions.append(version)
            if 'sha256' in version_info[1]:
                sha256 = version_info[1].split('sha256=')[1].strip()
                sha256_hashes[version] = sha256
            if 'url' in version_info[1]:
                url = version_info[1].split('url=')[1].strip()
                sha256_hashes[version] = f"url={url}"

        if line.startswith("variant"):
            variant_info = line.split('variant(')[1].split(')')[0].replace("'", "").split(',')
            variant_name = variant_info[0].strip()
            default = variant_info[1].strip().split('=')[1].strip()
            description = variant_info[2].strip().split('=')[1].strip()
            variants.append((variant_name, default, description))

    # Generate the package specification for each version and variant combination
    for version in versions:
        package_spec += f"spack package add package-name@{version} sha256={sha256_hashes[version]}\n"
        for variant in variants:
            package_spec += f"spack package add package-name@{version} {'+' if variant[1] == 'True' else '~'}{variant[0]}\n"

    return package_spec