from functools import reduce
from textnode import TextType, TextNode

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

# if len(sections) % 2 == 0:
#             raise ValueError("Invalid markdown, formatted section not closed")


