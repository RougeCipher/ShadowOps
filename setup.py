# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ShadowOps",
    version="1.0.0",
    author="Vishnu",
    author_email="rougedevexplorer@gmail.com",
    description="A playful Python package that modifies built-in functions for fun.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ShadowOps",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'shadowops=shadowops.cli:main',
        ],
    },
    install_requires=[
        # List your dependencies here, e.g.,
        # "requests>=2.25.1",
    ],
    include_package_data=True,
)
