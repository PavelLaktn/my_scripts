#-*- encoding: utf-8 -*-
#!/usr/bin/python3
"""Delete all files except Z reports"""

import os

def delete_files(dpath: str) -> str:
    """
    Delete all files except the Z reports

    If the directory path doesn't exist return 'The path doesn't exist'
    else return the string with the count of all files in the directory
    and the count of deleted files.

    Args:
        dpath
            Type: string
            Description: Directory path
    Returns:
        Type: string
        Description: The 'The path doesn't exist' string
                     or the string with the count of all files in the directory
                     and the count of deleted files.
    """

    directory = os.path.abspath(dpath)
    print(directory)
    # Test whether the path exists
    if not os.path.exists(dpath):
        return "The path doesn't exist"
    else:
        # Make list of files
        files = os.listdir(directory)
        all_files_count = len(files)
        delete_files_count = 0
        for file in files:
            if file.find('Z') == -1:
                os.remove(directory + "\\" + file)
                delete_files_count += 1
        return "All files: {}  Delete files: {}".format(all_files_count, delete_files_count)

def main():
    # Directory path
    dpath = "C:\\Users\\Pavel\\Desktop\\Test"
    # Try to delete files and print the result
    result = delete_files(dpath)
    print(result)

if __name__ == '__main__':
    main()
