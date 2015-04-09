from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='cmsplugin-bootstrap',
    version='0.1',
    packages=find_packages(),
    url='http://github.com/arkanister/cmsplugin-bootstrap',
    license='BSD',
    author='Arkanister',
    author_email='arkanister.dev@gmail.com',
    description='Bootstrap plugins to DjangoCMS',
    keywords='bootstrap django cms django-cms',
    long_description=README,
    install_requires=[
        "Django >= 1.7",
        "django-cms >= 3.0",
        "cmsplugin-filer",
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False
)
