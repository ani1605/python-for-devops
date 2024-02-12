import re

# Define the pattern you want to search for
pattern = r'\b\d{3}-\d{2}-\d{4}\b'  # Example pattern for a social security number

# Open the file and read its content
with open('example.txt', 'r') as file:
    content = file.read()

# Use re.findall() to find all occurrences of the pattern in the content
matches = re.findall(pattern, content)

# Print the matches
print("Matches:", matches)
