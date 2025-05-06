import os
import csv
import json
from template_part import TemplatePart
from template import Template


class TemplateBuilder:
    """
    Class to generate a complete template from multiple parts.
    """

    @staticmethod
    def read_template_parts_list(template_parts_list_file):
        """
        Reads a list of template part files from a CSV file.

        Parameters:
            template_parts_list_file (str): Path to the CSV file.

        Returns:
            list: List of JSON file paths.

        Raises:
            ValueError: If the file extension is not supported.
            FileNotFoundError: If a file is not found.
        """
        if not template_parts_list_file.endswith('.csv'):
            raise ValueError(
                f"Unsupported file extension: {template_parts_list_file}")

        with open(template_parts_list_file, 'r') as f:
            reader = csv.reader(f)
            template_parts_list = [row[0] for row in reader if row]

        for template_part in template_parts_list:
            if not os.path.exists(template_part):
                raise FileNotFoundError(f"File not found: {template_part}")
            if not template_part.endswith('.json'):
                raise ValueError(
                    f"The file must be in JSON format: {template_part}")

        return template_parts_list

    @staticmethod
    def set_content_id(new_id, template_parts_file_content):
        """
        Updates the IDs of the contents in a template part.

        Parameters:
            new_id (int): New ID to assign.
            template_parts_file_content (dict): Content of the template part.

        Returns:
            dict: Updated content.
        """
        for group in (
                template_parts_file_content)['elabftw']['extra_fields_groups']:
            group['id'] = new_id

        for field in template_parts_file_content['extra_fields'].values():
            field['group_id'] = new_id

        return template_parts_file_content

    @staticmethod
    def concatenate(existing_template_parts_content,
                    new_template_part_content):
        """
        Concatenates two template part contents.

        Parameters:
            existing_template_parts_content (dict): Existing content.
            new_template_part_content (dict): New content to add.

        Returns:
            dict: Merged content.
        """
        existing_template_parts_content['elabftw'][
            'extra_fields_groups'].extend(
            new_template_part_content['elabftw']['extra_fields_groups']
        )
        existing_template_parts_content['extra_fields'].update(
            new_template_part_content['extra_fields']
        )
        return existing_template_parts_content

    @staticmethod
    def save_template(full_template_content, template_file_path):
        """
        Saves the template content to a JSON file.

        Parameters:
            full_template_content (dict): Content to save.
            template_file_path (str): Path to the output file.

        Returns:
            None
        """
        with open(template_file_path, 'w') as f:
            json.dump(full_template_content, f, indent=4)

    @staticmethod
    def generate_template(template_parts_list_file, template_file_path):
        """
        Generates a complete template by merging all listed parts.

        Parameters: template_parts_list_file (str): Path to the CSV file
        listing the parts. template_file_path (str): Path to the output JSON
        file.

        Returns:
            None
        """
        template_parts_list = TemplateBuilder.read_template_parts_list(
            template_parts_list_file)
        full_template_content = None

        for new_id, template_part_file in enumerate(template_parts_list):
            template_part = TemplatePart(template_part_file)
            new_template_part_content = TemplateBuilder.set_content_id(
                new_id + 1, template_part.template_content)

            if full_template_content is None:
                full_template_content = new_template_part_content
            else:
                full_template_content = TemplateBuilder.concatenate(
                    full_template_content, new_template_part_content
                )

        TemplateBuilder.save_template(full_template_content,
                                      template_file_path)
