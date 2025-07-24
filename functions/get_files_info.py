# function to get the directory informations

import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(full_path)
    absolute_wd = os.path.abspath(working_directory)

    content = []
    
    if not absolute_path.startswith(absolute_wd):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    elif not os.path.isdir(absolute_path):
        return f'Error: "{directory}" is not a directory'

    else:
        try:
            files = os.listdir(path=absolute_path)
            for f in files:
                f_path = os.path.join(absolute_path, f)
                size = os.path.getsize(f_path)
                is_dir = os.path.isdir(f_path)
                content.append(f"- {f}: file_size:{size} bytes, is_dir={is_dir}")
            return "\n".join(content)
        except Exception as e:
            return f"Error: {e}"



get_files_info("")


