from setuptools import setup
import os
from glob import glob
from setuptools import find_packages

package_name = 'slampibot_bringup'

setup(
    name=package_name,
    version='6.0.0',
    packages=find_packages(exclude=[]),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', package_name, 'params'), glob(os.path.join('params', '*'))),
        (os.path.join('share', package_name, 'rviz'), glob(os.path.join('rviz', '*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Leo Cho',
    author_email='leohycho@gmail.com',
    maintainer='erail',
    maintainer_email='edurobotailab@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='ROS2 Foxy Packages for Slampibot',    
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bringup_node = slampibot_bringup.slampibot_bringup:main',
        ],
    },
)
