import os
import json
import unittest
from program import sniff_schema


class SchemaGenerationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.input_data = {
            "attributes": {
                "attribute1": "value1",
                "attribute2": "value2"
            },
            "message": {
                "key1": "value1",
                "key2": 123,
                "key3": ["1", "2", "3"],
                "key4": [{
                    "subkey1": "subvalue1",
                    "subkey2": "subvalue2"
                }],
                "key5": {
                    "subkey1": "subvalue1",
                    "subkey2": "subvalue2"
                }
            }
        }

        self.expected_schema = {
            "key1": {"type": "string", "tag": "", "description": "", "required": False},
            "key2": {"type": "integer", "tag": "", "description": "", "required": False},
            "key3": {"type": "enum", "tag": "", "description": "", "required": False},
            "key4": {"type": "array", "tag": "", "description": "", "required": False},
            "key5": {"type": None, "tag": "", "description": "", "required": False}
        }
        return super().setUp()

    def test_schema_generation(self):
        schema = sniff_schema(self.input_data)
        self.assertEqual(schema, self.expected_schema)


if __name__ == "__main__":
    unittest.main()
