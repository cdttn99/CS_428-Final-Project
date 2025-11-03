import re
import sys
import os

def remove_escapes(text):
    text = text.replace('\\\\', '\\')

    text = re.sub(r'\\([`*_{}\[\]()#+\-.!<>])', r'\1', text)

    return text

def clean_file(filename):
    # Read the File
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    # Convert \\\\ and \\ to \\ \ respectively and remove all other escapes
    cleaned_text = remove_escapes(text)
    # Overwrite the file with the new text
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(cleaned_text)
    print(f"Cleaned: {filename}")

if __name__ == "__main__":
    # Target a folder
    target = sys.argv[1]
    # Walk through every file in that folder
    for root, _, files in os.walk(target):
        for file in files:
            filepath = os.path.join(root, file)
            clean_file(filepath)