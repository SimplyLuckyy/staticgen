import unittest

from htmlnode import HTMLNode, LeafNode

class TestTextNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("a", "link text", ["child1"], {"href": "https://www.google.com"})
        self.assertEqual(
            "HTMLNode(a, link text, ['child1'], {'href': 'https://www.google.com'})", repr(node)
        )

    def test_html_to_props(self):
        node = HTMLNode("a", "link text", ["child1"], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', node.props_to_html()
        )
    
    def test_props2(self):
        node = HTMLNode(value="link text", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', node.props_to_html()
        )
    
    def test_getarguments(self):
        node = HTMLNode("h1", "text")

        self.assertEqual(
            node.tag,
            "h1"
        )

        self.assertEqual(
            node.value,
            "text"
        )

        self.assertEqual(
            node.children,
            None
        )

        self.assertEqual(
            node.props,
            None
        )
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "none test")
        self.assertEqual(node.to_html(), "none test")
    
    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "h1 test")
        self.assertEqual(node.to_html(), "<h1>h1 test</h1>")