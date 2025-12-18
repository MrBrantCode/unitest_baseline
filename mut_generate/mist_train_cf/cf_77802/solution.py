"""
QUESTION:
Identify and return all duplicate files present in a file system, based on their paths. The input is a list of directory information, where each string represents a directory path followed by its file names and contents. The output should be a list of groups of duplicate file paths, where each group contains all the file paths of the files that share the same content.

A group of duplicate files is defined as at least two files that share identical content. The format of a single directory info string is: "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)", where n >= 1 and m >= 0.

Constraints:
- 1 <= paths.length <= 2 * 10^4
- 1 <= paths[i].length <= 3000
- 1 <= sum(paths[i].length) <= 5 * 10^5
- paths[i] consist of English letters, digits, '/', '.', '(', ')', and ' '.
- No files or directories share the same name within the same directory.
- Each given directory info represents a unique directory.
"""

def findDuplicate(paths):
    content_to_paths = {}
    for path_group in paths:
        path_data = path_group.split(" ")
        for file in path_data[1:]:
            open_b = file.find('(')
            close_b = file.find(')')
            file_name = file[:open_b]
            file_content = file[open_b+1 : close_b]
            if file_content not in content_to_paths:
                content_to_paths[file_content] = [path_data[0] + '/' + file_name]
            else:
                content_to_paths[file_content].append(path_data[0] + '/' + file_name)
    return [dup_files for dup_files in content_to_paths.values() if len(dup_files) > 1]