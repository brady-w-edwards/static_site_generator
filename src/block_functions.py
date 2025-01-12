import re
from inline_functions import *
from htmlnode import ParentNode, LeafNode


# BLOCK TYPE CONSTANTS
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def markdown_to_htmlnode(markdown):
    md_children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            h_value = heading_type(block)
            block_node = LeafNode(f"h{h_value}", block)
            md_children.append(block_node)
        if block_type == block_type_paragraph:
            paragraph_node = text_to_children(block)
            md_children.append(paragraph_node)
        if block_type == block_type_code:
            code_children = text_to_children(block)
            code_node = ParentNode("pre", code_children)
            md_children.append(code_node)
        if block_type == block_type_quote:
            quote_node = LeafNode("blockquote", block)
            md_children.append(quote_node)
        if block_type == block_type_olist:
            md_children.append(list_node(block, "olist"))
        if block_type == block_type_ulist:
            md_children.append(list_node(block, "ulist"))
    return ParentNode("div", md_children)

def list_node(markdown_list, list_type):
    list_line_nodes = []
    lines = text_to_children(markdown_list)
    for line in lines:
        list_item = ParentNode("li", line)
        list_line_nodes.append(list_item)
    olist_node = ParentNode(f"{list_type}", list_line_nodes)
    return olist_node


def text_to_children(text):
    html_node_children = []
    lines = text.splitlines()
    for line in lines:
        inline_text_node = text_to_textnodes(line)
        inline_html_node = text_node_to_html_node(inline_text_node)
        html_node_children.append(inline_html_node)
    return html_node_children


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        new_block = block.strip()
        if new_block == "":
            continue
        new_blocks.append(new_block)
    return new_blocks


def block_to_block_type(block):
    lines = block.split("\n")
    
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph
    