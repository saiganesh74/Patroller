from setuptools import setup

package_name = 'patrol_navigation'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Sai Ganesh',
    maintainer_email='ganeshrejeti1@gmail.com',
    description='Handles patrol path logic',
    license='MIT',
    entry_points={
        'console_scripts': [
            'patrol_node = patrol_navigation.patrol_node:main',
        ],
    },
)
