from textnode import *

def main():
    new_obj = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(new_obj.__repr__())

main()