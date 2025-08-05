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


    # test split links & images
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
            ],
            new_nodes,
        )


    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](link.com) and another [second link](link.org)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "link.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "link.org")
            ],
            new_nodes,
        )

    def test_split_links_multi(self):
        node1 = TextNode("This is text with a [link](link.com) and another [second link](link.org)",TextType.TEXT,)
        node2 = TextNode("This is more text with a [link](link.gov)",TextType.TEXT,)
        node3 = TextNode("This is the [final link](link.edu) text",TextType.TEXT,)
        new_nodes = split_nodes_link([node1, node2, node3])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "link.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "link.org"),
                TextNode("This is more text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "link.gov"),
                TextNode("This is the ", TextType.TEXT),
                TextNode("final link", TextType.LINK, "link.edu"),
                TextNode(" text", TextType.TEXT)
            ],
            new_nodes
        )

    def test_split_links_multi(self):
        node1 = TextNode("This is text with an ![image](image.png) and another ![second image](image.jpg)",TextType.TEXT,)
        node2 = TextNode("This is more text with an ![image](image.webp)",TextType.TEXT,)
        node3 = TextNode("This is the ![final image](image.kra) text",TextType.TEXT,)
        new_nodes = split_nodes_image([node1, node2, node3])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "image.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "image.jpg"),
                TextNode("This is more text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "image.webp"),
                TextNode("This is the ", TextType.TEXT),
                TextNode("final image", TextType.IMAGE, "image.kra"),
                TextNode(" text", TextType.TEXT)
            ],
            new_nodes
        ) 

    # Test All Together
    def test_all(self):
        text = TextNode(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
            , TextType.TEXT)
        new_nodes = text_to_textnodes([text])
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),    
            ],
            new_nodes
        )





if __name__ == "__main__":
    unittest.main()