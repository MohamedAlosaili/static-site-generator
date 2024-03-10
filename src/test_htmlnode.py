import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        html_node = HTMLNode("h1", "Hello World", None, {"class": "text-2xl font-bold text-center", "id": "hello-world-header"})
        self.assertEqual(repr(html_node), "<h1 class=\"text-2xl font-bold text-center\" id=\"hello-world-header\">Hello World</h1>")
        print("Test -> HTMLNode repr - passed ✅")
    
    def test_props_to_html(self):
        html_node = HTMLNode("a", "Click here", None, {"href": "https://www.google.com"})
        self.assertEqual(html_node.props_to_html(), " href=\"https://www.google.com\"")
        print("Test -> HTMLNode props_to_html - passed ✅")

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag(self):
        leaf_node = LeafNode("p", "This is a paragraph of text.")
        leaf_node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf_node.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(leaf_node2.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
        print("Test -> test_to_html_with_tag - passed ✅")

    def test_to_html_just_value(self):
        leaf_node = LeafNode(None, "Plain text without a tag")
        self.assertEqual(leaf_node.to_html(), "Plain text without a tag")
        print("Test -> test_to_html_just_value - passed ✅")

    def test_leaf_without_value(self):
        leaf_node = LeafNode("span", None)
        self.assertRaises(ValueError, leaf_node.to_html)
        print("Test -> test_leaf_without_value - passed ✅")

class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
        self.maxDiff = None
        parent_node = ParentNode(
                        "section",
                        [
                            LeafNode("h2", "Cool Title", {"id": "cool-title-id"}),
                            ParentNode("div", [
                                LeafNode("div", "Card 1"),
                                LeafNode("div", "Card 2"),
                                LeafNode("div", "Card 3"),
                                LeafNode("div", "Card 4"),
                            ]),
                            ParentNode("div", [
                                ParentNode(
                                    "p",
                                    [
                                        LeafNode("b", "Bold text"),
                                        LeafNode(None, "Normal text"),
                                        LeafNode("i", "italic text"),
                                        LeafNode(None, "Normal text"),
                                    ],
                                ),
                                ParentNode("a", [
                                    LeafNode(None, "Coolest"),
                                    LeafNode("b", "Backend Learning Platform"),
                                    LeafNode(None, "I ever see")
                                ])
                            ]),
                            ParentNode(
                                "p",
                                [
                                    LeafNode("b", "Bold text"),
                                    LeafNode(None, "Normal text"),
                                    LeafNode("i", "italic text"),
                                    LeafNode(None, "Normal text"),
                                ],
                            )
                        ],
                    )
        self.assertEqual(parent_node.to_html(), "<section><h2 id=\"cool-title-id\">Cool Title</h2><div><div>Card 1</div><div>Card 2</div><div>Card 3</div><div>Card 4</div></div><div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><a>Coolest<b>Backend Learning Platform</b>I ever see</a></div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></section>")
        print("Test -> test_parent_to_html - passed ✅")


    def test_parent_without_tag(self):
        parent_node = ParentNode(None, [])
        self.assertRaises(ValueError, parent_node.to_html)
        print("Test -> test_parent_without_tag - passed ✅")

    def test_parent_without_children(self):
        parent_node = ParentNode("p", None)
        self.assertRaises(ValueError, parent_node.to_html)
        print("Test -> test_parent_without_children - passed ✅")

if __name__ == "__main__":
    unittest.main()
