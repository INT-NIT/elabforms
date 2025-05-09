import sys
from template_builder import TemplateBuilder


def main():
    """
    Main function to handle CLI arguments and execute the template generation.
    """
    if len(sys.argv) != 3:
        print("Usage: python cli.py <template_parts_list_file.csv>"
              " <output_template.json>")
        sys.exit(1)

    template_parts_list_file = sys.argv[1]
    output_template_file = sys.argv[2]

    try:
        TemplateBuilder(template_parts_list_file,
                        output_template_file)
        print(f"Template successfully generated and saved to"
              f" {output_template_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
