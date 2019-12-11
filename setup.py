from setuptools import setup, find_packages
from os import path
from io import open


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requires = [req.strip() for req in f if req]


setup(
    name='falibrary',
    version='0.5.3',
    author='Keming Yang',
    author_email='kemingy94@gmail.com',
    description='',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/kemingy/falibrary',
    packages=find_packages(exclude=['examples*', 'tests*']),
    package_data={
        'falibrary': ['templates/*.html'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    install_requires=requires,
    zip_safe=False,
    extras_require={},
    entry_points={
        'console_scripts': [],
    },
)
