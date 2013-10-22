#!/usr/bin/python

"""
#----------------------------------------------------------------
Author: Jason Gors <jasonDOTgorsATgmail>
Creation Date: 10-22-2013
Purpose:
#----------------------------------------------------------------
"""

from distutils.core import setup

setup_args = dict(
    name="pip_updater",
    version="1.0", 
    description="To update all pip pkgs installed locally.",
    author="Jason Gors",
    author_email="jasonDOTgorsATgmailDOTcom",
    url="https://github.com/jgors/pip_updater",
    license="MIT",
)

setup_args['scripts'] = ['pip_updater']


def main():
    setup(**setup_args)

if __name__ == '__main__':
    main()
