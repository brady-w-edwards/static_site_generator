from enum import Enum

class TextType(Enum):
    normal = "normal"
    bold = "bold"
    italic = "italic"
    code = "code"
    links = "links"
    images = "images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(object, TextNode):
            return False
        else:
            return vars(self) == vars(other)
        
    def __repr__(self):
        type(self)