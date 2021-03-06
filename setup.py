import dtf

from setuptools import setup
from sys import version_info

REQUIRES = ['pyyaml']

if version_info < (2, 7):
    # no argparse in 2.6 standard
    REQUIRES.append('argparse')


setup(
    name='dtf',
    maintainer='tychoish',
    maintainer_email='sam@tychoish.com',
    description='Documentation Testing Framework',
    version=dtf.__version__,
    license='Apache',
    url='http://cyborginstitute.org/projects/dtf',
    packages=['dtf'],
    install_requires=REQUIRES,
    test_suite=None,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Documentation',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'License :: OSI Approved :: Apache Software License',
    ],
    entry_points={
        'console_scripts': [
            'dtf = dtf.dtf:main',
            ],
        }
    )
