import os
import shutil
from textnode import TextType, TextNode
from block_functions import markdown_to_blocks, markdown_to_html_node

def main():
    copy_dir_to_new_dir("./static", "./public")
    generate_page("./content/index.md", "template.html", "./public")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    try:
        with open(from_path) as content_file:
            md_contents = content_file.read()
        
        with open(template_path) as template_file:
            template = template_file.read()
        
        html_node = markdown_to_html_node(md_contents)
        html_string = html_node.to_html()
        title = extract_title(md_contents)
        
        # Replace `{{ Title }}` and `{{ Content }}`
        new_template = template.replace("{{ Title }}", title)
        new_html = new_template.replace("{{ Content }}", html_string)

        filename = "index.html"
        file_path = os.path.join(dest_path, filename)
        os.makedirs(dest_path, exist_ok=True)

        with open(file_path, 'w') as file:
            file.write(new_html)

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except PermissionError as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    


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


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block.strip("# ")
        else:
            raise Exception("Invalid Markdown: no header present")



main()