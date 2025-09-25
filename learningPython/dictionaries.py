#dictionaries
band = {
    "vocals":"Plant",
    "guitar":"Page"

}
band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

#Access Items
print(band["vocals"])
print(band.get("guitar"))

#list all keys
print(band.keys())

#list all value
print(band.values())

#list of keys/value pairs as tuples
print(band.items())

#verify a key exists 
print("guitar" in band)
print("triangle" in band)

#change values
band["vocals"] = "Coverdale"
band.update({"bass":"JPJ"})

print(band)

#remove items
print(band.pop("bass"))
print(band)

band["drums"]="Bonham"
print(band)

print(band.popitem()) # returns a tuple
print(band)

#Delete and clear

band["drums"]="Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dicitonaries

# band2 = band # create a reference
# print("Bad copy")
# print(band2)
# print(band )

# band2["drums"]="Dave"
# print(band )

band2 = band.copy()
band2["drums"]="Dave"
print("Good copy!")
print(band)
print(band2)

#or use the dict() constructor function  
band3 = dict(band )
print("Good copy!")
print(band3)

#nested dictionaries

member1 = {
    "name":"Plant",
    "instrument":"vocals"
}
member2 = {
    "name":"Page",
    "instrument":"guitar"
}
band = {
    "member1":member1,
    "member2":member2
} 
print("")
print(band)
print(band["member1"]["name"])

# sets

nums = {1,2,3,4}
nums2 = set((1,2,3,4))

print(nums )
print(nums2)
print(type(nums))
print(len(nums))

#no duplicates allowed
nums = {1,2,2,4} # it doesnt allow duplicate values as you can saee there are already two 2's here
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = {1,True,2,False,3,4,0} #ahh actually 1 is a duplicate of True as in programming 1 is considered true and it goes same for 0 as it is considered false. dupe meas duplicate
print(nums)

#check if a value is in a set
print(2 in nums)

#but you cannot refer to an element in the set with an index position or a key

#add a new elemnent to a set
nums.add(8)
print(nums)

# add elements from one set to another
morenums = {5,6,7}
nums.update(morenums) # we are passing numbers from more nums set to nums set
print(nums)

# you can use update with lists, tuples and dictionaries, too.

# merge two sets to create a new set
one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)

# keep only duplciates
one = {1,2,3}
two = {2,3,4}

one.intersection_update(two)
print(one)

# keep everything except duplciates
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)