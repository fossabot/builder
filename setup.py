from distutils.core import setup
import setuptools
import io
import os
import re


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


long_description = read('README.rst')


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='builder',
    version=find_version('builder', 'version.py'),
    description='Builder CLI tool',
    long_description=long_description,
    url='https://github.com/waghanza/builder',
    author='Marwan Rabbâa',
    author_email='waghanza@gmail.com',
    license='MIT',
    classifiers=[
            'Development Status :: 1 - Planning',
            'Environment :: Console',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: MIT License'
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
    ],
    keywords='package linux distribution',
    packages=setuptools.find_packages(),
    install_requires=open('requirements.txt').readlines(),
    entry_points={'console_scripts': ['builder=builder:cli']}
)
