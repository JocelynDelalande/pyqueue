#
#    Postfix queue control python tool (pyqueue)
#
#    Copyright (C) 2014 Denis Pompilio (jawa) <denis.pompilio@gmail.com>
#
#    This file is part of pyqueue
#
#    This program is free software; you can redistribute it and/or
#    modify it under the terms of the GNU General Public License
#    as published by the Free Software Foundation; either version 2
#    of the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, see <http://www.gnu.org/licenses/>.

import sys
from functools import wraps
from datetime import datetime


#: Boolean to control activation of the :func:`debug` decorator.
DEBUG = False

def debug(function):
    """
    Decorator to print some call informations and timing debug on stderr.
    
    Function's name, passed args and kwargs are printed to stderr. Elapsed time
    is also print at the end of call. This decorator is based on the value of
    :data:`DEBUG`. If ``True``, the debug informations will be displayed.
    """
    @wraps(function)
    def run(*args, **kwargs):
        name = function.func_name
        if DEBUG is True:
            print >> sys.stderr, "[DEBUG] Running {0}".format(name)
            print >> sys.stderr, "[DEBUG]     args: {0}".format(args)
            print >> sys.stderr, "[DEBUG]   kwargs: {0}".format(kwargs)
            start = datetime.now()

        ret = function(*args, **kwargs)

        if DEBUG is True:
            stop = datetime.now()
            print >> sys.stderr, "[DEBUG] Exectime of {0}: {1} seconds".format(
                    name, (stop - start).total_seconds())

        return ret

    return run

