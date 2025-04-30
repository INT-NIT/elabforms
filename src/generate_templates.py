def read_template_parts_list(template_parts_list_file):
    """
    Reads a file containing a list of template parts to be concatenated.

    Parameters:
        template_parts_list_file (str): Path to the .csv or .txt file
        containing the list.

    Returns:
        list of str: A list of file paths as strings.

    Raises:
        ValueError: If the file extension is not supported.
        FileNotFoundError: If the file does not exist.
    """
    pass


def read_template_parts_list_csv(template_parts_list_file):
    """
    Reads file paths from a CSV file. Assumes the first column contains
    the paths.

    Parameters:
        template_parts_list_file (str): Path to the CSV file.

    Returns:
        list of str: A list of strings from the first column of each row.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    pass


def read_template_parts(template_parts_file):
    """
    Reads a JSON template parts file and extracts the 'groupfield' and
    its details.

    Parameters:
        template_parts_file (str): Path to a JSON file representing a
        template parts.

    Returns:
        tuple:
            - str: The 'groupfield'.
            - list of dict: The list of 'groupfield_details'.

    Raises:
        FileNotFoundError: If the JSON file does not exist.
        json.JSONDecodeError: If the JSON structure is invalid.
    """
    pass


def check_template_parts_structure(template_parts_file_content):
    """
    Validates the structure of a template parts content against Elab
    format rules.

    Parameters:
        template_parts_file_content (dict): The JSON-parsed content of
        the template parts.

    Returns:
        bool: True if the structure is valid.

    Raises:
        ValueError: If the structure does not meet the required format.
        Warning: If some fields do not have corresponding 'groupfield'
        mappings.
    """
    pass


def edit_content_id(new_id, template_parts_file_content):
    """
    Updates the ID of the content in a template parts.

    Parameters:
        new_id (int): The new ID to assign.
        template_parts_file_content (dict): The original template parts
        content.

    Returns:
        dict: The updated template parts content.
    """
    pass


def concatenate_template_parts(existing_template_parts_content,
                               new_template_parts_content):
    """
    Concatenates the contents of two template parts.

    Parameters:
        existing_template_parts_content (dict): Content of the existing
        template.
        new_template_parts_content (dict): Content of the new template
        to append.

    Returns:
        dict: The merged template content.
    """
    pass


def save_template(full_template_content, template_file_path):
    """
    Saves the template content to a JSON file.

    Parameters:
        full_template_content (dict): The content to save.
        template_file_path (str): Path to the output JSON file.

    Returns:
        None
    """
    pass


def generate_template(template_parts_list_file, template_file_path):
    """
    Generates a full template by merging all template parts listed in a
    file.

    Parameters:
        template_parts_list_file (str): Path to a .csv or .txt file
        listing JSON parts files.
        template_file_path (str): Path to the output JSON file to save
        the template.

    Returns:
        None
    """
    pass
