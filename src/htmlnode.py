
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError("invalid HTML: no value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def props_to_html(self):
        string = ""
        for key, value in self.props.items():
            string += f' {key}="{value}"'
        return string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self. value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
    