Github features Git repository hosting, a download page for your Git tags 
(or any archive), a basic issue tracker, a wiki and static page hosting 
(`gh-pages <http://pages.github.com/>`_). It would be perfect for hosting a 
Python package and its documentation if gh-pages was easy to setup and 
was compatible with `Sphinx <http://sphinx.pocoo.org>`_. 

Setting up a root branch for gh-pages is quite complex; Sphinx put its
source and static files in directories named "_static" and "_source"
that gh-pages doesn't want to serve them.

The Sphinx extension (``github.tools.sphinx``) corrects the last problem; 
some paver tasks (``github.tools.task.*``) take care of the creation of a Git 
submodule to host the built html documentation; The PasteScript template 
create the basic layout and pavement.py script to get started.

Requirements
============

This extension and its dependencies require:

 * a GitHub user account and,
 * Git (tested with 1.6.2.4), 
 * Python 2.5+.
 
It currently has only been tested on Ubuntu 8.04 (and Git built from source)
with Python 2.5.

It should work on os X. For Windows, It should work as long as 
`GitPython <http://pypi.python.org/pypi/GitPython/>`_ does. However since it 
simply  start ``git`` subprocesses to work, it might be difficult to use with
Git installer like `msysgit <http://code.google.com/p/msysgit/>`_ or 
`gitextensions <http://code.google.com/p/gitextensions/>`_. 



Installation
============

The easiest way to get github-tools is if you have setuptools installed::

	easy_install github-tools

Without setuptools, download it from 
`Pypi <http://pypi.python.org/pypi/github-tools/>`_ or from 
`Github <http://github.com/dinoboff/github-tools/downloads>`_, untar it
and run::

	python setup.py install

The current development version can be found at 
http://github.com/dinoboff/github-tools/tarball/master.


Usage
=====

Package layout
--------------

If you are starting from scratch, create the basic layout with paster::

	paster create -t gh_package <project name>
	
The project name will be used for pypi and for your Github repository
(``http://github.com/<user>/<project name>``). The project details are saved in
``src/<package name>/__init__.py``.

To finish your development environment setup, create a virtual environment
and deploy your package in development mode::

	cd <project name>
	python bootstrap.py --no-site-packages
	
The basic package comes with a virtualenv boostrap script
to create an  isolated Python environments. To activate this environment
in your shell, run::

	source ./virtual-env/bin/activate
	# or .\virtual-env\Scripts\activate.bat on windows

Finally::

	paver generate_setup minilib develop.

Paver add a ``setup.py`` file to your package and a portable paver library
(required by ``setup.py``), and deploy your application in development mode;
The "src" folder which contains your package is added to the Python path.

You are ready to write your package (in ``src/``) and its documentation
(in ``docs/source``). You should probably start tracking your project now::

	git init
	git add .
	git commit -m "initial import"  


Github project creation
-----------------------

When you are ready to share your work, you will need to 
create a repository at GitHub and push your local repository. Paver can do it 
for you. Paver will need your GitHub user name and token to create 
the repository. You can set them with the following command::

	git config --global github.user <user>
	git config --global github.token <token>
	
You can find your token on your 
`Github account page <https://github.com/account>`_.

Then, to create the repository and upload your project::

	paver gh_register
	

Documentation hosting
---------------------
	
Once the project is created, you can create your gh-pages branch 
and upload it to GitHub::

	paver gh_pages_create gh_pages_build
	
Paver will create a submodule of your project at ``docs/build/html``,
create a gh-pages root branch and push the branch to your project.
It then build the html doc. To clean the html build folder, it update 
the submodule (you will lose changes not committed and pushed), 
remove every files and directory (except ``.git/``) 
and rebuild the documentation.

When your documentation can be published, simply push your gh-pages submodule 
to GitHub::

	paver gh_pages_build gh_pages_update -m "update docs with..."
	
Your documentation should be available 
at ``http://<user name>.github.com/<project name>``.

You might also want to update the submodule reference (a submodule point 
to specific commit on a remote repository, not to the HEAD 
of a specific branch)::

	git add docs/build/html
	git commit -m "update gh-pages submodule"
	
Help and Development
====================

If you'd like to help out, you can fork the project
at http://github.com/dinoboff/github-tools/ and report any bugs 
at http://github.com/dinoboff/github-tools/issues.
