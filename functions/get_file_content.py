import os
from . import config

MAX_CHARS = config.MAX_CHARS

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(full_path)
    absolute_wd = os.path.abspath(working_directory)
 
    
    # File Path Validity checks
    if not absolute_path.startswith(absolute_wd):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    elif not os.path.isfile(absolute_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    # read file in string
    try:
        with open(absolute_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if os.path.getsize(absolute_path) > MAX_CHARS:
                file_content_string += f"[...File {file_path} truncated at {MAX_CHARS} characters]"
            
            return file_content_string

    except Exception as e:
        return f"Error: {e}"


