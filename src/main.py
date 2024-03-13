import os, shutil

from textnode import TextNode
from copy_static import copy_content
from generate_page import generate_pages_recursive

def main():
    source_dir = "./static"
    dist_dir = "./public"

    if os.path.exists(dist_dir):
        shutil.rmtree(os.path.join(dist_dir))

    print(f"Copying static files from {source_dir} -> {dist_dir}")    
    copy_content(source_dir, dist_dir)
    
    dir_content_path = "content"
    template_path = "template.html"
    dest_dir_path = "public"
    generate_pages_recursive(dir_content_path, template_path, dest_dir_path)


main()