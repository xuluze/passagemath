# -*- coding: utf-8 -*-
"""
Package Creator
"""

# ****************************************************************************
#       Copyright (C) 2015-2016 Volker Braun <vbraun.name@gmail.com>
#                     2020-2024 Matthias Koeppe
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#                  https://www.gnu.org/licenses/
# ****************************************************************************

import os

import logging
log = logging.getLogger()

from sage_bootstrap.env import SAGE_ROOT


class PackageCreator(object):

    def __init__(self, package_name):
        self.package_name = package_name
        self.path = os.path.join(SAGE_ROOT, 'build', 'pkgs', package_name)
        try:
            os.mkdir(self.path)
        except OSError:
            pass

    def set_version(self, version):
        """
        Write the version to ``package-version.txt``
        """
        with open(os.path.join(self.path, 'package-version.txt'), 'w+') as f:
            f.write(version)
            f.write('\n')

    def set_type(self, pkg_type):
        """
        Write the package type to ``type``
        """
        with open(os.path.join(self.path, 'type'), 'w+') as f:
            f.write(pkg_type)
            f.write('\n')

    def set_tarball(self, tarball, upstream_url):
        """
        Write the tarball name pattern to ``checksums.ini``
        """
        with open(os.path.join(self.path, 'checksums.ini'), 'w+') as f:
            f.write('tarball={0}'.format(tarball))
            f.write('\n')
            if upstream_url:
                f.write('upstream_url={0}'.format(upstream_url))
            f.write('\n')

    def set_pypi_urls(self, pypi_version):
        """
        Write the ``checksums.ini`` file
        """
        with open(os.path.join(self.path, 'checksums.ini'), 'w+') as f:
            for url in pypi_version.urls:
                if 'cp' in url['python_version'] or 'py3' in url['python_version']:
                    f.write('[{0}]\n'.format(url['filename']))
                    f.write('tarball={0}\n'.format(url['filename']))
                    f.write('sha256={0}\n'.format(url['digests']['sha256']))
                    f.write('upstream_url={0}\n'.format(url['url']))
                    f.write('\n')

    def set_description(self, description, license, upstream_contact):
        """
        Write the ``SPKG.rst`` file
        """
        with open(os.path.join(self.path, 'SPKG.rst'), 'w+') as f:
            # Attempt to bring title to a common style
            if description.startswith(self.package_name + ':'):
                description = description[len(self.package_name + ':'):]
            if description.startswith(self.package_name + ' is'):
                description = description[len(self.package_name + ' is'):]
            description = description.strip()
            if not description.endswith('etc.'):
                description = description.rstrip('.')
            if description.startswith('A ') or description.startswith('a '):
                description = description[2:].strip()
            if description.startswith('An ') or description.startswith('an '):
                description = description[3:].strip()
            if description:
                description = description[0].upper() + description[1:]

            def heading(title, char='-'):
                return '{0}\n{1}\n\n'.format(title, char * len(title))
            if description:
                title = '{0}: {1}'.format(self.package_name, description)
            else:
                title = self.package_name
            f.write(heading(title, '='))
            f.write(heading('Description'))
            if description:
                f.write('{0}\n\n'.format(description))
            f.write(heading('License'))
            if license:
                f.write('{0}\n\n'.format(license))
            f.write(heading('Upstream Contact'))
            if upstream_contact:
                f.write('{0}\n\n'.format(upstream_contact))

    def _remove_files(self, files):
        """
        Remove ``files`` from the package directory if they exist.
        """
        for file in files:
            try:
                os.remove(os.path.join(self.path, file))
            except OSError:
                pass

    def set_python_data_and_scripts(self, pypi_package_name=None, source='normal', dependencies=None):
        """
        Write the files ``dependencies``, ``dependencies_build``, and other files for Python packages.

        If ``source`` is ``"normal"``, write the files ``spkg-install.in`` and
        ``version_requirements.txt``.

        If ``source`` is ``"wheel"``, write the file ``version_requirements.txt``.

        If ``source`` is ``"pip"``, write the file ``requirements.txt``.

        Remove existing files that belong to other source types.
        """
        if pypi_package_name is None:
            pypi_package_name = self.package_name
        with open(os.path.join(self.path, 'dependencies_build'), 'w+') as f:
            if source == 'wheel':
                f.write(' | pip $(PYTHON)\n\n')
            else:
                f.write(' | $(PYTHON_TOOLCHAIN) $(PYTHON)\n\n')
            f.write('----------\nAll lines of this file are ignored except the first.\n')
        with open(os.path.join(self.path, 'dependencies'), 'w+') as f:
            f.write('# No dependencies\n\n')
            f.write('----------\nAll lines of this file are ignored except the first.\n')
        if source == 'normal':
            with open(os.path.join(self.path, 'spkg-install.in'), 'w+') as f:
                f.write('cd src\nsdh_pip_install .\n')
            with open(os.path.join(self.path, 'version_requirements.txt'), 'w+') as f:
                f.write('{0}\n'.format(pypi_package_name))
            # Remove this file, which would mark the package as a pip package.
            self._remove_files(['requirements.txt'])
        elif source == 'wheel':
            with open(os.path.join(self.path, 'version_requirements.txt'), 'w+') as f:
                f.write('{0}\n'.format(pypi_package_name))
            # Remove this file, which would mark the package as a pip package.
            self._remove_files(['requirements.txt'])
            if pypi_package_name != 'pip':
                # 'pip' should be the only wheel package that has a custom spkg-install.in script.
                # Remove the script for all other wheel packages, to avoid errors when
                # switching from normal to wheel packages.
                self._remove_files(['spkg-build.in', 'spkg-install.in', 'spkg-install'])
        elif source == 'pip':
            with open(os.path.join(self.path, 'requirements.txt'), 'w+') as f:
                f.write('{0}\n'.format(pypi_package_name))
            self._remove_files(['checksums.ini', 'spkg-build.in', 'spkg-install.in', 'spkg-install', 'install-requires.txt'])
        elif source == 'script':
            self._remove_files(['checksums.ini', 'requirements.txt'])
        else:
            raise ValueError('package source must be one of normal, script, pip, or wheel')
