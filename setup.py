# -*- coding: utf-8 -*-

import codecs

from setuptools import setup


with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='dbb-ranking-parser',
    version='0.3.1-dev',
    description='Extract league rankings from the DBB (Deutscher Basketball Bund e.V.) website.',
    long_description=long_description,
    url='http://homework.nwsnet.de/releases/4a51/#dbb-ranking-parser',
    author='Jochen Kupperschmidt',
    author_email='homework@nwsnet.de',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Other/Nonlisted Topic',
    ],
    packages=['dbbrankingparser'],
    install_requires=['lxml>=3.4.0'],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'dbb-ranking = dbbrankingparser.cli:main',
            'dbb-ranking-server = dbbrankingparser.httpserver:main',
        ],
    },
)
