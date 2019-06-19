s=' A method is like a function, but it runs "on" an object '
s2='-'
print(s.lower()) # Returns the lowercase version of the string
print(s.upper()) # Returns the uppercase version of the string
print(s.strip()) # Returns a string with whitespace removed from the start and end
print(s.isalpha()) # tests if all the string chars are in alpha numeric character classes
print(s.isdigit()) # tests if all the string chars are in digit character classes
print(s.isspace()) # tests if all the string chars are in space character classes
print(s.startswith(" ")) # Tests if the string starts with the given other string
print(s.endswith(" ")) # Tests if the string ends with the given other string
print(s.find("like")) # Searches for the given  string within s and returns the first index where it begins
print(s.replace("like","love")) # Returns a string where all occurrences of 'old' have been replaced by 'new'
print(s.split()) # returns a list of substrings separated by the given delimiter
print(s2.join(s))  #opposite of split()
