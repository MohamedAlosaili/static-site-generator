import unittest

from block_markdown import BlockType, markdown_to_blocks, block_to_block_type, markdown_to_html_node
from htmlnode import ParentNode, LeafNode

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        result = markdown_to_blocks(markdown)
        self.assertListEqual(result, ["This is **bolded** paragraph", """This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line""", """* This is a list
* with items"""])
        
        print("Test -> test_markdown_to_blocks - passed ✅")

    def test_markdown_to_blocks_multi_empty_line(self):
        markdown = """This is **bolded** paragraph

        

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line



* This is a list
* with items"""
        result = markdown_to_blocks(markdown)
        self.assertListEqual(result, ["This is **bolded** paragraph", """This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line""", """* This is a list
* with items"""])
        
        print("Test -> test_markdown_to_blocks_multi_empty_line - passed ✅")

    def test_block_to_block_type_heading(self):
        block = "## Title"
        result = block_to_block_type(block)
        print(result)
        self.assertEqual(result, BlockType.HEADING)
        print("Test -> test_block_to_block_type_heading - passed ✅")

    def test_block_to_block_type_code(self):
        block = "``` console.log(\"Hello world\") ```"
        result = block_to_block_type(block)
        print(result)
        self.assertEqual(result, BlockType.CODE)
        print("Test -> test_block_to_block_type_code - passed ✅")

    def test_block_to_block_type_quote(self):
        block = "> text\n> text"
        result = block_to_block_type(block)
        print(result)
        self.assertEqual(result, BlockType.QUOTE)
        print("Test -> test_block_to_block_type_quote - passed ✅")

    def test_block_to_block_type_unordered_list(self):
        block = """- thing 1
        - thing2
        - thing3 
        """
        result = block_to_block_type(block)
        print(result)
        self.assertEqual(result, BlockType.UNORDERED_LIST)
        print("Test -> test_block_to_block_type_unordered_list - passed ✅")

    def test_block_to_block_type_ordered_list(self):
        block = """1. thing 1
        2. thing2
        3. thing3 
        """
        result = block_to_block_type(block)
        print(result)
        self.assertEqual(result, BlockType.ORDERED_LIST)
        print("Test -> test_block_to_block_type_ordered_list - passed ✅")

    def test_block_to_block_type_paragraph(self):
        block = """hello
        world 
        ."""
        result = block_to_block_type(block)
        print(result)
        self.assertEqual(result, BlockType.PARAGRAPH)
        print("Test -> test_block_to_block_type_paragraph - passed ✅")
    
    def test_markdown_to_html_node(self):
        self.maxDiff = None
        markdown = """### header

Some text here should be interpreted as paragraph

- thing1
- thing2
- thing3

Another text block should be a paragraph, **but** with some in *line* elements
for example `this text should be displayed as code`

> Cool quote"""

        actual = markdown_to_html_node(markdown)
        result_html = actual.to_html()

        self.assertEqual(
            result_html, 
            "<div><h3>header</h3><p>Some text here should be interpreted as paragraph</p><ul><li>thing1</li><li>thing2</li><li>thing3</li></ul><p>Another text block should be a paragraph, <b>but</b> with some in <i>line</i> elements for example <code>this text should be displayed as code</code></p><blockquote>Cool quote</blockquote></div>"
        )

        print("Test -> test_markdown_to_html_node - passed ✅")