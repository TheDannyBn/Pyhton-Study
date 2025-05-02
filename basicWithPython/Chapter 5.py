#Chapter 5 – Dictionaries and Structuring Data
#Create a dictionary with your name and age.
#Print the value of a key from the dictionary.
#Add a new key-value pair to the dictionary.
#Remove a key from the dictionary.
#Loop through all keys and print them.
#Loop through all values and print them.
#Check if a key exists in the dictionary.
#Create a list of dictionaries, each representing a person.
#Change a value in a dictionary.
#Use get() to safely retrieve a key that may not exist.

my_dict = {"name": "Danny", "age": 27}
print(my_dict["name"])

my_dict['city'] = "Ashdod"
print(my_dict)

del my_dict["age"]
print(my_dict)

for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

if "name" in my_dict:
    print("Name key exists!")

people = [
    {"name": "Danny", "age": 27,"city": "Ashdod"},
    {"name": "Sherry", "age": 30,"city": "Tel Aviv"},
    {"name": "Mali", "age": 25,"city": "Ashkelon"}
]

people[0]["age"] = 26
print(people[0])

job = my_dict.get("job", "Not specified")
print(job)