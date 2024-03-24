import os
import re

from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.
    Returns a list of requirement strings.
    """
    requirements = set()
    for path in requirements_paths:
        with open(path) as reqs:
            requirements.update(
                line.split('#')[0].strip() for line in reqs
                if is_requirement(line.strip())
            )
    return list(requirements)


def is_requirement(line):
    """
    Return True if the requirement line is a package requirement;
    that is, it is not blank, a comment, a URL, or an included file.
    """
    return line and not line.startswith(('-r', '#', '-e', 'git+', '-c'))


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    with open(filename, encoding='utf-8') as opened_file:
        version_file = opened_file.read()
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


VERSION = get_version("calc", "__init__.py")


setup(
    name="openedx-calc",
    # Note: cannot easily move version to calc/__init__.py because it imports all
    #   of calc, which causes failure here when requirements have not yet been loaded.
    version=VERSION,
    description=('A helper library for mathematical calculations and symbolic '
                 'mathematics, used by Open edX.'),
    long_description=README,
    long_description_content_type="text/x-rst",
    author='edX',
    author_email='oscm@edx.org',
    url='https://github.com/openedx/openedx-calc',
    packages=[
        'calc',
        "symmath"
    ],
    include_package_data=True,
    install_requires=load_requirements('requirements/base.in'),
    python_requires=">=3.8",
    license="AGPL 3.0",
    test_suite='tests',
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
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.11',
    ],
)
