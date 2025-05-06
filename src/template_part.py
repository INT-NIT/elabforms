# File: src/template_part.py
from template import Template


class TemplatePart(Template):
    """
    Class to manage a template part for ElabFTW.
    Inherits from the Template class.
    """

    @staticmethod
    def check_structure(template_file_content):
        """
        Validates the structure of a template part.

        Parameters:
            template_file_content (dict): JSON content of the file.

        Raises:
            ValueError: If the structure is invalid.
        """
        # Call the base validation from the Template class
        super(TemplatePart, TemplatePart).check_structure(template_file_content)

        # Ensure there is only one groupfield
        if len(template_file_content['elabftw']['extra_fields_groups']) > 1:
            raise ValueError("The 'extra_fields_groups' list must contain only"
                             "one groupfield for a template part.")