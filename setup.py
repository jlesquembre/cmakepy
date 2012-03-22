# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
setup(
    name = "CmakePy",
    version = "0.1.1",
    packages = find_packages(),
    #scripts = ['cmake.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['Jinja2>=2.6', 'distribute'],

    
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        #'': ['*.txt', '*.cpp'],
        'cmakepy.templates': ['*.txt', '*.cpp'],
        # And include any *.msg files found in the 'hello' package, too:
        #'templates': ['*.txt','*.cpp'],
    },
    
    entry_points = {
        'console_scripts': [
            'cmake.py = cmakepy.cmakepy:main',
        ]
    },
    
    
    #include_package_data = True,

    # metadata for upload to PyPI
    author = "Jose Luis Lafuente",
    author_email = "joseluis@japeto.com",
    description = "Creates a new cmake project",
    license = "GPLv3",
    keywords = "cmake c++",
    url = "https://github.com/jlesquembre/cmakepy",   
    
    # could also include long_description, download_url, classifiers, etc.
) 
