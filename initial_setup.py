from pathlib import Path
import os
import re

def replace_text_in_file(file_name, placeholder, replacement_text):

    to_process = Path(__file__).parent / file_name

    with open(to_process, 'r') as file:
        content = file.read()

    updated_content = content.replace(placeholder, replacement_text)

    with open(to_process, 'w') as file:
        file.write(updated_content)

def rename_python_src_directory(project_name):

    formatted_project_name = re.sub(r'[^a-z]', '', project_name.lower())

    python_src = Path(__file__).parent / 'src' / 'mayapythonprojecttemplate'
    python_src.rename(Path(__file__).parent / 'src' / formatted_project_name)
    return formatted_project_name

if __name__ == "__main__":
    user_name = os.getenv('USER_NAME')
    project_name = os.getenv('PROJECT_NAME')
    project_description = os.getenv('PROJECT_DESC')

    replace_text_in_file("README.md", "{{PROJECT_OWNER}}", user_name)
    replace_text_in_file("README.md", "{{PROJECT_NAME}}", project_name)
    replace_text_in_file("README.md", "{{PROJECT_DESC}}", project_description)
    replace_text_in_file("CONTRIBUTING.md", "{{PROJECT_OWNER}}", user_name)
    replace_text_in_file("CONTRIBUTING.md", "{{PROJECT_NAME}}", project_name)
    replace_text_in_file("mkdocs.yml", "{{SITE_NAME}}", project_name)
    new_project_name = rename_python_src_directory(project_name)
    replace_text_in_file("tests/maya/test_example.py", "{{PROJECT_NAME}}", new_project_name)
