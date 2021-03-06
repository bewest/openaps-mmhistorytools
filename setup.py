from setuptools import setup, find_packages

long_description ='''openaps MMHistoryTools plugin
==============================
This package is a vendor plugin for openaps that provides tools for cleaning, condensing, and
reformatting history data.
'''

requires = ['openaps', 'python-dateutil']

setup(
    name='openapscontrib.mmhistorytools',
    version='0.0.0',
    url='http://github.com/loudate/openaps-mmhistorytools',
    license='MIT',
    author='Nathan Racklyeft',
    author_email='loudnate+pypi@gmail.com',
    description='openaps mmhistorytools plugin',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Documentation',
        'Topic :: Utilities',
        ],
    platforms='any',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['openapscontrib'],
)
