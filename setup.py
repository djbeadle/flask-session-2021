"""
Flask-Session
-------------

Flask-Session-2021 is an extension for Flask that adds support for
Server-side Session to your application.

`Flask-Session-2021` is a fork of the [Flask-Session](https://github.com/fengsp/flask-session) package by [fengsp](https://github.com/fengsp/). The goal is to be a drop in replacement for the original package

Links
`````

* `development version
  <https://github.com/djbeadle/flask-session-2021/zipball/master#egg=Flask-dev>`_

"""
from setuptools import setup


setup(
    name='Flask-Session-2021',
    version='0.4.0',
    url='https://github.com/djbeadle/flask-session-2021',
    license='BSD',
    author='Daniel Beadle',
    author_email='djbeadle@gmail.com',
    description='Adds server-side session support to your Flask application',
    long_description=__doc__,
    packages=['flask_session'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.8',
        'cachelib'
    ],
    test_suite='test_session',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
