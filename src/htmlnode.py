

# HTMLNode(TAG, VALUE, CHILDREN, PROPERTY)
class HTMLNode():
    
    # An HTMLNode without a tag will just render as raw text
    # An HTMLNode without a value will be assumed to have children
    # An HTMLNode without children will be assumed to have a value
    # An HTMLNode without props simply won't have any attributes
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    # Child classes will override to render themselves in HTML
    def to_html(self):
        raise NotImplementedError("to_html is not yet implemented")


    def props_to_html(self):
        html = ""

        for key, value in self.props.items():
            html += f' {key}="{value}"'

        return html

    def __repr__(self):
        return (
            "Node({\n"
            f"    'tag': {self.tag!r},\n"
            f"    'value': {self.value!r},\n"
            f"    'children': {self.children!r},\n"
            f"    'props': {self.props!r}\n"
            "})"
    )
