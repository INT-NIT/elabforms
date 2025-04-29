import csv
import os
import json


def read_template_part_list(template_part_list_file):
    """
    Reads a list of template part file paths from a CSV or TXT file.

    Parameters:
        template_part_list_file (str): Path to the .csv or .txt file containing the list.

    Returns:
        list of str: A list of file paths as strings.

    Raises:
        ValueError: If the file extension is not supported.
        FileNotFoundError: If the file does not exist.
    """
    pass


def read_template_part_list_csv(template_part_list_file):
    """
    Reads file paths from a CSV file. Assumes the first column contains the paths.

    Parameters:
        template_part_list_file (str): Path to the CSV file.

    Returns:
        list of str: A list of strings from the first column of each row.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    pass


def read_template_part_list_txt(template_part_list_file):
    """
    Reads file paths from a TXT file, assuming one path per line.

    Parameters:
        template_part_list_file (str): Path to the TXT file.

    Returns:
        list of str: A list of strings, each corresponding to one line in the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    pass


def read_template_part(template_part_file):
    """
    Reads a JSON template part file and extracts the 'groupfield' and its details.

    Parameters:
        template_part_file (str): Path to a JSON file representing a template part.

    Returns:
        tuple:
            - str the  'groupfield' .
            - list of dict: The list of 'groupfield_details'.

    Raises:
        FileNotFoundError: If the JSON file does not exist.
        json.JSONDecodeError: If the JSON structure is invalid.
    """
    pass


def check_template_part_structure(template_part_file_content):
    """
    Validates the structure of a template part content against Elab format rules.

    Parameters:
        template_part_file_content (dict): The JSON-parsed content of the template part.

    Returns:
        bool: True if the structure is valid.

    Raises:
        ValueError: If the structure does not meet the required format.
        Warning: If some fields do not have corresponding 'groupfield' mappings.
    """
    pass


def edite_content_id(new_id, template_part_file_content):
    """
    Updates the ID of the content in a template part.

    Parameters:
        new_id (int): The new ID to assign.
        template_part_file_content (dict): The original template part content.

    Returns:
        dict: The updated template part content.
    """
    pass


def concate_template_part(existing_template_part_content, new_template_part_content):
    """
    Concatenates the contents of two template parts.

    Parameters:
        existing_template_part_content (dict): Content of the existing template.
        new_template_part_content (dict): Content of the new template to append.

    Returns:
        dict: The merged template content.
    """
    pass


def save_template(template_part_content, template_file_path):
    """
    Saves the template content to a JSON file.

    Parameters:
        template_part_content (dict): The content to save.
        template_file_path (str): Path to the output JSON file.

    Returns:
        None
    """
    pass


def generate_template(template_list_file,template_file_path):
    """
    Generates a full template by merging all template parts listed in a file.

    Parameters:
        template_list_file (str): Path to a .csv or .txt file listing JSON part files.
        template_file_path (str): Path to the output JSON file to save the template .


    Returns:
       None.
    """
    pass
