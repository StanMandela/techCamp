"""
Dictionaries:
Unordered list of items
declare using {} braces
using Key values

"""
# myDict= {}
#print(type(myDict))
myDict= {

    1: 'orange',
    2: 'banana',
    3: 'Lemon'
}
print(myDict)
client={
    "Name": "Mandela",
    "Age": " 32",
    "Status": "Single",
    "Dislikes": [ "Lazyness","Pride", "Broke"],
    "Schools_attended": (" Nairobi School", "JKUAT"),
    "parents": {
        "mother": "nancy",
        "father": " peter"
    }
}
print(client)
print(client["Age"])
print(myDict[2])
print(client["Dislikes"][1])
print(client["Schools_attended"][0])
h = client["parents"]
print(h["mother"])