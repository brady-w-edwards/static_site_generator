import unittest
from block_functions import *


class TestBlockFunctions(unittest.TestCase):
    def test_markdown_to_block(self):
        md = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        self.assertEqual(
            markdown_to_blocks(md),
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ]
        )

    def test_block_type_heading(self):
        block = "# This is a heading"
        self.assertEqual(
            block_to_block_type(block),
            block_type_heading
        )

    def test_block_type_code(self):
        block = "```This is code```"
        self.assertEqual(
            block_to_block_type(block),
            block_type_code
        )

    def test_block_type_quote(self):
        block = ">This is a quote"
        self.assertEqual(
            block_to_block_type(block),
            block_type_quote
        )

    def test_block_multiple_quotes(self):
        block = ">This is a quote\n>The second line of the quotes"
        self.assertEqual(
            block_to_block_type(block),
            block_type_quote
        )

    def test_block_type_unordered_list(self):
        block = "- This is an unordered list\n- with two lines"
        self.assertEqual(
            block_to_block_type(block),
            block_type_ulist
        )

    def test_block_type_ordered_list(self):
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)