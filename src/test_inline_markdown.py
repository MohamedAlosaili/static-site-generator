import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_image, extract_markdown_link, split_nodes_image, split_nodes_link, text_to_textnodes

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter_with_one_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT, None),
            TextNode("code block", TextType.CODE, None),
            TextNode(" word", TextType.TEXT, None),
        ])
        print("Test -> test_split_nodes_delimiter_with_one_block - passed ✅")

    def test_split_nodes_delimiter_with_two_blocks(self):
        node = TextNode("This is **text** with **two** bold blocks", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with ", TextType.TEXT),
            TextNode("two", TextType.BOLD),
            TextNode(" bold blocks", TextType.TEXT),
        ])
        
        print("Test -> test_split_nodes_delimiter_with_two_blocks - passed ✅")

    def test_extract_markdown_image(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and [anchor](https://boot.dev)"
        result = extract_markdown_image(text)
        self.assertListEqual(result, [("image", "https://i.imgur.com/zjjcJKZ.png")])
        print("Test -> test_extract_markdown_image - passed ✅")
    
    def test_extract_markdown_link(self):
        text = "This is text with a [anchor1](https://boot.dev), ![image](https://i.imgur.com/zjjcJKZ.png), and [anchor2](https://boot.dev)"
        result = extract_markdown_link(text)
        self.assertListEqual(result, [("anchor1", "https://boot.dev"), ("anchor2", "https://boot.dev")])
        print("Test -> test_extract_markdown_link - passed ✅")

    def test_extract_markdown_link_multi_words(self):
        text = "This is text with a [Long text for simple link](https://boot.dev)"
        result = extract_markdown_link(text)
        self.assertListEqual(result, [("Long text for simple link", "https://boot.dev")])
        print("Test -> test_extract_markdown_link_multi_words - passed ✅")

    def test_split_nodes_image_two_images(self):
        node = node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ])
        print("Test -> test_split_nodes_image_two_images - passed ✅")

    def test_split_nodes_image_one_image(self):
        node = node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        ])
        print("Test -> test_split_nodes_image_one_image - passed ✅")

    def test_split_nodes_link_two_links(self):
        self.maxDiff = None
        node = node = TextNode(
            "This is text with a [link one](https://www.google.com) and another [link two](https://www.facebook.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link one", TextType.LINK, "https://www.google.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "link two", TextType.LINK, "https://www.facebook.com"
            ),
        ])
        print("Test -> test_split_nodes_image_two_links - passed ✅")

    def test_split_nodes_link_one_link(self):
        node = node = TextNode(
            "This is text with a [link](https://boot.dev) and few text after",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" and few text after", TextType.TEXT),
        ])
        print("Test -> test_split_nodes_image_one_link - passed ✅")

    def test_text_to_textnodes(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)'
        result = text_to_textnodes(text)
        self.assertListEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])
        print("Test -> text_text_to_textnodes - passed ✅")