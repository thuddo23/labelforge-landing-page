import os


def rename_files_and_collect_changes(root_directory):
    """
    Traverse all directories under root_directory using os.walk.
    If a filename contains 'anolytics', rename the file by replacing
    'anolytics' with 'labelforge' and record the change.

    Returns:
        changed_names: list of tuples (old_filename, new_filename)
    """
    changed_names = []
    for root, dirs, files in os.walk(root_directory):
        for filename in files:
            if "Anolytics" in filename:
                old_filepath = os.path.join(root, filename)
                new_filename = filename.replace("Anolytics", "labelforge")
                new_filepath = os.path.join(root, new_filename)
                try:
                    os.rename(old_filepath, new_filepath)
                    changed_names.append((filename, new_filename))
                    print(f"Renamed: {old_filepath} -> {new_filepath}")
                except Exception as e:
                    print(f"Error renaming {old_filepath}: {e}")
    return changed_names


def update_file_contents(root_directory, changed_names):
    """
    Traverse all directories under root_directory and update file contents.
    For each file, replace any occurrence of an old filename (from changed_names)
    with the new filename.
    """
    for root, dirs, files in os.walk(root_directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            # Attempt to read the file content
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                print(f"Skipping {filepath} (could not read): {e}")
                continue

            original_content = content
            # Replace each occurrence of old filename with new filename
            for old_name, new_name in changed_names:
                content = content.replace(old_name, new_name)

            # Write back only if changes were made
            if content != original_content:
                try:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated contents in: {filepath}")
                except Exception as e:
                    print(f"Error writing to {filepath}: {e}")


def main():
    root_directory = './labelforge'  # Change this if you want to start in a different directory
    # Step 1: Rename files and record changes
    changed_names = rename_files_and_collect_changes(root_directory)
    # Step 2: Update file contents based on the name changes
    if changed_names:
        update_file_contents(root_directory, changed_names)
    else:
        print("No files were renamed; nothing to update in file contents.")


if __name__ == "__main__":
    main()
