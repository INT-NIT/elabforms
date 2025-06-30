Installation
============

Create a virtual environment:

.. code-block:: bash

   python3 -m venv myenv
   source myenv/bin/activate

---

You will need `template_part` files to generate the final template.
These files are located in the `elabforms_INTProjects` and `elabforms_BIDSMetadata` repositories — private Git repositories at NIT.

**Reminder:**

A `template_part` is an elabform with a single `groupfield`.
You need to create a `template_file_list.csv` file listing the parts you want to concatenate, **in this order**, for example:

.. code-block:: text

   template_part_Example_1.json
   template_part_Example_2.json
   ...
   template_part_Example_N.json

Each line corresponds to one template part file.
