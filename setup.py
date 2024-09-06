from setuptools import setup, find_packages

setup(
    name="nmap_scanner",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "python-nmap",
    ],
    entry_points={
        "console_scripts": [
            "nmap_scan=run_scanner:main",
        ],
    },
    author="Your Name",
    description="A Python project for scanning hosts using Nmap",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/nmap_scanner",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

