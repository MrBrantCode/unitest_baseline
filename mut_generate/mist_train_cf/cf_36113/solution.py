"""
QUESTION:
Write a function `generate_xctool_command` that takes two parameters: `platform` (string, one of "iPhoneOS", "iPhoneSimulator", or "Mac") and `build_type` (string, one of "library", "test", or "framework" for Mac only). The function should return a string representing the corresponding xctool command based on the input `platform` and `build_type`. If the input `platform` or `build_type` is invalid, the function should return "Invalid platform or build type".
"""

def generate_xctool_command(platform, build_type):
    if platform == "iPhoneOS":
        if build_type == "library":
            return 'xctool -project build-mac/mailcore2.xcodeproj -sdk iphoneos7.1 -scheme "static mailcore2 ios" build ARCHS="armv7 armv7s arm64"'
        elif build_type == "test":
            return '#echo Link test for iPhoneOS\nxcodebuild -project build-mac/mailcore2.xcodeproj -sdk iphoneos7.1 -target "test-ios" CODE_SIGN_IDENTITY="" build'
    elif platform == "iPhoneSimulator":
        if build_type == "library":
            return 'xctool -project build-mac/mailcore2.xcodeproj -sdk iphonesimulator7.1 -scheme "static mailcore2 ios" build ARCHS="i386 x86_64"'
        elif build_type == "test":
            return 'xctool -project build-mac/mailcore2.xcodeproj -sdk iphonesimulator7.1 -scheme "test-ios" build ARCHS="i386 x86_64"'
    elif platform == "Mac":
        if build_type == "library":
            return 'xctool -project build-mac/mailcore2.xcodeproj -sdk macosx10.8 -scheme "static mailcore2 osx" build'
        elif build_type == "framework":
            return 'xctool -project build-mac/mailcore2.xcodeproj -sdk macosx10.8 -scheme "mailcore osx" build'
        elif build_type == "test":
            return 'xctool -project build-mac/mailcore2.xcodeproj -sdk macosx10.8 -scheme "tests" build'
    return "Invalid platform or build type"