import os, subprocess, sys

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    absolute_path = os.path.abspath(full_path)
    absolute_wd = os.path.abspath(working_directory)

    try:
            
        # File Path Validity checks
        if not absolute_path.startswith(absolute_wd):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        # Check if File exist
        elif not os.path.isfile(absolute_path):
            return f'Error: File "{file_path}" not found.'
        # Check if file is a python file
        elif not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
        else:
            # execute file and capture stdout and stderr
            completed_process = subprocess.run([sys.executable, absolute_path, *args], timeout=30, capture_output=True, cwd=absolute_wd)
            out = completed_process.stdout.decode()
            err = completed_process.stderr.decode()
            return_code = completed_process.returncode

            #check if stdout and stderr have anythin useful inside
            if out.strip() == "" and err.strip() == "":
                result = "No output produced."
            else:      
                result = f"STDOUT:{out}\nSTDERR:{err}"
            
            if return_code != 0:
                result += f"\nProcess exited with code {return_code}"
            
            return result
            
    except Exception as e:

        return f"Error: executing Python file: {e}"

