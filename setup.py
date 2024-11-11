"""
Setup configuration for Treecraft package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="treecraft",
    version="0.1.0",
    author="Ashwin Murali",
    author_email="ashwinmurali27@gmail.com",
    description="Generate directory structures from text-based tree representations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/treecraft",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "treecraft=treecraft.cli:main",
        ],
    },
)