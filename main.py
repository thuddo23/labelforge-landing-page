#!/usr/bin/env python3
import os
import sys

def replace_domain_in_html_files(directory, old_domain, new_domain):
    # Walk through all subdirectories starting from the given directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                except Exception as e:
                    print(f"Error reading {file_path}: {e}", file=sys.stderr)
                    continue

                # Replace all occurrences of the old domain with the new domain
                new_content = content.replace(old_domain, new_domain)

                # If any changes were made, overwrite the file
                if new_content != content:
                    try:
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(new_content)
                        print(f"Updated: {file_path}")
                    except Exception as e:
                        print(f"Error writing {file_path}: {e}", file=sys.stderr)

if __name__ == '__main__':
    # Usage: python script.py [directory] [old_domain] [new_domain]
    # Defaults: current directory, "anolytics.ai", "labelforge.tech"
    directory = "./labelforge"
    old_domain = "anolytics.ai"
    new_domain = "labelforge.tech"

    if len(sys.argv) >= 4:
        directory = sys.argv[1]
        old_domain = sys.argv[2]
        new_domain = sys.argv[3]
    else:
        print("Using default values: directory='.', old_domain='anolytics.ai', new_domain='labelforge.tech'")

    replace_domain_in_html_files(directory, old_domain, new_domain)
