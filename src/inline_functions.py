from functools import reduce
import re
from textnode import TextType, TextNode
from htmlnode import LeafNode


def text_to_textnodes(text):
    if text == "":
        return [TextNode(text, TextType.TEXT)]
    original = TextNode(text, TextType.TEXT)
    bold = split_nodes_delimiter([original], "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "*", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    image = split_nodes_image(code)
    done = split_nodes_link(image)
    return done


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            strings = node.text.split(delimiter)
            i = 0
            while i < len(strings):
                if i % 2 == 0:
                    new_node = TextNode(strings[i], TextType.TEXT)
                    new_nodes.append(new_node)
                else: 
                    new_node = TextNode(strings[i], text_type)
                    new_nodes.append(new_node)
                i += 1
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0],TextType.IMAGE, image[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0],TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def extract_markdown_images(text):
    find_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return find_images


def extract_markdown_links(text):
    find_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return find_links
