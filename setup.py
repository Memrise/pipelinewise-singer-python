#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="pipelinewise-singer-python",
      version='3.0.0',
      description="Singer.io utility library - PipelineWise compatible",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="TransferWise",
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3 :: Only'
      ],
      url="https://github.com/transferwise/pipelinewise-singer-python",
      install_requires=[
          'pytz==2024.1',
          'jsonschema==4.23.0',
          'orjson==3.10.7',
          'python-dateutil==2.9.0.post0',
          'backoff==2.2.1',
          'ciso8601==2.3.1',
      ],
      extras_require={
          'dev': [
              'pylint==3.2.7',
              'pytest==8.3.3',
              'coverage[toml]==7.6.1',
          ]
      },
      packages=['singer'],
      package_data={
          'singer': [
              'logging.conf'
          ]
      },
      include_package_data=True
      )
