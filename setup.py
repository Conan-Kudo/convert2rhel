#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# Copyright(C) 2016 Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from setuptools import setup, find_packages

from man.build_manpage import build_manpage


# Utility function to read content of a file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='convert2rhel',
    version='0.9',
    description='Automates the conversion of the installed other-than-RHEL'
                ' distribution to Red Hat Enterprise Linux (RHEL)',
    long_description=read('README'),
    author='Michal Bocek',
    author_email='mbocek@redhat.com',
    url='www.redhat.com',
    license='GNU General Public License v3 (GPLv3)',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'convert2rhel = convert2rhel.main:main',
        ]
    },
    cmdclass={'build_manpage': build_manpage},
    include_package_data=True
)
