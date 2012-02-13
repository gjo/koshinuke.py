# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    long_description = f.read()

description = """koshinuke.py is python implementation \
of the server side for KoshiNuke."""

cmdclass = {}

from setup_env import KoshinukeBuild
cmdclass['build_env'] = KoshinukeBuild

setup(
    name='koshinuke.py',
    version='0.1',
    license='Apache License 2.0',
    author='lanius',
    author_email='lanius@nirvake.org',
    description=description,
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-KVSession',
        'GitPython',
    ],
    cmdclass=cmdclass,
    entry_points="""
    [console_scripts]
    kn_add_user = koshinuke.script:add_user
    kn_add_proj = koshinuke.script:add_project
    kn_add_repo = koshinuke.script:add_repository
    """,
)