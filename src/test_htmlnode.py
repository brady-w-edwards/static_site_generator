import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

# HTML NODE TESTS
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