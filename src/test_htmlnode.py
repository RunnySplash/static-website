import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()
