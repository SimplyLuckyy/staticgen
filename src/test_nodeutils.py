import unittest

from htmlnode import HTMLNode, LeafNode
from textnode import *
from nodeutils import *

class TestTextNode(unittest.TestCase):

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

    # test extract markdown
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a [link](https://www.boot.dev)")
        self.assertListEqual([("link", "https://www.boot.dev")], matches)

    def test_2links(self):
        matches = extract_markdown_links("This is text with a [link](https://www.boot.dev) and a [second link](https://www.boot.dev)")
        self.assertListEqual([
            ("link", "https://www.boot.dev"),
            ("second link", "https://www.boot.dev")], matches)
            
    def test_2images(self):
        matches = extract_markdown_images("This is text with a ![image](img.png) and a ![second image](img.jpg)")
        self.assertListEqual([
            ("image", "img.png"),
            ("second image", "img.jpg")], matches)

if __name__ == "__main__":
    unittest.main()