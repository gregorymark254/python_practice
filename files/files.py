# Read -error if it does not exist

import os
f = open("names.txt")
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("File does not exist.")
finally:
    f.close()

# append - ceate a file if it does not exist
f = open("names.txt", "a")
f.write("Neil\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# write(overwrite)
f = open("context.txt", "w")
f.write("I deleted all context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# two ways to create a new file

# opens a file for writing, creates the file if it does not exist
f = open("name_list.txt", "w")
f.close()

# create the specific file but return error if file exist
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

# delete a file
# avoid an error if it does not exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file was not found.")

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
