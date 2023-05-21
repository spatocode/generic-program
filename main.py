import sys
import json


def sniff_schema(json_data):
    schema = {}
    message_data = json_data.get("message", {})
    for key, value in message_data.items():
        schema[key] = {"type": get_data_type(value), "tag": "", "description": "", "required": False}
    return schema


def get_data_type(data):
    if isinstance(data, str):
        return "string"
    elif isinstance(data, int):
        return "integer"
    elif isinstance(data, list) and len(data) > 0:
        if isinstance(data[0], dict):
            return "array"
        else:
            return "enum"


def dump_schema(schema, output_file):
    with open(output_file, "w") as file:
        json.dump(schema, file, indent=4)


def program(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            json_data = json.load(file)
    except FileNotFoundError:
        print(f"Input file '{input_file}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Invalid JSON format in '{input_file}'.")
        return

    schema = sniff_schema(json_data)
    dump_schema(schema, output_file)
    print(f"Schema generated successfully and saved to '{output_file}'.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python program.py input_file output_file")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        program(input_file, output_file)
