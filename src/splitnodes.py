from htmlnode import *
from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("Unclosed Syntax")
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            splitnodes = node.text.split(delimiter)
            for index in range(0, len(splitnodes)):
                if splitnodes[index] == "":
                    pass
                else:
                    if index % 2 == 0:
                        new_nodes.append(TextNode(splitnodes[index], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(splitnodes[index], text_type))
    return new_nodes

            