from setuptools import setup

package_name = 'square_challehnge'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gadorneles',
    maintainer_email='dorneles1215@gmail.com',
    description='ROS 2 package for the turtle challenge',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'challenge_node = turtle_challenge.challenge_node:main',
        ],
    },
)
