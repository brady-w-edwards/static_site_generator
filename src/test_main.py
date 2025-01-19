import unittest
from main import extract_title


class TestMainFunctions(unittest.TestCase):
    def test_markdown_title(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")