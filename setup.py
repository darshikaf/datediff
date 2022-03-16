import os
from pathlib import Path

from setuptools import find_packages, setup

name = "datediff"
version_basepath = "_version"
pysrc_dir = "."
packages = [p for p in find_packages(pysrc_dir) if not p.startswith("tests")]
package_dir = {"": pysrc_dir}

# only add the version if it exists
version_fname = Path(f"{name}/{version_basepath}")
if version_fname.exists():
    with version_fname.open("r") as f:
        version = f.read().strip()
else:
    version = os.getenv("VERSION", "0.0.0")
    with version_fname.open("w") as f:
        f.write(version)

data_files = ["LICENSE"]

entry_points = {"console_scripts": ["datediff = datediff.cli:app"]}

with open("LICENSE") as f:
    _license = f.read()

setup(
    name=name,
    version=version,
    description="Application to compute difference between two Dates",
    url=f"https://github.com/darshikaf/{name}",
    author="",
    author_email="",
    packages=packages,
    package_dir=package_dir,
    data_files=data_files,
    include_package_data=True,
    zip_safe=False,
    entry_points=entry_points,
)
