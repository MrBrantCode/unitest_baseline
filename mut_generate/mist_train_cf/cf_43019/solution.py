"""
QUESTION:
Write a function named `configure_ndk_flags` that takes two parameters: `ndk_version` (str) and `architecture` (str). The function should return a dictionary containing 'CPPFLAGS' and 'LINKFLAGS' as keys, which are lists of compiler and linker flags respectively. 

The function must handle the following cases:
- If the `ndk_version` is greater than or equal to 15.0.4075724, add flags to 'CPPFLAGS' and 'LINKFLAGS'.
- If the `ndk_version` is greater than or equal to 17.1.4828580, include additional linker flags in 'LINKFLAGS'. 

Assume that variables `target_opts`, `common_opts`, `env`, `lib_sysroot` are defined elsewhere in the code.
"""

from distutils.version import LooseVersion

def configure_ndk_flags(ndk_version: str, architecture: str) -> dict:
    flags = {'CPPFLAGS': [], 'LINKFLAGS': []}

    if ndk_version is not None and LooseVersion(ndk_version) >= LooseVersion("15.0.4075724"):
        flags['CPPFLAGS'].extend(['-target', target_opts, common_opts])

        if LooseVersion(ndk_version) >= LooseVersion("17.1.4828580"):
            flags['LINKFLAGS'].extend(['-Wl,--exclude-libs,libgcc.a', '-Wl,--exclude-libs,libatomic.a', '-nostdlib++'])
        else:
            flags['LINKFLAGS'].append(env["ANDROID_NDK_ROOT"] + "/sources/cxx-stl/llvm-libc++/libs/" + architecture + "/libandroid_support.a")

        flags['LINKFLAGS'].extend(['-shared', '--sysroot=' + lib_sysroot, '-Wl,--warn-shared-textrel'])
        flags['LIBPATH'] = [env["ANDROID_NDK_ROOT"] + "/sources/cxx-stl/llvm-libc++/libs/" + architecture + "/"]
        flags['LINKFLAGS'].append(env["ANDROID_NDK_ROOT"] + "/sources/cxx-stl/llvm-libc++/libs/" + architecture + "/libc++_shared.so")

    return flags