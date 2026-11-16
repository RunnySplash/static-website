from enum import Enum

# different type of inline text
class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


# TextNode(TEXT, TEXT_TYPE, URL)
class TextNode():
    
    # constructor
    # Only link and images require URL field (None is used for others)
    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL
    
    # 2 text are eq if all properties are the same
    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    # string representation of a TextNode
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'



