import os

from setuptools import setup

VERSION_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            'betterdicts', 'version.py')

DESCRIPTION = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read()

VERSION = None
with open(VERSION_FILE, 'r') as f:
    VERSION = f.read().split()[2][1:-1]


setup(
    name='betterdicts',
    version=VERSION,
    packages=['betterdicts'],
    url='https://github.com/Lguyogiro/BetterDict',
    license='MIT',
    author='Robert Pugh, Patrick Lange',
    author_email='robert.pugh408@gmail.com, mail@langep.com',
    description=(
        'Mergeable Python dictionary/OrderedDict/defaultdict/Counter '
        'with arithmetic operator support'
    ),
    long_description=DESCRIPTION,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries :: Python Modules'
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)