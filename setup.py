import os
from setuptools import setup
from setuptools import find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-geoportal',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        'Django', 
	'FeinCMS', 
	'PIL', 
	'django-admin-tools', 
	'django-filebrowser', 
	'django-grappelli', 
	'django-modeltranslation', 
	'django-mptt', 
	'django-ratings',
	'django-tinymce',
	'easy-thumbnails',
    ],
    license='BSD License', # example license
    description='A simple Django geoportal app.',
    long_description=README,
    url='http://allvbg.ru/',
    author='Lovrjakov Ilja',
    author_email='pman89@ya.ru',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
