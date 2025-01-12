import unittest
from textnode import TextNode
from inline_functions import *

class TestInlineFunctions(unittest.TestCase):
    def test_initial_result(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_two_nodes(self):
        node1 = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is text with a `another code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("another code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_bold(self):
        node = TextNode("This is text with **bold typed** words.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("bold typed", TextType.BOLD),
                TextNode(" words.", TextType.TEXT),
            ]
        )

    def test_italic(self):
        node = TextNode("This is text with *italic typed* words.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("italic typed", TextType.ITALIC),
                TextNode(" words.", TextType.TEXT),
            ]
        )

    def test_image_extract(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_images(text),
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
        
    def test_link_extract(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(
            extract_markdown_links(text),
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
        
    def test_split_image(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                 TextNode("This is text with a ", TextType.TEXT),
                 TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            ]
        )

    def test_split_image_only(self):
        node = TextNode(
            "![rick roll](https://i.imgur.com/aKaOqIh.gif)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            ]
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                 TextNode("This is text with a ", TextType.TEXT),
                 TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                 TextNode(" and ", TextType.TEXT),
                 TextNode(
                     "obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                 ),
            ]
        )

    def test_split_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            ]
        )

    def test_split_link_only(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            ]
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                     "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                 ),
            ]
        )

    def test_text_to_textnode(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual(
            text_to_textnodes(text),
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )

    def test_empty_string(self):
        self.assertEqual(
            text_to_textnodes(""),
            [TextNode("", TextType.TEXT)]
        )

    def test_single_bold(self):
        self.assertEqual(
            text_to_textnodes("This is **bold** text"),
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT)
            ]
        )

    # def test_multiple_bold(self):
    #     self.assertEqual(
    #         text_to_textnodes("**Bold** normal **bold again**"),
    #         [
    #             TextNode("Bold", TextType.BOLD),
    #             TextNode(" normal ", TextType.TEXT),
    #             TextNode("bold again", TextType.BOLD)
    #         ]
    #     )
