class HTMLNode:
    """
        tag(optional): html tag (e.g. h1, p, a)
        value(optional): the string of the tag
        children(optional): list of HTMLNode children []
        props(optional): dict of the node attribute (e.g href, class, id) - { href: "https://www.somedomain.com" }

        if HTMLNode without a 'tag' it means it just a plain text
        if HTMLNode without a 'value' it means it has some children
        if HTMLNode without a 'children' it has some text (value) 
        if HTMLNode without a 'props' it means it just a tag with a value or children 
    """
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("You have to implement this method before using it.")
    
    def props_to_html(self):
        attr = ""

        if self.props == None:
            return attr

        for key, val in self.props.items():
            attr += f" {key}=\"{val}\""
        return attr
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        # if self.tag == "img":
        #     return f"<{self.tag}{self.props_to_html()} />"

        if self.value == None:
            print("ERROR", self)
            raise ValueError("Missing Value in LeafNode")

        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>" 
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid Value: ParentNode must have a tag")
        if self.children is None:
            raise ValueError("Invalid Value: ParentNode must have children")
        
        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html += child.to_html()

        return html + f"</{self.tag}>"