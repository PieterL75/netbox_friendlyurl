from setuptools import find_packages, setup

setup(
    name='netbox_friendlyurl',
    version='0.2',
    description='Netbox Friendly URLs',
    long_description='Create urls in NetBox that are more user friendly and that redirect to real netbox urls',
    long_description_content_type='text/x-rst',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
