#! /usr/bin/python
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line

print("Enter the lines you want to add bullet points on, end your input with line '!'")

lines = []
for line in iter(input, '!'):  # Read multiple lines from user input
    line = '* ' + line  # Add bullet points
    lines.append(line)
text = '\n'.join(lines)
print(text)
