from setuptools import setup

setup(
    name='keebsound',
    version='0.0.1',
    packages=['keeb'],
    url='https://github.com/sillyfatcat/keebsound',
    license='MIT',
    author='Shelby Shum',
    author_email='sshum00@gmail.com',
    description='Keeb generates realistic keyboard sounds depending on the input',
    keywords=['KEYBOARD', 'SOUND', 'MECHANICAL KEYBOARD'],
    download_url='https://github.com/sillyfatcat/keebsound/archive/v0.1.tar.gz',
    install_requires=[
        'click',
        'playsound',
        'pynput'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': ['keeb=keeb.main:main']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
