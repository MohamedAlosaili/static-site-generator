import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq_text_and_text_type(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)
        print("Test -> equality of 'text' and 'text_type' - passed ✅")

    def test_eg_all_prop_with_none_url(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)
        print("Test -> equality of all props - passed ✅")

    def test_eg_all_prop_with_nonempty_url(self):
        node = TextNode("This is a text node", "bold", "https://mohammed-alosayli.com")
        node2 = TextNode("This is a text node", "bold", "https://mohammed-alosayli.com")
        self.assertEqual(node, node2)
        print("Test -> equality of all props(filled) - passed ✅")

    def test_neq_text(self):
        node1 = TextNode("This is a text node.", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node1, node2)
        print("Test -> inequality of 'text' - passed ✅")

    def test_neq_text_type(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
        print("Test -> inequality of 'text_type' - passed ✅")

    def test_neq_url(self):
        node = TextNode("This is a text node", "bold", "https://github.com")
        node2 = TextNode("This is a text node", "bold", "https://mohammed-alosayli.com")
        self.assertNotEqual(node, node2)
        print("Test -> inequality of 'url' - passed ✅")

    def test_print(self):
        node = TextNode("This is a text node", "bold", "https://github.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, https://github.com)")
        print("Test -> text node representing - passed ✅")


if __name__ == "__main__":
    unittest.main()
