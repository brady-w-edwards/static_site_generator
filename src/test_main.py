import unittest
from main import extract_title_markdown


class TestMainFunctions(unittest.TestCase):
    def test_markdown_title(self):
        md = "# Hello"
        self.assertEqual(extract_title_markdown(md), "Hello")