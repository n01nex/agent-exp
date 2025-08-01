import os

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(full_path)
    absolute_wd = os.path.abspath(working_directory)

    try:
            
        # File Path Validity checks
        if not absolute_path.startswith(absolute_wd):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # elif not os.path.exists(os.path.dirname(absolute_path)):
            #create new directories$

        os.makedirs(os.path.dirname(absolute_path),exist_ok=True)

        with open(absolute_path, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:

        return f"Error: {e}"

