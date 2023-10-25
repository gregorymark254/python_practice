# dictionaries
band = {
    "vocals": "Plant",
    "guiter": "Page"
}

band2 = dict(vocals="plants", guiter="page")

print(band)
print(band2)
print(type(band))
print(len(band))

# access items
print(band["vocals"])
print(band.get("guiter"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key\value pair as tiples
print(band.items())

# verify a key exists
print("guiter" in band)
print("triangle" in band)


# cahnge values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# remove item
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

# delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# copy dictonaries
# band2 = band  # creates a reference
# print("Bad copy")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy")
print(band)
print(band2)

# or use the dict() consttructer function
band3 = dict(band)
print("Good copy")
print(band3)

# nested dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guiter"
}
band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])

# sets
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# no duplicates allowed
nums = {1, 2, 2, 3}
print(nums)

# true is a dupe of 1, false is a dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in the set with an index position or a key
nums.add(8)
print(nums)

# add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# you can use update with list tuples and dictionaries too.
# merge 2 sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# keep dulicates only
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# keep everything except dulicates only
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
