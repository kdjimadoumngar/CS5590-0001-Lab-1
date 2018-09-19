# 3. Consider the following scenario. You have a list of students who are attending class "Python" and another
# list of students who are attending class "Web Application".
# Find the list of students who are attending “python” classes but not “Web Application”

Python =["A", "B","C","D","E","F","G","H","I","J","K"] #  List of students in Python class

WEB =["C","D","E","F","G","H"] #  List of students in WEB class

count = [] # Initilialization of the count, empty

for bx in Python: # Loop through Python Class students. We used bx library as intersecter between the 2 classes.
    if bx not in WEB: # Compare with students in WEB Class
        count.append(bx) # Append the student to the counter Count if not found WEB
if count:
    print("These are students of Python class that are not in WEB Class")
    print(count)
else:
    print("All the students in Python class are in WEB Class")

    ########################################About bx###################################
    # The bx - python project is a python library and associated set of scripts to allow for rapid implementation
    # of genome scale analyses.The library contains a variety of useful modules, but the particular strengths are, among others:
    # “Intersecter” for performing fast intersection tests that preserve both query and target intervals and associated annotation
    # Generic data structure for indexing on disk files that contain blocks of data associated with intervals on various sequences
    # (used, for example, to provide random access to individual alignments in huge files; optomized for use over network filesystems)
    # Data structures for working with intervals on sequences

