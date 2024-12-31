import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node)

    def test_eq(self):
        node = HTMLNode("p", "This is a paragraph", None, None)
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node, node2)

    def test_tag_not_eq(self):
        node = HTMLNode("h1", "This is a heading")
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertNotEqual(node, node2)

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