"""
QUESTION:
Create a function `generate_docker_tags` that takes four parameters: `appname`, `image_type`, `version`, and `domain`, all of type `str`, and returns a tuple of two `str` values. The function should construct two Docker image tags: a meta tag and a release tag, each in the format "appname:image_type-version" and append the domain to the meta tag to form a phase meta tag, but return only two tags, the `meta_tag` and the `phase_meta_tag` in the format "registry.domain/appname:image_type-version".
"""

from typing import Tuple

def generate_docker_tags(appname: str, image_type: str, version: str, domain: str) -> Tuple[str, str]:
    registry = f"registry.{domain}"
    meta_tag = f"{appname}:{image_type}-{version}"
    phase_meta_tag = f"{registry}/{appname}:{image_type}-{version}"
    return meta_tag, phase_meta_tag