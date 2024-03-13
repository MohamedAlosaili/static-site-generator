import os, shutil


def copy_content(source_path, dest_path):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    
    dir_content = os.listdir(source_path)

    for item in dir_content:
        current_source_path = os.path.join(source_path, item)
        current_dest_path = os.path.join(dest_path, item)

        if os.path.isfile(current_source_path):
            print(f"copied {current_source_path} -> {current_dest_path} ✅")
            shutil.copy(current_source_path, current_dest_path)
            continue
        copy_content(current_source_path, current_dest_path)