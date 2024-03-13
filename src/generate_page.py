import re, os, shutil

from block_markdown import markdown_to_html_node

def extract_title(markdown):
    print(markdown.split("\n"))
    title_regex = re.compile(r"^# .+$", re.M)
    titles_list = re.findall(title_regex, markdown)
    print(titles_list)
    if len(titles_list) == 0:
        raise ValueError("Invalid markdown: page must have title")
    return titles_list[0].replace("# ", "")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating Page from {from_path} to {dest_path} using {template_path} Template")

    from_file = open(from_path)
    markdown = from_file.read()
    from_file.close()

    template_file = open(template_path)
    template = template_file.read()
    template_file.close()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    page_content = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    mode = "x"
    if not os.path.exists(os.path.exists(dest_path)):
        mode = "x"
    dest_file = open(dest_path, mode)
    dest_file.write(page_content)
    dest_file.close()