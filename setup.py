from distutils.core import setup
import py2exe

setup(
    console=['kiya/base.py'],
    options = {
        'py2exe' : {
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
