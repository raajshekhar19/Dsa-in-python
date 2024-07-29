#slicing => slice() [start:stop:step]
name  = "bro code"
sub_str = name[0:2] # in pyton the stop index is exclusive
print(sub_str)
last_name = name[4:8]
print(last_name)

funcky_name =name[0:8:3]# same as [::3]
print(funcky_name)

#print the reversed name 
reversed_name = name[::-1]
print(reversed_name)

#reversed using slice
website1 = "https://google.com"
website2 ="https://wikipedia.com"
slice =slice(8,-4)
print(website1[slice])
print(website2[slice])

