import re

from inline_markdown import text_to_textnodes 
from textnode import text_node_to_html_node
from htmlnode import LeafNode, ParentNode

class BlockType:
    HEADING="heading"
    PARAGRAPH="paragraph"
    CODE="code"
    QUOTE="quote"
    UNORDERED_LIST='unordered_list'
    ORDERED_LIST='ordered_list'

def markdown_to_html_node(markdown): 
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        print("\nBLOCK TYPE", block_type)
        if block_type == BlockType.HEADING:
            nodes.append(to_heading(block))
        elif block_type == BlockType.CODE:
            nodes.append(to_code(block))
        elif block_type == BlockType.QUOTE:
            nodes.append(to_quote(block))
        elif block_type == BlockType.UNORDERED_LIST:
            nodes.append(to_unordered_list(block))
        elif block_type == BlockType.ORDERED_LIST:
            nodes.append(to_ordered_list(block))
        elif block_type == BlockType.PARAGRAPH:
            nodes.append(to_paragraph(block))
    return ParentNode("div", nodes)
            

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    text_blocks = []
    # print("BLOCKs", blocks)
    for block in blocks:
        if block.strip() == "":
            continue
        print("\nBLOCK", block)
        text_blocks.append(block)

    return text_blocks

def block_to_block_type(block):
    heading_regex = r"^#{1,6} \w+"
    quote_regex = re.compile(r"^> .+", re.MULTILINE)
    unordered_list_regex = re.compile(r"^(-|\*) .+", re.MULTILINE)
    ordered_list_regex = re.compile(r"^\d\. \w+", re.MULTILINE)

    print("BLOCK", block)
    if re.match(heading_regex, block):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif re.match(quote_regex, block):
        return BlockType.QUOTE
    elif re.match(unordered_list_regex, block):
        return BlockType.UNORDERED_LIST
    elif re.match(ordered_list_regex, block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def text_to_leafnodes(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes

def to_heading(block):
    extract_heading_level = re.findall(r"^#{1,6}", block)[0]
    leafnodes = text_to_leafnodes(block.lstrip(r"#{1,6} "))
    return ParentNode(f"h{len(extract_heading_level)}", leafnodes)

def to_code(block):
    code_content = block[3:-3]
    leafnodes = text_to_leafnodes(code_content)

    return ParentNode("pre", [ParentNode("code",leafnodes)])

def to_quote(block):
    quote_content = block.replace("> ", "").split("\n")
    leafnodes = text_to_leafnodes(" ".join(quote_content))

    return ParentNode("blockquote", leafnodes)

def to_ordered_list(block):
    children = block.split("\n")
    list_items = []
    for child in children:
        child_text = re.sub(re.compile(r"^\d.\s", re.M), "", child).split("\n")
        leafnodes = text_to_leafnodes(" ".join(child_text))
        list_items.append(ParentNode("li", leafnodes))
    return ParentNode("ol", list_items)

def to_unordered_list(block):
    children = block.split("\n")
    list_items = []
    for child in children:
        child_text = re.sub(re.compile(r"^(-|\*)\s", re.M), "", child).split("\n")
        leafnodes = text_to_leafnodes(" ".join(child_text))
        list_items.append(ParentNode("li", leafnodes))
    return ParentNode("ul", list_items)

def to_paragraph(block):
    lines = block.split("\n")
    leafnodes = text_to_leafnodes(" ".join(lines))
    
    return ParentNode("p", leafnodes)
    

