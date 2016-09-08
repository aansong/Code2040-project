import requests 
import json
import ast

# Step 2
s2url = "http://challenge.code2040.org/api/reverse"
s2complete = "http://challenge.code2040.org/api/reverse/validate"

step2 = requests.post(s2url, {'token':api_key})

reversed_word = step2.text[::-1]

finished2 = requests.post(s2complete, {'token':api_key, 'string':reversed_word})

print(step2.text)
print reversed_word

print (finished2.text)

# Step 3
s3url = "http://challenge.code2040.org/api/haystack"
s3fetch = requests.post(s3url, {'token':api_key})

my_dict = s3fetch.text
#dictionary = dict(my_dict)
#print my_dict
dictionary = ast.literal_eval(my_dict)
#print dictionary


target_word = dictionary["needle"]
target_index = 0
our_haystack = dictionary["haystack"]
#print("length of our haystack is {}".format(len(our_haystack)))
for x in range(len(our_haystack)):
	if our_haystack[x] == target_word:
		#print (our_haystack[x], " = ", target_word)

		target_index = x
		#print target_index
		break

s3complete = "http://challenge.code2040.org/api/haystack/validate"
finished3 = requests.post(s3complete, {"token": api_key, "needle":target_index})
print finished3.text

#Step 4

s4url = "http://challenge.code2040.org/api/prefix"
s4fetch = requests.post(s4url, {"token": api_key})
new_dict = s4fetch.text

to_use = ast.literal_eval(new_dict)
print(to_use)

s4_array = to_use["array"]
s4_answer_array = []
prefix = to_use["prefix"]
prefix_len = len(prefix)
for word in s4_array:
	if word.startswith(prefix) == False:
#	if word[:prefix_len] != prefix:
		s4_answer_array.append(word)

print s4_answer_array

s4validate = "http://challenge.code2040.org/api/prefix/validate"
finished4 = requests.post(s4validate, {"token":api_key, "array":s4_answer_array})

print finished4.text







