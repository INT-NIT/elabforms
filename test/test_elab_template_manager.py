from src.elab_template_manager import read_template_part_list
import os
import unittest
import json
from tempfile import NamedTemporaryFile
from src.elab_template_manager import (
    read_template_part_list,
    read_template_part_list_txt,
    read_template_part_list_csv
)


class TestElabTemplateManager(unittest.TestCase):

    def setUp(self):
        # create a temporaly csv file and a temp text file
        # tmp json
        self.txt_file = NamedTemporaryFile(mode="w+", delete=False, suffix=".txt")
        self.txt_file.write("template1.json\n")
        self.txt_file.write("template2.json\n")
        self.txt_file.close()

        # tmp csv file
        self.csv_file = NamedTemporaryFile(mode="w+", delete=False, suffix=".csv")
        self.csv_file.write("template1.json\n")
        self.csv_file.write("template2.json\n")
        self.csv_file.close()

    def tearDown(self):
        # clean file
        os.unlink(self.txt_file.name)
        os.unlink(self.csv_file.name)

    def test_read_template_part_list_txt(self):
        expected = ["template1.json", "template2.json"]
        result = read_template_part_list_txt(self.txt_file.name)
        self.assertEqual(result, expected)

    def test_read_template_part_list_csv(self):
        expected = ["template1.json", "template2.json"]
        result = read_template_part_list_csv(self.txt_file.name)
        self.assertEqual(result, expected)

    def test_read_template_part_list(self):
        expected = ["template1.json", "template2.json"]

        result1 = read_template_part_list_csv(self.txt_file.name)
        result2 = read_template_part_list_csv(self.txt_file.name)
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
