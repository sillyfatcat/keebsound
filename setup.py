from setuptools import setup

setup(
    name='keebsound',
    version='0.0.1',
    packages=['keeb'],
    url='',
    license='',
    author='Shelby Shum',
    author_email='sshum00@gmail.com',
    description='Keeb generates realistic keyboard sounds depending on the input',
    install_requires=[
        'click',
        'playsound',
        'pynput'
    ],
    entry_points={
        'console_scripts': ['keeb=keeb.main:main']
    }
)
