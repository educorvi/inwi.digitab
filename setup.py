# -*- coding: utf-8 -*-
"""Installer for the inwi.digitab package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='inwi.digitab',
    version='1.0a1',
    description="Plone-Add-On zur Konfiguration von Verarbeitungsregeln mit den Werkzeugen des CMS",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Lars Walther',
    author_email='meinkraeks@gmail.com',
    url='https://pypi.python.org/pypi/inwi.digitab',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['inwi'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8, >=3.9, >=3.10",
    install_requires=[
        # -*- Extra requirements: -*-
        'plone.api>=1.8.4',
        'Products.GenericSetup>=1.8.2',
        'setuptools',
        'z3c.jbot',
        'plone.behavior',
        'collective.z3cform.datagridfield',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
