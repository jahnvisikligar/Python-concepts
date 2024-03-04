'''1. Join items of a given list using '-' and print the string.'''
def convertToString(weekdays):
#Write your code here
	return("-".join(weekdays))
weekdays=['sun','mon','tue','wed','thu','fri','sat']	
print(convertToString(weekdays))

#-------------------------------------------------------------------------------------------------------------------

'''2. count the occurrences of a particular element in the list and output highest occurring element'''
def findMaxOccuringString(days):
    # Write your code here. Do not use counter() / count()
	count={}
	for i in days:
		if i in count:
			count[i]+=1
		else:
			count[i]=1
	highest_occurrence=max(count, key=count.get)
	return highest_occurrence
days=['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print(findMaxOccuringString(days))

#-------------------------------------------------------------------------------------------------------------------

'''3. Merge dictionaries a and b. The resultant dict must contain all items of'''
#both dicts. If key is common then the value of key in resultant dict
#must be the sum of value in a and b.
def dictMerge(a, b):
#Write your code here
	result=a|b
	for key in set(a) & set(b):
 		result[key]=a[key]+b[key]
	return result    
a = {'a': 1, 'y': 2, 'z': 3}
b = {'a': 4, 'b': 5, 'y': 6}
print(dictMerge(a,b))

#-------------------------------------------------------------------------------------------------------------------

'''4. Return the Item with highest value count'''
def itemWithHighestValue(items):
#Write your code here.
#Output: Mumbai
	max_count=0
	max_item=None
	for item in items:
		for key,value in item.items():
			if value>max_count:
				max_count=value
				max_item=key
	return max_item
items = [{'Delhi': 3}, {'Mumbai': 9}, {'Goa': 7}, {'Gujrat': 4}]
print(itemWithHighestValue(items))

#-------------------------------------------------------------------------------------------------------------------

'''5. Implement a group_by_owners function that:
● Accepts a dictionary containing the file owner name for each file name.
● Returns a dictionary containing a list of file names for each owner name,in any order.
For example, for dictionary
{'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
the group_by_owners function should return
{'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.'''
def group_by_owners(files):
#Write your code here
	group_by={}
	for key,value in files.items():
		group_by[value]=[key] if value not in group_by.keys() else group_by[value]+[key]
	return group_by
files={'Input.txt':'Randy','Code.py':'Stan','Output.txt':'Randy'}
print(group_by_owners(files))
