import re, os, shutil

from block_markdown import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_content = os.listdir(dir_path_content)
    for item in dir_content:
        current_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(current_path):
            generate_page(current_path, template_path, dest_path.replace("md", "html"))
            continue

        generate_pages_recursive(current_path, template_path, dest_path)    

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

    if not os.path.exists(dest_path):
        os.makedirs(os.path.dirname(dest_path), 511, True)
        
    dest_file = open(dest_path, "x")
    dest_file.write(page_content)
    dest_file.close()