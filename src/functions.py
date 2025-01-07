from functools import reduce
import re
from textnode import TextType, TextNode
from htmlnode import LeafNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            strings = node.text.split(delimiter)
            i = 0
            while i < len(strings):
                if i % 2 == 0:
                    new_node = TextNode(strings[i], TextType.NORMAL)
                    new_nodes.append(new_node)
                else: 
                    new_node = TextNode(strings[i], text_type)
                    new_nodes.append(new_node)
                i += 1
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            return


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        else:
            return

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
            

def extract_markdown_images(text):
    find_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return find_images


def extract_markdown_links(text):
    find_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return find_links
