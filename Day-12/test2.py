def modify_file(file_path, old_text, new_text):
    # Open the file for reading
    with open(file_path, 'r') as file:
        # Read the content
        content = file.read()

    # Modify the content
    modified_content = content.replace(old_text, new_text)

    # Open the file for writing
    with open(file_path, 'w') as file:
        # Write the modified content back to the file
        file.write(modified_content)

# Example usage:
#file_path = 'abc.text'
#old_text = 'Devops'
#new_text = 'Jenkins'
modify_file("abc.text", "Jenkins", "Kubernetes")
