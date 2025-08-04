import unittest

from htmlnode import HTMLNode, LeafNode
from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_noteq2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is an another text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_equrl(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://https://www.wikipedia.org/")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://https://www.wikipedia.org/")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://https://www.wikipedia.org/")
        self.assertEqual(
            "TextNode(This is a text node, text, https://https://www.wikipedia.org/)", repr(node)
        )
    

    # test node to html
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_img(self):
        node = TextNode("alt text", TextType.IMAGE, "ImageLink")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "ImageLink", "alt": "alt text"})


if __name__ == "__main__":
    unittest.main()