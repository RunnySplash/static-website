

# HTMLNode(TAG, VALUE, CHILDREN, PROPERTY)
class HTMLNode():
    
    # An HTMLNode without a tag will just render as raw text
    # An HTMLNode without a value will be assumed to have children
    # An HTMLNode without children will be assumed to have a value
    # An HTMLNode without props simply won't have any attributes
    def __init__(
            self, 
            tag: str | None=None, 
            value: str | None=None, 
            children: list["HTMLNode"] | None=None,
            props: dict[str, str] | None=None
    ) -> str:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    # Child classes will override to render themselves in HTML
    def to_html(self) -> str:
        raise NotImplementedError("to_html is not yet implemented")


    def props_to_html(self) -> str:

        html = ""

        if self.props is None:
            return html


        for key, value in self.props.items():
            html += f' {key}="{value}"'

        return html

    def __repr__(self) -> str:
        return (
            "HtmlNode({\n"
            f"    'tag': {self.tag!r},\n"
            f"    'value': {self.value!r},\n"
            f"    'children': {self.children!r},\n"
            f"    'props': {self.props!r}\n"
            "})"
    )


# Child Class of HTMLNode
# -> doesn't allow children
# -> value and tag args are required
class LeafNode(HTMLNode):
    
    def __init__(
            self,
            tag: str | None,
            value: str,
            props: dict[str, str] | None=None
    ) -> None:
        super().__init__(tag, value, None, props)


    # raise err if there's no value
    # otherwise if return a value if there's no tag
    #               or a <tag props>value</tag> 
    def to_html(self) -> str:
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        
        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

    def __repr__(self) -> str:
        return (
            "LeafNode({\n"
            f"    'tag': {self.tag!r},\n"
            f"    'value': {self.value!r},\n"
            f"    'props': {self.props!r}\n"
            "})"
        )

