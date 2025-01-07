import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from functions import text_node_to_html_node

# HTML NODE TESTS
class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        node = HTMLNode("a", "This is a link", None, props)
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())

# PARENT NODE TESTS
class TestParentNode(unittest.TestCase):
    def test_value(self):
        node = ParentNode("p", [LeafNode("b", "Leaf node 1")])
        self.assertEqual(node.__repr__(), 'ParentNode(p, children: [LeafNode(b, Leaf node 1, None)], None)')

    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_nested_parent(self):
        parent = ParentNode("div", [
            ParentNode("p", [
                LeafNode("b", "Bold text")
            ])
        ])
        self.assertEqual(parent.to_html(), "<div><p><b>Bold text</b></p></div>")

    def test_props(self):
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode("a", "link text", {"href": "https://www.google.com"}),
                LeafNode(None, "Normal text"),
            ],
            {"class": "link"}
        )
        self.assertEqual(
            node.to_html(),
            '<p class="link"><b>Bold text</b><a href="https://www.google.com">link text</a>Normal text</p>'
            )


# LEAF NODE TESTS
class TestLeafNode(unittest.TestCase):
    def test_no_value(self):
        node = LeafNode("p", None)
        try:
            node.to_html()
            print("Value error not raised")
        except ValueError:
            pass

    def test_no_tag(self):
        node = LeafNode(None, "This test should yield plain text")
        self.assertEqual(node.to_html(), "This test should yield plain text")

    def test_p_tag(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(
            node.to_html(),
            "<p>This is a paragraph</p>"
        )

    def test_link_tag(self):
        props = {"href": "https://www.google.com"}
        node1 = LeafNode("a", "Click me!", props)
        self.assertEqual(
            node1.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

class TestTextToLeafNode(unittest.TestCase):
    def text_normal(self):
        normal_node = TextNode("this is my text", TextType.NORMAL)
        self.assertEqual(
            repr(text_node_to_html_node(normal_node)),
            "LeafNode(None, this is my text, None)"
        )

    def test_bold(self):
        bold_node = TextNode("this is my text", TextType.BOLD)
        self.assertEqual(
            repr(text_node_to_html_node(bold_node)),
            "LeafNode(b, this is my text, None)"
        )

    def test_italic(self):
        italic_node = TextNode("this is my text", TextType.ITALIC)
        self.assertEqual(
            repr(text_node_to_html_node(italic_node)),
            "LeafNode(i, this is my text, None)"
        )

    def test_link(self):
        link_node = TextNode("this is my text", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(
            repr(text_node_to_html_node(link_node)),
            "LeafNode(a, this is my text, {'href': 'https://www.boot.dev'})"
        )

    def test_image(self):
        image_node = TextNode("this is my text", TextType.IMAGE, "https://www.boot.dev")
        self.assertEqual(
            repr(text_node_to_html_node(image_node)),
            "LeafNode(img, , {'src': 'https://www.boot.dev', 'alt': 'this is my text'})"
        )