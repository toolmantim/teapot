"""
Setup file for the Teapot WSGI middleware package.
"""

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="teapot",
    version="1.0.1",
    author="Tim Lucas",
    description="WSGI middleware implementing RFC 2324 - HTCPCP/1.0 (I'm a teapot)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/toolmantim/teapot",
    py_modules=["teapot"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "License :: Public Domain",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.6",
    test_suite="test_teapot",
)
