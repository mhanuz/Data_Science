li=['dd','RRR','W','ssss']
print(sorted(li, key=len)) # sorted according to the length of strings
#print(sorted(li, key=li.lower)) # key argument specifying str.lower function to use for sorting
strs = ['xc', 'zb', 'yd' ,'wa']
def myfunc(s):  #  this function takes a string, and returns its last letter
    return s[-1]
print(sorted(strs, key=myfunc))
