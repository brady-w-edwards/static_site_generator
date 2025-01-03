from htmlnode import LeafNode
from textnode import TextType

def text_node_to_html_node(text_node):
        if isinstance(text_node.text_type, TextType) == False:
            raise Exception("Invalid text type")
        match text_node.text_type.value:
            case "normal":
                return LeafNode(None, text_node.text)
            case "bold":
                return LeafNode("b", text_node.text)
            case "italic":
                return LeafNode("i", text_node.text)
            case "code":
                return LeafNode("code", text_node.text)
            case "link":
                return LeafNode("a", text_node.text, {"href": text_node.url})
            case "image":
                return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})