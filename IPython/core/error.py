# encoding: utf-8
"""
Global exception classes for IPython.core.

Authors:

* Brian Granger
* Fernando Perez
* Min Ragan-Kelley

Notes
-----
"""

#-----------------------------------------------------------------------------
#  Copyright (C) 2008-2011  The IPython Development Team
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Exception classes
#-----------------------------------------------------------------------------

class IPythonCoreError(Exception):
    pass


class TryNext(IPythonCoreError):
    """Try next hook exception.

    Raise this in your hook function to indicate that the next hook handler
    should be used to handle the operation.  If you pass arguments to the
    constructor those arguments will be used by the next hook instead of the
    original ones.
    
    A _msg argument will not be passed on, so it can be used as a displayable
    error message.
    """

    def __init__(self, _msg="", *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.msg = _msg
    
    def __str__(self):
        return str(self.msg)

class UsageError(IPythonCoreError):
    """Error in magic function arguments, etc.

    Something that probably won't warrant a full traceback, but should
    nevertheless interrupt a macro / batch file.
    """

class StdinNotImplementedError(IPythonCoreError, NotImplementedError):
    """raw_input was requested in a context where it is not supported

    For use in IPython kernels, where only some frontends may support
    stdin requests.
    """
