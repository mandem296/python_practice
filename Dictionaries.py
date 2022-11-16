#allows storing values in key value pairs
#whenever we want to access a particular information, we use a key to access it.
#word is the key
#definition is the value
#symbols used are {}
#keys can be numbers, letters as long as they are unique and one cannot repeat keys

#for example: Jan--> January

#give dictionary name and values
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

#accessing a specific key or value
#access dictionary
print(monthConversions["Mar"])

#or
#this is appropriate in cases where value is not available. helps in creating default value
#print(name_of_dictionary.get("name_of_key", "message if key is not mapped to anything"))

print(monthConversions.get("mad","Not a valid key"))