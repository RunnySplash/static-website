from enum import Enum

# different type of inline text
class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"


# TextNode(TEXT, TEXT_TYPE, URL)
class TextNode():
    
    # constructor
    def __init__(self, TEXT, TEXT_TYPE, URL):
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



