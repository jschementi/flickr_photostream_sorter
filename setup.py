import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='flickr_photostream_sorter',
    version='0.1',
    packages=['flickr_photostream_sorter'],
    install_requires=[
        "flickrapi==1.4.4"
    ],
    entry_points={
        'console_scripts': [
            'flickr_photostream_sorter = flickr_photostream_sorter:main',
        ]
    },
    author='Jimmy Schementi',
    author_email='jimmy@schementi.com',
    url='https://github.com/jschementi/flickr_photostream_sorter',
    description='Sort your Flickr photostream by changing each photo\'s posted date to when it was taken.',
    long_description=README,
    keywords='flickr photostream sort',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ]
)
