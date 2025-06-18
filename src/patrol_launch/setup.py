from setuptools import setup
import os
from glob import glob

package_name = 'patrol_launch'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        (os.path.join('share', package_name), ['package.xml']),
        # 👇 This line includes launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Sai Ganesh',
    maintainer_email='ganeshrejeti1@gmail.com',
    description='Launch package for patrol bot',
    license='MIT',
    entry_points={
        'console_scripts': [],
    },
)
