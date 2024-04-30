import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div", "Hello_World", None, {"class": "greeting", "href": "https://github.com"})
        self.assertEqual(node.props_to_html(),' class="greeting" href="https://github.com"')
    
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, World")
        self.assertEqual(node.to_html(), "Hello, World")



if __name__ == "__main__":
    unittest.main()