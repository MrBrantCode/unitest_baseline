"""
QUESTION:
Implement the `install_package` function, which takes a package name, a list of dependencies, and a boolean flag indicating whether the package should be installed in "zip-safe" mode. The function should return a string indicating the installation status. If the installation is successful, return a string in the format "Package <package_name> installed successfully in <mode> mode". If the installation fails due to missing dependencies, return a string in the format "Failed to install <package_name>: missing dependencies: <missing_dependencies>". The function should assume that all packages and dependencies are unique and that there are no circular dependencies.
"""

def install_package(package_name, dependencies, zip_safe):
    installed_packages = set()

    def install_helper(pkg, deps):
        if pkg in installed_packages:
            return
        for dep in deps:
            if dep not in installed_packages:
                return dep
        installed_packages.add(pkg)

    missing_deps = install_helper(package_name, dependencies)
    if missing_deps:
        return f"Failed to install {package_name}: missing dependencies: {missing_deps}"

    mode = "zip-safe" if zip_safe else "regular"
    return f"Package {package_name} installed successfully in {mode} mode"