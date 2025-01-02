from textnode import TextType, TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode

def main():
    new_obj = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(new_obj.__repr__())

main()