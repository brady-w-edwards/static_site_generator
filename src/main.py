import os
import shutil
from textnode import TextType, TextNode
from block_functions import markdown_to_blocks, markdown_to_html_node

def main():
    copy_dir_to_new_dir("./static", "./public")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    content_file = open(from_path)
    md_contents = content_file.read()
    template_file = open(template_path)
    template = template_file.read()
    html_node = markdown_to_html_node(md_contents)
    html_string = html_node.to_html()
    title = extract_title_markdown(md_contents)
    template.replace("\{\{Title\}\}", title)
    template.replace("\{\{Content\}\}", html_string)
    


def copy_dir_to_new_dir(source, destination):
    if os.path.exists(destination):
        print(f"Deleting files and directories in {destination}...")
        shutil.rmtree(destination)
    if not os.path.exists(destination):
        os.mkdir(destination)
        print(f"Copying files and directories in {source} to {destination}...")
        dir_to_copy = os.listdir(source)
        for item in dir_to_copy:
            item_path = os.path.join(source, item)
            if os.path.isfile(item_path):
                copied = shutil.copy(item_path, destination)
                print(f"Copied: {copied}")
            else: copy_dir_to_new_dir(item_path, os.path.join(destination, item))


def extract_title_markdown(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block.strip("# ")
        else:
            raise Exception("Invalid Markdown: no header present")



main()