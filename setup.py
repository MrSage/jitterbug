from setuptools import setup, find_packages
from datetime import datetime

version = '%s' % datetime.now().strftime("%Y-%m-%d-%H_%M_%S_%f")

setup(
    name='jitterbug',
    version=version,
    description="Just In Time Transpiler for Django",
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['django', 'httpagentparser'],
)