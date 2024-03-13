import os, shutil

from textnode import TextNode
from copy_static import copy_content
from generate_page import generate_page

def main():
    source_dir = "./static"
    dist_dir = "./public"

    if os.path.exists(dist_dir):
        shutil.rmtree(os.path.join(dist_dir))

    print(f"Copying static files from {source_dir} -> {dist_dir}")    
    copy_content(source_dir, dist_dir)
    
    from_path = os.path.join("content", "index.md")
    template_path = os.path.join("template.html")
    dest_path = os.path.join("public", "index.html")
    generate_page(from_path, template_path, dest_path)

main()