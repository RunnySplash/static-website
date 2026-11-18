import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    
    def test_eq(self):
        node = HTMLNode(
            tag="p",
            value="Hello, world!",
            children=None,
            props={"href": "https://www.google.com","target": "_blank",}
        )

        ans = " href=\"https://www.google.com\" target=\"_blank\""

        self.assertEqual(ans, node.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node2 = LeafNode(
            tag="a",
            value= "Click Me!",
            props={"href": "https://www.google.com"}
        )
        self.assertEqual(node2.to_html(), "<a href=\"https://www.google.com\">Click Me!</a>")


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
