import io

from setuptools import setup
from setuptools import find_packages

setup(
  name='ker.py',
  version='0.0.2',
  description='Hostker Python SDK',
  author='SkyAo',
  author_email='csvwolf@qq.com',
  packages=find_packages(),
  long_description=io.open('README.md', encoding='utf-8').read()
)