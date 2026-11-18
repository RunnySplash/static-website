from enum import Enum
from htmlnode import LeafNode

# different type of inline text
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


# TextNode(TEXT, TEXT_TYPE, URL)
class TextNode():
    
    # constructor
    # Only link and images require URL field (None is used for others)
    def __init__(self, TEXT: str, TEXT_TYPE: TextType, URL: str | None=None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL
    
    # 2 text are eq if all properties are the same
    def __eq__(self, other):
        
        # return false if other is not also a text node
        if not isinstance(other, TextNode):
            return false

        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    # string representation of a TextNode
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'


# function to convert a TextNode to an LeafNode
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
        if text_node is None:
            raise ValueError("TextNode must be provided")

        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(None, text_node.text, None)
            case TextType.BOLD:
                return LeafNode("b", text_node.text, None)
            case TextType.ITALIC:
                return LeafNode("i", text_node.text, None)
            case TextType.CODE:
                return LeafNode("code", text_node.text, None)
            case TextType.LINK:
                return LeadNode("a",
                                text_node.text,
                                {"href" : text_node.url}
                                )
            case TextType.IMAGE:
                return LeafNode("img",
                                None,
                                {"src": text_node.url, "alt": text_node.text}
                                )

            
            
            
