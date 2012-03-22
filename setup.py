import sys, os
try:
    from setuptools import setup
except:
    from distutils.core import setup

if sys.version_info < (2,5):
    raise NotImplementedError("Sorry, you need at least Python 2.6 or Python 3.x to use simpledict.")
    
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
        
setup(
    name='webapp2_static',
    version='0.1',
    description='Simple handler to Serve static files on non Google App Engine (GAE) webapp2 environments',
    author='Robert Spychala',
    author_email="robspychala@gmail.com",
    url="http://github.com/robspychala/webapp2_static",
    keywords=["webapp2"],
    platforms=['any'],
    py_modules=['webapp2_static'],
    scripts=['webapp2_static.py'],
    license='MIT',
    classifiers=[
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            "Development Status :: 3 - Alpha",
            "Topic :: Database :: Database Engines/Servers",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
            ],
    long_description=read('Readme.md'),
    test_suite="tests"
)

# python setup.py register sdist upload