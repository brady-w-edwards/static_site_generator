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

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        print(node)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )