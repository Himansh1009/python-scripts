users = ['Dave','John','Sara']

data = ['Dave',52,True]

emptylist =[]

print("Dave" in emptylist)

print(users[0])
print(users[-1])

print(users.index('Sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1]) 

print("")

print(len(data))

#here we are adding name to a list
users.append('Elsa')
print(users)
#>>> here it rquires [] to encapsulate names to put words into list else it would have put letters eg:- users += ('Jason') >> print(users)
users += ['Jason']
print(users)

users.extend(['eddie','Raghav'])
print(users)

#here we are adding anothers list to a list
# users.extend(data)
# print(users)

users.insert(0,'Johna') #here we are inserting a name at a particular index
print(users)

print('')

users[2:2] = ['Eddie','Alex']
print(users)

users[1:3] = ['Robert','JPJ']
print(users)

print("")

users.remove('Johna')
print(users)

print("")

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['dave']
users.sort()
print(users)


users.sort(key=str.lower)
print(users)

nums = [4,42,78,1,5]
nums.reverse()
print(nums)
# nums.sort()
# print(nums)

print("")

# nums.sort(reverse=True)
# nums.sort(reverse=True)
# print(nums)
# nums.sort(=True)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print("")
print(numscopy)
print(mynums)
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1,"Neil",True])

print(mylist)

#Tuples

mytuple = tuple(("dave",42,True))
anothertuple=(1,4,2,8,2,2)
print(mytuple)
print(type(mytuple))
print((type)(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey)= anothertuple
print(anothertuple)
print(one)
print(two)
print(hey)

print(anothertuple.count(2))