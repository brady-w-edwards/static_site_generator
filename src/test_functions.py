import unittest
from textnode import TextNode
from functions import *

class TestSplitDelimiter(unittest.TestCase):
    def test_initial_result(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.NORMAL),
            ]
        )

    def test_two_nodes(self):
        node1 = TextNode("This is text with a `code block` word", TextType.NORMAL)
        node2 = TextNode("This is text with a `another code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.NORMAL),
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("another code block", TextType.CODE),
                TextNode(" word", TextType.NORMAL),
            ]
        )

    def test_bold(self):
        node = TextNode("This is text with **bold typed** words.", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.NORMAL),
                TextNode("bold typed", TextType.BOLD),
                TextNode(" words.", TextType.NORMAL),
            ]
        )

    def test_italic(self):
        node = TextNode("This is text with *italic typed* words.", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.NORMAL),
                TextNode("italic typed", TextType.ITALIC),
                TextNode(" words.", TextType.NORMAL),
            ]
        )

    def test_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_images(text),
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
        
    def test_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(
            extract_markdown_links(text),
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])