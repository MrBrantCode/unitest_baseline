"""
QUESTION:
Create a function `create_package_config` that takes in `name`, `deps`, `readme_md`, `license_banner`, and `**kwargs` as parameters. The function should process the `kwargs` to extract optional parameters `visibility`, `substitutions`, `ng_packager`, and `terser_config_file` with default values if not provided. The default values should be `None` for `visibility`, `PKG_GROUP_REPLACEMENTS` for `substitutions`, `_INTERNAL_NG_PACKAGE_PACKAGER` for `ng_packager`, and `_INTERNAL_NG_PACKAGE_DEFALUT_TERSER_CONFIG_FILE` for `terser_config_file`. The function should then construct and return a package configuration dictionary with the processed parameters and default values.
"""

def create_package_config(name, deps, readme_md, license_banner, **kwargs):
    visibility = kwargs.pop("visibility", None)
    substitutions = kwargs.pop("substitutions", PKG_GROUP_REPLACEMENTS)
    ng_packager = kwargs.pop("ng_packager", _INTERNAL_NG_PACKAGE_PACKAGER)
    terser_config_file = kwargs.pop("terser_config_file", _INTERNAL_NG_PACKAGE_DEFALUT_TERSER_CONFIG_FILE)

    package_config = {
        "name": name,
        "deps": deps,
        "readme_md": readme_md,
        "license_banner": license_banner,
        "visibility": visibility,
        "substitutions": substitutions,
        "ng_packager": ng_packager,
        "terser_config_file": terser_config_file
    }

    return package_config