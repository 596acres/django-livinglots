from setuptools import setup, find_packages
import os

import livinglots


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
]

setup(
    author='Eric Brelsford',
    author_email='eric@596acres.org',
    name='django-livinglots',
    version=livinglots.__version__,
    description=('The parent app for Living Lots, a suite of apps by 596 '
                 'Acres for mapping and connecting people to the vacant land '
                 'in their neighborhoods.'),
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/596acres/django-livinglots/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.5.1',
    ],
    packages=find_packages(),
    include_package_data=True,
)
