import os

# List all Markdown files in the repository
markdown_files = [file for file in os.listdir('.') if file.endswith('.md')]

# Open README.md file to write the consolidated content
with open('README.md', 'w') as readme:
    for file_name in markdown_files:
        with open(file_name, 'r') as md_file:
            content = md_file.read()
            # Write content to README.md
            readme.write(f"## {file_name}\n\n")
            readme.write(content)
            readme.write('\n\n---\n\n')  # Separation between files
