import os
import markdown

# List all Markdown files in the repository
markdown_files = [file for file in os.listdir('.') if file.endswith('.md')]

# Open README.md file to write the consolidated content
with open('README.md', 'w') as readme:
    for file_name in markdown_files:
        if file_name == "README.md":
            print('Skipping README.md')  # Added print statement for clarity
        else:    
            with open(file_name, 'r') as md_file:
                md_content = md_file.read()
                # Convert Markdown to HTML
                html_content = markdown.markdown(md_content)
                # Write HTML content to a new file
                with open(file_name.replace('.md','.html'), 'w') as html_file:
                    html_file.write(html_content)
                # Write content to README.md
                readme.write(f"## {file_name}\n\n")
                readme.write(md_content)
                readme.write('\n\n---\n\n')  # Separation between files

# Convert README.md to HTML separately
with open('README.md', 'r') as md_file:
    md_content = md_file.read()
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)
    # Write HTML content to a new file
    with open('index.html', 'w') as html_file:
        html_file.write(html_content)
