import re
from textnode import TextNode, TextType

def text_to_textnodes(text): 
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        chunks = node.text.split(delimiter)
        for i in range(0, len(chunks)):
            if chunks[i] == "":
                continue 

            # even index mean the splitted target
                
            if i % 2 != 0:
                new_nodes.extend([TextNode(chunks[i], text_type)])
                continue
            new_nodes.extend([TextNode(chunks[i], TextType.TEXT)])
    return new_nodes

def extract_markdown_image(text):
    regex = r"!\[(.*?)\]\((.*?)\)"
    images = re.findall(regex, text)
    return images

def extract_markdown_link(text):
    regex = r"(?<!\!)\[(.*?)\]\((.*?)\)"
    links = re.findall(regex, text)
    return links

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        images = extract_markdown_image(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        for image in images:
            text_list = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if text_list[0] != "":
                new_nodes.append(TextNode(text_list[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            
            if len(text_list) > 1:
                # more to the next chunk
                original_text = text_list[1:][0]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        links = extract_markdown_link(old_node.text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        for link in links:
            text_list = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if text_list[0] != "":
                new_nodes.append(TextNode(text_list[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            
            if len(text_list) > 1:
                # more to the next chunk
                original_text = text_list[1:][0]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes