#Chapter 6 – Manipulating Strings
#Print the length of a string.
#Convert a string to uppercase and print it.
#Convert a string to lowercase and print it.
#Replace a word in a string with another word.
#Check if a string starts with a specific letter.
#Check if a string ends with a specific letter.
#Split a sentence into words using split().
#Join a list of words into one string using join().
#Use string formatting to insert a variable into a sentence.
#Remove leading and trailing spaces from a string.


text = '  Hello World!  '

print(len(text))
print(text.upper())
print(text.lower())
new_text = text.replace("World", "Python")
print(new_text)

print(text.startswith("H"))
print(text.strip().startswith("H"))

print(text.endswith("!"))
print(text.strip().endswith("!"))

words = text.split()
print(words)

word_list = ["Python", "is", "awesome"]
joined_text = ' '.join(word_list)
print(joined_text)

name = "Danny"
formatted_text = f"My name is {name}."
print(formatted_text)

stripped_text = text.strip()
print(stripped_text)