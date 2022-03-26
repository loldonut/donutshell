from setuptools import setup

version = '0.0.1rc3'
description = 'A Shell built-in Python but not meant for daily use.'

from pathlib import Path
this_dir = Path(__file__).parent
README = (this_dir / "README.md").read_text()

packages = [
    'donutshell',
    'donutshell.utils',
    'donutshell.builtin_modules'
]

setup(
    name='donutshell',
    version=version,
    author='loldonut',
    description=description,

    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/loldonut/donutshell',

    license='MIT',
    packages=packages,
    install_requires=['setuptools'],
    keywords=['shell', 'terminal', 'console'],

    entry_points={
        'console_scripts': [
            'donutshell = donutshell.__main__:main',
        ]
    },

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Topic :: System :: Shells',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Typing :: Typed'
    ],
)
