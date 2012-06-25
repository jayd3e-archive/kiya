from distutils.core import setup
import py2exe

requires = []

setup(
    name='kiya',
    version='0.1',
    packages=['kiya'],
    requires=requires,
    console=['kiya/base.py'],
    options={
        'py2exe': {
          'packages': [],
          'includes': ['cairo',
                       'pygtk',
                       'gio',
                       'pango',
                       'pangocairo',
                       'atk',
                       'gobject']
        },
        'sdist': {
            'formats': 'zip'
        }
    }
)
