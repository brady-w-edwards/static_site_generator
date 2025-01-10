import re


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
    if block.startswith("# "):
        return "Heading 1"
    if block.startswith("## "):
        return "Heading 2"
    if block.startswith("### "):
        return "Heading 3"
    if block.startswith("#### "):
        return "Heading 4"
    if block.startswith("##### "):
        return "Heading 5"
    if block.startswith("###### "):
        return "Heading 6"
    if block.startswith("```") and block.endswith("```"):
        return "code"
    if block.startswith(">"):
        quote_lines = block.splitlines()
        for quote_line in quote_lines:
            if quote_line.startswith(">"):
                continue
            raise Exception("Invalid Markdown: quote needs > in each line")
        return "quote"
    if block.startswith("* ") or block.startswith("- "):
        unordered_lines = block.splitlines()
        for unordered_line in unordered_lines:
            if unordered_line.startswith("* ") or unordered_line.startswith("- "):
                continue
            raise Exception("Invalid Markdown: list needs * or - in each line")
        return "unorderd_list"
    if block.startswith("1. "):
        ordered_lines = block.splitlines()
        i = 1
        for ordered_line in ordered_lines:
            if ordered_line.startswith(rf"^{i}\. .+$"):
                continue
            raise Exception("Invalid Markdown: list needs ordered numbers at each line")
        return "ordered_list"
    return "normal"
    