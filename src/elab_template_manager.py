import csv
import os
import json


def read_template_part_list(template_part_list_file):
    """
    Reads a list of template parts from a file (.csv or .txt).

    Parameters:
        template_part_list_file (str): Path to the input file.
                                       Must be a .csv or .txt file.

    Returns:
        list: A list of strings representing the template parts (lines).

    Raises:
        ValueError: If the file extension is not supported.
        FileNotFoundError: If the file does not exist.
    """
    template_part_list = []

    _, ext = os.path.splitext(template_part_list_file)

    if ext.lower() == ".csv":
        template_part_list = read_template_part_list_csv(template_part_list_file)

    elif ext.lower() == ".txt":
        template_part_list = read_template_part_list_txt(template_part_list_file)

    else:
        raise ValueError("File format not supported: must be .csv or .txt")

    # Check if each file exists and has a valid extension
    for index, template_part in enumerate(template_part_list):
        file = template_part.strip()
        _, ext = os.path.splitext(file)

        # Check file existence and extension validation for each line in the list
        if not os.path.exists(file):
            raise FileNotFoundError(f"File not found in line {index + 1}: {file}")
        elif ext.lower() not in [".csv", ".json"]:
            raise ValueError(f"Invalid file type in line {index + 1}: {file} (must be .csv or .json)")

    return template_part_list


def read_template_part_list_csv(template_part_list_file):
    """
    Reads template parts from a CSV file containing one JSON file per line in the first column.

    Parameters:
        template_part_list_file (str): Path to the .csv file.

    Returns:
        list: A list of strings representing the first column of each row.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    template_part_list = []
    if os.path.exists(template_part_list_file):
        with open(template_part_list_file, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:  # Ensure row is not empty
                    template_part_list.append(row[0])  # Get the first column
    else:
        raise FileNotFoundError(f"File not found: {template_part_list_file}")

    return template_part_list


def read_template_part_list_txt(template_part_list_file):
    """
    Reads template parts from a TXT file containing one JSON file per line.

    Parameters:
        template_part_list_file (str): Path to the .txt file.

    Returns:
        list: A list of strings parsed from JSON lines.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    template_part_list = []
    if os.path.exists(template_part_list_file):
        with open(template_part_list_file, mode='r', encoding='utf-8') as txtfile:
            for line in txtfile:
                line = line.strip()  # Remove any leading/trailing whitespace
                if line:
                    template_part_list.append(line)
    else:
        raise FileNotFoundError(f"File not found: {template_part_list_file}")

    return template_part_list
