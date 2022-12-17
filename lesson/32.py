import os
"""tree =os.walk("tree")
for file in tree:
    print(file)"""
def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        level = root.count(os.sep)
        indent = " " * 4 * level
        print(f"{indent}[{os.path.basename(root)}]")
        sup = " " * 4 * (level + 1)
        for i in files:
            print(f"{sup}{i}")
read_dir("tree")