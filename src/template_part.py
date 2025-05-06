import json


class TemplatePart:
    """
    Class to manage a template part for ElabFTW.
    """

    def __init__(self, template_part_file):
        """
        Initializes the TemplatePart object.

        Parameters:
            template_part_file (str): Path to the JSON file.
        """
        self.template_part_file = template_part_file
        self.template_part = self.read_template_part(template_part_file)

    @staticmethod
    def read_template_part(template_parts_file):
        """
        Reads a JSON template part file and validates its structure.

        Parameters:
            template_parts_file (str): Path to the JSON file.

        Returns:
            dict: Content of the JSON file.

        Raises:
            ValueError: If the structure is invalid.
        """
        try:
            with open(template_parts_file, 'r') as f:
                template_parts_content = json.load(f)
                TemplatePart.check_structure(template_parts_content)
                return template_parts_content
        except KeyError as e:
            raise ValueError(f"Invalid template file: missing key {e}")

    @staticmethod
    def check_structure(template_parts_file_content):
        """
        Validates the structure of a template part.

        Parameters:
            template_parts_file_content (dict): JSON content of the file.

        Raises:
            ValueError: If the structure is invalid.
        """
        required_keys = ['elabftw', 'extra_fields']
        for key in required_keys:
            if key not in template_parts_file_content:
                raise ValueError(f"Invalid template file: missing key {key}")

        if 'extra_fields_groups' not in template_parts_file_content['elabftw']:
            raise ValueError("Invalid template file: missing "
                             "'extra_fields_groups' key")
        if not isinstance(
                template_parts_file_content['elabftw']['extra_fields_groups'],
                list):
            raise ValueError("'extra_fields_groups' must be a list")
        if not template_parts_file_content['elabftw']['extra_fields_groups']:
            raise ValueError("The 'extra_fields_groups' list is empty")
        if not all(isinstance(group, dict) for group in
                   template_parts_file_content['elabftw'][
                       'extra_fields_groups']):
            raise ValueError("'extra_fields_groups' must contain dictionaries")
        if not all('id' in group for group in
                   template_parts_file_content['elabftw'][
                       'extra_fields_groups']):
            raise ValueError("'extra_fields_groups' dictionaries must have an "
                             "'id' key")
        # check if the extrat_fields_groups have a single group
        if (len(template_parts_file_content['elabftw']['extra_fields_groups'])
                > 1):
            raise ValueError("The 'extra_fields_groups' list must contain a "
                             "single group a template part is expected to "
                             "have a single groupfield")
