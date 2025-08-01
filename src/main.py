from textnode import *

def main():
    test_object = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(test_object)

main()