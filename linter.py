#
# sqlint.py
# SQL Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Steve Purcell & Kieran Trezona-le Comte
# Copyright (c) 2015 Powershop NZ Ltd
#
# License: MIT
#

"""This module exports the Sqlint plugin class."""

from SublimeLinter.lint import Linter, util


class Sqlint(Linter):

    """Provides an interface to sqlint."""

    cmd = 'sqlint'
    defaults = {'selector': 'source.sql'}
    tempfile_suffix = 'sql'

    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.0.5'

    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+):'
        r'(?:(?P<error>ERROR)|(?P<warning>WARNING)) '
        r'(?P<message>.+$(?:\r?\n  .+$)*)'
    )

    multiline = True
    line_col_base = (1, 1)
    error_stream = util.STREAM_STDOUT
