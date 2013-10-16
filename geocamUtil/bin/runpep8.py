#!/usr/bin/env python
# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

import sys
import os
import re

from geocamUtil.management.commandUtil import getSiteDir

STRIP_COMMENT = re.compile(r'#.*$')
CONFIG_FILE = os.path.join(getSiteDir(), 'management', 'pep8Flags.txt')
DEFAULT_FLAGS = '--ignore=E501 --show-source --show-pep8 --repeat'


def dosys(cmd, verbosity):
    if verbosity > 1:
        print 'running: %s' % cmd
    ret = os.system(cmd)
    if verbosity > 1:
        if ret != 0:
            print 'warning: command exited with non-zero return value %d' % ret
    return ret


def readFlags(path):
    f = file(path, 'r')
    flags = []
    for line in f:
        line = re.sub(STRIP_COMMENT, '', line)
        line = line.strip()
        if line:
            flags.append(line)
    return ' '.join(flags)


def runpep8(paths, verbosity=1):
    if verbosity > 0:
        print '### pep8'

    if not paths:
        paths = ['.']

    # give helpful error message if pep8 is not installed
    ret = os.system('pep8 --help > /dev/null')
    if ret != 0:
        print >> sys.stderr, "\nWARNING: can't run pep8 command -- try 'pip install pep8'\n"
        sys.exit(1)

    # extract flags from <site>/management/pep8Flags.txt if it exists
    if verbosity > 1:
        print 'checking for pep8 flags in %s' % CONFIG_FILE
    if os.path.exists(CONFIG_FILE):
        flags = readFlags(CONFIG_FILE)
    else:
        flags = DEFAULT_FLAGS

    for d in paths:
        d = os.path.relpath(d)
        cmd = 'pep8 %s' % flags
        if verbosity > 2:
            xargsFlags = '--verbose'
        else:
            xargsFlags = ''
        if os.path.isdir(d):
            dosys('find %s -name "*.py" | egrep -v "external|attic" | xargs %s -n50 -d"\n" %s' % (d, xargsFlags, cmd), verbosity)
        else:
            dosys('%s %s' % (cmd, d), verbosity)


def main():
    import optparse
    parser = optparse.OptionParser('usage: %prog [dir1] [file2.py] ...')
    parser.add_option('-v', '--verbosity',
                      type='int',
                      default=1,
                      help='Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output')
    opts, args = parser.parse_args()
    runpep8(args, verbosity=opts.verbosity)

if __name__ == '__main__':
    main()
