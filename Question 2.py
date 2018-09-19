# 2. Suppose you have two files. And what is inside the files are as follows:
#
# File1:
# “This time, we are going to learn how to write programs that recognize objects in images using deep learning. In other
# words, we are going to explain the black magic that allows Google Photos to search your photos based on what is in the picture”

# File2:
# “this we to are in the that your on based what is how other”

with open('File 1.txt', 'r') as file1: # Opening File 1

    with open('File 2.txt', 'r') as file2: # Opening File 1

        Intersect = set(file1).intersection(file2) # Intersection between File 1 and File 2

Intersect.discard('\n') # Removing all the intersection

with open('Intersection_file.txt','w') as output_file: # Open the output file

    for line in Intersect: # Loop through the intersect line and write the output

        output_file.write(line)



