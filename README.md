Simple paver+distutils project with a few examples.
===================================================

Intro
-----

This project demonstrates basic usage of [Paver](http://paver.github.com/paver/) 
and [distutils](http://docs.python.org/2/distutils/index.html) to help make your 
Python project installable and to support a consistent and maintainable 
develop-build-install (and release!) workflow.

### A quick primer on setup.py

``setup.py`` is the de-facto entry point for installing a package and for 
distributing your package with [PyPi](http://pypi.python.org/pypi).  For 
example, given an initial checkout of this repository, you can install the 
``pkgdemo`` Python package onto your system with the following command:

    $ python setup.py install

But you can also use ``easy_install``:

    $ easy_install .

Or ``pip``:

    $ pip install .

If you are actively developing, but not yet ready to install and you want to 
take advantage of the features provided by the techniques presented here, 
``python setup.py develop`` will create a package in-place and allow continued 
development without having to re-install the package.

Initial setup
-------------

Assuming you've already installed [Paver](http://paver.github.com/paver/), you 
can use the ``paver`` command to initialize your project:

    $ paver generate_setup
    ---> paver.misctasks.generate_setup
    Write setup.py
    $ paver minilib
    ---> paver.misctasks.minilib
    Generate paver-minilib.zip

Your ``setup()`` will go in ``pavement.py``.  For example:

    from paver.setuputils import setup

    setup(
        name = "pkgdemo",
        packages = ["pkgdemo"],
        version = "1.0",
        author = "Austin Marshall",
        package_data =
            {
                "pkgdemo": [
                    "assets/*.txt", 
                    "assets/css/*.css",
                    "assets/js/*.js"
                ]
            },
        zip_safe = False
    )

- ``packages`` defines the list of packages to be included in your 
distribution.  Remember, these must be proper python packages (i.e., there must
be a ``__init__.py`` file present).  By default, all python modules will be 
included.
- ``package_data`` explicitly defines additional non-python data files to be 
included in your distribution by way of a dict mapping directories to lists of 
files using glob syntax.  Alternatively, you can leave ``package_data`` out 
altogether, and instead have ``include_package_data = True`` to automatically 
identify and bundle all files.  The resulting ``setup()`` would be:

        setup(
            name = "pkgdemo",
            packages = ["pkgdemo"],
            version = "1.0",
            author = "Austin Marshall",
            include_package_data = True,
            zip_safe = False
        )

- ``distutils`` will attempt to automatically determine whether the target egg 
can be distributed as a compressed zip file, or as a directory.  By specifying 
``zip_safe = False``, you force it to use a directory, so that your non-python 
data files can be accessed.

Build your package
------------------
    
    $ python setup.py build
    running build
    running build_py
    creating build
    creating build/lib.linux-x86_64-2.6
    creating build/lib.linux-x86_64-2.6/pkgdemo
    copying pkgdemo/__init__.py -> build/lib.linux-x86_64-2.6/pkgdemo
    creating build/lib.linux-x86_64-2.6/pkgdemo/assets
    copying pkgdemo/assets/README.txt -> build/lib.linux-x86_64-2.6/pkgdemo/assets
    creating build/lib.linux-x86_64-2.6/pkgdemo/assets/css
    copying pkgdemo/assets/css/style.css -> build/lib.linux-x86_64-2.6/pkgdemo/assets/css
    creating build/lib.linux-x86_64-2.6/pkgdemo/assets/js
    copying pkgdemo/assets/js/lib.js -> build/lib.linux-x86_64-2.6/pkgdemo/assets/js

Inspect the build tree to confirm:
    
    $ tree build
    build
    └── lib.linux-x86_64-2.6
        └── pkgdemo
            ├── assets
            │   ├── css
            │   │   └── style.css
            │   ├── js
            │   │   └── lib.js
            │   └── README.txt
            └── __init__.py

    5 directories, 4 files

Install your package.
---------------------

It should look something like the following, but with paths specific to your 
environment:

    $ python setup.py install
    running install
    running build
    running build_py
    running install_lib
    creating /home/ubuntu/testpkgdemo/lib/python2.6/site-packages/pkgdemo
    creating /home/ubuntu/testpkgdemo/lib/python2.6/site-packages/pkgdemo/assets
    copying build/lib.linux-x86_64-2.6/pkgdemo/assets/README.txt -> /home/ubuntu/testpkgdemo/lib/python2.6/site-packages/pkgdemo/assets
    creating /home/ubuntu/testpkgdemo/lib/python2.6/site-packages/pkgdemo/assets/js
    copying build/lib.linux-x86_64-2.6/pkgdemo/assets/js/lib.js -> /home/ubuntu/testpkgdemo/lib/python2.6/site-packages/pkgdemo/assets/js
    creating /home/ubuntu/testpkgdemo/lib/python2.6/site-packages/pkgdemo/assets/css
    copying build/lib.linux-x86_64-2.6/pkgdemo/assets/css/style.css -> /home/ubuntu/testpkgdemo/lib/python2.6/site-packages/pkgdemo/assets/css
    copying build/lib.linux-x86_64-2.6/pkgdemo/__init__.py -> /home/ubuntu/testpkgdemo/lib/python2.6/site-packages/pkgdemo
    byte-compiling /home/ubuntu/testpkgdemo/lib/python2.6/site-packages/pkgdemo/__init__.py to __init__.pyc
    running install_egg_info
    running egg_info
    writing pkgdemo.egg-info/PKG-INFO
    writing top-level names to pkgdemo.egg-info/top_level.txt
    writing dependency_links to pkgdemo.egg-info/dependency_links.txt
    reading manifest file 'pkgdemo.egg-info/SOURCES.txt'
    writing manifest file 'pkgdemo.egg-info/SOURCES.txt'
    Copying pkgdemo.egg-info to /home/ubuntu/testpkgdemo/lib/python2.6/site-packages/pkgdemo-1.0-py2.6.egg-info
    running install_scripts

Confirm
-------

Start Python, import your package and inspect the docstring.
    
    $ python
    Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41) 
    [GCC 4.4.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pkgdemo
    >>> pkgdemo.__doc__

pkg_resources
-------------

Because you're using paver+distutils to manage your distribution, you can use 
``pkg_resources`` to provide access to the resources you've just bundled in 
your distribution.  Take [pkgdemo/__init__.py](pkgdemo/tree/master/pkgdemo/__init__.py) for example:

    from pkg_resources import resource_string

    __doc__ = resource_string(__name__, "assets/README.txt")

The ``pkgdemo`` docstring is set to the contents of ``assets/README.txt``.  You 
do not need to calculate absolute or relative paths and instead can rely on the 
helper functions in [pkg_resources](http://peak.telecommunity.com/DevCenter/PkgResources).

Entry Points (console scripts)
------------------------------

``entry_points`` provides a convenient mechanism for defining console scripts.  

Consider the following snippet:

    setup(
        ...
        entry_points = 
            {
                "console_scripts": [
                    "pkgdemo = pkgdemo.actions:main",
                    "pkgdemo-foo = pkgdemo.actions:foo"
                ]
            }
        ...
    )

Here you define two commands: ``pkgdemo`` and ``pkgdemo-foo``.  The definitions 
for which can be found in the actions module of the pkgdemo package ([pkgdemo/actions.py](pkgdemo/tree/master/pkgdemo/actions.py)).

Following an installation, the ``main()`` and ``foo()`` functions defined in 
[pkgdemo/actions.py](pkgdemo/tree/master/pkgdemo/actions.py) can be executed by 
invoking the ``pkgdemo`` and ``pkgdemo-foo`` commands respectively:

    $ pkgdemo
    pkgdemo.actions None {'foo': None}

    $ pkgdemo-foo --bar Bar baz
    pkgdemo.actions:foo( baz ):  {'bar': 'Bar'}

The scripts are automatically generated and placed in the bin directory 
relative to the package.

    $ which pkgdemo
    /Path/to/pkgdemo/bin/pkgdemo

The contents should look something like:

    #!/Path/to/python
    # EASY-INSTALL-ENTRY-SCRIPT: 'pkgdemo==1.0','console_scripts','pkgdemo'
    __requires__ = 'pkgdemo==1.0'
    import sys
    from pkg_resources import load_entry_point

    sys.exit(
       load_entry_point('pkgdemo==1.0', 'console_scripts', 'pkgdemo')()
    )

The generated scripts need not be checked into revision control or maintained 
seperately as they are generated and made available at time of installation.