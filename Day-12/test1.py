# Open the file for reading
with open('abc.text', 'r') as file:
    # Read the content
    content = file.read()

# Modify the content (replace 'old' with 'new')
content = content.replace('Aws', 'Devops')

# Open the file for writing
with open('abc.text', 'w') as file:
    # Write the modified content back to the file
    file.write(content)