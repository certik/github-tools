"""
Helpers for Python package hosting at GitHub.

Copyright (c) 2009, Damien Lebrun
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above COPYRIGHT notice,
      this list of conditions and the following disclaimer.
      
    * Redistributions in binary form must reproduce the above COPYRIGHT notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

PROJECT = 'github-tools'
DESCRIPTION = __doc__.strip().splitlines()[0]
AUTHOR = 'Damien Lebrun'
AUTHOR_EMAIL = 'dinoboff@hotmail.com'
VERSION_TUPLE = (0, 1, 3, '', '')
VERSION = '%s.%s' % VERSION_TUPLE[0:2]
RELEASE = '%s.%s.%s%.1s%s' % VERSION_TUPLE[0:5]

COPYRIGHT = __doc__.strip().splitlines()[2]
LICENCE = 'BSD'
LICENCE_NOTICE = '\n'.join(__doc__.strip().splitlines()[2:])