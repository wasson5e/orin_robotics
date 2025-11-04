#python script to change the labeling id on the annotations
import os, re

original_folder = '/Volumes/Extreme SSD/project-3-at-2025-11-03-19-00-dd58a817/labels'
output_folder = '/Volumes/Extreme SSD/project-3-at-2025-11-03-19-00-dd58a817/labels/updated'
file_array = []
dig_reg = "^(\d)\s"
files = os.listdir(original_folder)
for items in range(len(files)):
    print(files[items])
    #change the ID in the annotation
    path = original_folder + "/" + files[items]
    with open(path, "r") as fo:
        content = fo.read()
        #print(content)
        check = re.search(dig_reg, content)
        if check:
            print(True)
            print(check[0])
        else:
            print(False)
