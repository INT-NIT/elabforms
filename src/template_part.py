from template import Template


class TemplatePart(Template):
    """
    Class to manage a template part for ElabFTW.
    Inherits from the Template class.
    """
    def __init__(self, template_file):
        """
        Initializes the TemplatePart object.

        Parameters:
            template_file (str): Path to the JSON file.
        """
        super().__init__(template_file)
        # Call the structure validation for the template content
        self.check_structure(self.template_content)

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
        Template.check_structure(template_file_content)

        # Ensure there is only one groupfield
        if len(template_file_content['elabftw']['extra_fields_groups']) > 1:
            raise ValueError("The 'extra_fields_groups' list must contain only"
                             "one groupfield for a template part.")