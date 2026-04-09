import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'sensor_demo'

setup(
    name='sensor_demo',
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/sensor_demo']),
        ('share/sensor_demo', ['package.xml']),
        # Include all launch files in the package
        (os.path.join('share', 'sensor_demo', 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publisher_node = sensor_demo.publisher_node:main',
            'subscriber_node = sensor_demo.subscriber_node:main', 
        ],
    },
)
