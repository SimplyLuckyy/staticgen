import unittest

from htmlnode import HTMLNode, LeafNode
from textnode import *
from splitnodes import *


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
  
    # test splitnodes
    def test_1node(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])
    
    def test_1node_2blocks(self):
        node = TextNode("This is text with a **bold block** and a second **bold block**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" and a second ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
        ])

    def test_nonode(self):
        node = TextNode("This is plain text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is plain text", TextType.TEXT)])

    def text_multinodes(self):
        node1 = TextNode("This text is an _italic block_", TextType.TEXT)
        node2 = TextNode("And this text is a second _italic block_", TextType.TEXT)
        node3 = TextNode("This is the final _talic block_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2, node3], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This text is an ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode("And this is a second ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode("This is the final ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
            ])


if __name__ == "__main__":
    unittest.main()