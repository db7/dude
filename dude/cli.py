#!/usr/bin/env python
# -*- mode: python -*-
"""
    Dude - framework for experiments
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright (c) 2010,2011 Diogo Becker
    :license: MIT, see LICENSE for details.
"""

import sys

def main():
    import dude
    sys.exit(dude.cmdline.main(sys.argv[1:]))

if __name__ == '__main__':
    main()
