from setuptools import find_packages, setup

setup(
    name='netbox_friendlyurl',
    version='0.1',
    description='Create urls in NetBox that are more user friendly and that redirect to real netbox urls',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
