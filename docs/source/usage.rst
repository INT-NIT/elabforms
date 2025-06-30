Usage
=====



Install the package from Test PyPI:

.. code-block:: bash

   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple elabforms==0.0.6

### Usage

Test the installation by running:

.. code-block:: bash

   eform --help

To create a new form, run:

.. code-block:: bash

   eform template_file_list.csv template_generated.json
