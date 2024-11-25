openedx-calc
############

|pypi-badge| |ci-badge| |codecov-badge| |doc-badge| |pyversions-badge|
|license-badge| |status-badge|


Purpose
*******

A helper library for mathematical calculations and symbolic mathematics, used by the `edx-platform`_.

This code originally lived in the `edx-platform`_ repo, but now exists here independently.


Getting Started with Development
********************************

General
=======

Please see the Open edX documentation for `guidance on Python development`_ in this repo.

.. _guidance on Python development: https://docs.openedx.org/en/latest/developers/how-tos/get-ready-for-python-dev.html

Instructions
============

Fork and clone the repository, then open a terminal and cd into the repo folder.

Create a virtual environment with one of the python versions specified for the repo. 
Currently those are Python 3.11 and 3.12. Example:

.. code-block:: bash

    python3.11 -m venv ../openedx-calc-venv
    source ../openedx-calc-venv/bin/activate

Install the dependencies:

.. code-block:: bash

    make requirements

Then you can run the tests with just `tox`.

When Upgrading Requirements
---------------------------

Run `make upgrade` to get new versions, and `tox -r` to build the new virtual environment.


Getting Help
************

Documentation
=============

PLACEHOLDER: Start by going through `the documentation`_.  If you need more help see below.

.. _the documentation: https://docs.openedx.org/projects/{{cookiecutter.repo_name}}

(TODO: `Set up documentation <https://openedx.atlassian.net/wiki/spaces/DOC/pages/21627535/Publish+Documentation+on+Read+the+Docs>`_)

More Help
=========

If you're having trouble, we have discussion forums at
https://discuss.openedx.org where you can connect with others in the
community.

Our real-time conversations are on Slack. You can request a `Slack
invitation`_, then join our `community Slack workspace`_.

For anything non-trivial, the best path is to open an issue in this
repository with as many details about the issue you are facing as you
can provide.

https://github.com/openedx/openedx-calc/issues

For more information about these options, see the `Getting Help <https://openedx.org/getting-help>`__ page.

.. _Slack invitation: https://openedx.org/slack
.. _community Slack workspace: https://openedx.slack.com/

License
*******

The code in this repository is licensed under version 3 of the AGPL unless otherwise noted. 
Please see the `LICENSE`_ file for details.

.. _edx-platform: https://github.com/openedx/edx-platform
.. _LICENSE: https://github.com/openedx/openedx-calc/blob/master/LICENSE


Contributing
************

Contributions are very welcome.
Please read `How To Contribute <https://openedx.org/r/how-to-contribute>`_ for details.

This project is currently accepting all types of contributions, bug fixes,
security fixes, maintenance work, or new features.  However, please make sure
to discuss your new feature idea with the maintainers before beginning development
to maximize the chances of your change being accepted.
You can start a conversation by creating a new issue on this repo summarizing
your idea.

Because this repo is used for a wide variety of mathematical calculations,
including learner grades, it may occasionally be desirable to maintain
bug-for-bug compatibility with previous versions. Additions to the repo
are more likely to be accepted than changes that could alter the outputs
of existing functions.


The Open edX Code of Conduct
****************************

All community members are expected to follow the `Open edX Code of Conduct`_.

.. _Open edX Code of Conduct: https://openedx.org/code-of-conduct/

People
******

The assigned maintainers for this component and other project details may be
found in `Backstage`_. Backstage pulls this data from the ``catalog-info.yaml``
file in this repo.

.. _Backstage: https://backstage.openedx.org/catalog/default/component/openedx-calc

Reporting Security Issues
*************************

Please do not report security issues in public. Please email security@openedx.org.

.. |pypi-badge| image:: https://img.shields.io/pypi/v/openedx-calc.svg
    :target: https://pypi.python.org/pypi/openedx-calc/
    :alt: PyPI

.. |ci-badge| image:: https://github.com/openedx/openedx-calc/workflows/Python%20CI/badge.svg?branch=main
    :target: https://github.com/openedx/openedx-calc/actions
    :alt: CI

.. |codecov-badge| image:: https://codecov.io/github/openedx/openedx-calc/coverage.svg?branch=main
    :target: https://codecov.io/github/openedx/openedx-calc?branch=main
    :alt: Codecov

.. |doc-badge| image:: https://readthedocs.org/projects/openedx-calc/badge/?version=latest
    :target: https://docs.openedx.org/projects/openedx-calc
    :alt: Documentation

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/openedx-calc.svg
    :target: https://pypi.python.org/pypi/openedx-calc/
    :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/openedx/openedx-calc.svg
    :target: https://github.com/openedx/openedx-calc/blob/main/LICENSE.txt
    :alt: License

.. TODO: Choose one of the statuses below and remove the other status-badge lines.
.. |status-badge| image:: https://img.shields.io/badge/Status-Experimental-yellow
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Maintained-brightgreen
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Deprecated-orange
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Unsupported-red
