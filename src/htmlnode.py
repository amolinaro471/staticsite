class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.chidren}, props: {self.props}"
    
    def props_to_html(self):
        if self.props is None:
            return ""
        temp_props = ""
        for prop in self.props:
            temp_props += f" {prop}=\"{self.props[prop]}\""
        return temp_props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes require a value")
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            
    
    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, props= {self.props}"