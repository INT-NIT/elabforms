# elabforms
A set of tools to create and manage standardized forms for eLabFTW


## Installation
```bash
git clone git@github.com:INT-NIT/elabforms.git
cd elabforms

pip install -r requirements.txt
``` 
## Usage
```bash
cd src

python generate_templates.py template_file_list.csv template_generated.json
```
## For full documentation , see [readthedocs](https://elabform.readthedocs.io/en/latest/)
## Example
assuming you have a file `template_file_list.csv` with the following content:
```csv
template_part_Example_1.json
template_part_Example_2.json

```bash
python generate_templates.py template_file_list.csv template_generated.json
```
 let 's template_part_Example_1.json` ![GENERIC_BIDS_SESSION](docs/GNERIC_BIDS_SESSION.png) 

with content:
```json
{
    "elabftw": {
        "extra_fields_groups": [
            {
                "id": 1,
                "name": "GENERIC_BIDS_SESSION"
            }
        ]
    },
    "extra_fields": {
        "session_id": {
            "type": "text",
            "value": "",
            "group_id": 1,
            "position": 0,
            "required": true,
            "description": "Ex: '01 or predrug or 20231206'"
        },
        "Session duration": {
            "type": "number",
            "value": "",
            "group_id": 1,
            "position": 3,
            "description": "The duration of the session [in minutes]",
            "blank_value_on_duplicate": true
        }
    }
}
```
and `template_part_Example_2.json` ![GENERIC_BIDS_SESSION](docs/RUN_BIDS.png),
with the following content:
```json
{
  "elabftw": {
    "display_main_text": true,
    "extra_fields_groups": [
      {
        "id": 2,
        "name": "Run "
      }
    ]
  },
  "extra_fields": {
    "TaskName": {
      "type": "text",

      "group_id": 2,
      "position": 0,

      "description": "Code name of the task (no space and only alphanumeric characters).\n Ex: 'rest or facesnback or headnodding'"
    },
    "RunNumber": {
      "type": "text",
      "value": "",
      "group_id": 2,
      "position": 2
    },
    "StartTime": {
      "type": "text",
      "value": "",
      "group_id": 2
    },
    "RunComment": {
      "type": "text",
      "value": "",
      "group_id": 2,
      "position": 3,
      "description": "Comment about the subject behavior during the run."
    },
    "TaskDescription": {
      "type": "text",
      "value": "  ",
      "group_id": 2,
      "position": 1,
      "description": "Description of the task"
    }
  }
}
```

This will generate the following file " template_generated.json" ![GENERIC_BIDS_SESSION](docs/template_generated.png),

which will contain the content of the two files `template_part_Example_1.json` and `template_part_Example_2.json` concatenated together.
```json
{
    "elabftw": {
        "extra_fields_groups": [
            {
                "id": 1,
                "name": "GENERIC_BIDS_SESSION"
            },
            {
                "id": 2,
                "name": "Run "
            }
        ]
    },
    "extra_fields": {
        "session_id": {
            "type": "text",
            "value": "",
            "group_id": 1,
            "position": 0,
            "required": true,
            "description": "Ex: '01 or predrug or 20231206'"
        },
        "Session duration": {
            "type": "number",
            "value": "91",
            "group_id": 1,
            "position": "3",
            "description": "The duration of the session [in minutes]",
            "blank_value_on_duplicate": true
        },
        "TaskName": {
            "type": "text",
            "group_id": 2,
            "position": 0,
            "description": "Code name of the task (no space and only alphanumeric characters).\n Ex: 'rest or facesnback or headnodding'"
        },
        "RunNumber": {
            "type": "text",
            "value": "",
            "group_id": 2,
            "position": 2
        },
        "StartTime": {
            "type": "text",
            "value": "",
            "group_id": 2
        },
        "RunComment": {
            "type": "text",
            "value": "",
            "group_id": 2,
            "position": 3,
            "description": "Comment about the subject behavior during the run."
        },
        "TaskDescription": {
            "type": "text",
            "value": "  ",
            "group_id": 2,
            "position": 1,
            "description": "Description of the task"
        }
    }
}
```bash
