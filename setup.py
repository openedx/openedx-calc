import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


setup(
    name="openedx-calc",
    # Note: cannot easily move version to calc/__init__.py because it imports all
    #   of calc, which causes failure here when requirements have not yet been loaded.
    version='1.0.5',
    description='A helper library for mathematical calculations, used by Open edX.',
    long_description=README,
    long_description_content_type="text/x-rst",
    author='edX',
    author_email='oscm@edx.org',
    url='https://github.com/edx/openedx-calc',
    packages=[
        'calc'
    ],
    include_package_data=True,
    install_requires=[
        "pyparsing==2.2.0",
        "numpy",
        "scipy",
        'six',
    ],
    python_requires=">=3.5",
    license="AGPL 3.0",
    test_suite='calc.tests',
    tests_require=[
        'coverage',
    ],
    zip_safe=False,
    keywords='edx',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
