info={
    "name" : "Shivam ",
    "subjets" : ["python","java","javasript"],
    "topics" :("dict","set"),
    "age" : 5,
    "is adult" : True
}

# print(info)
# print(info["name"])
# print(info["subjets"])
# print(info["topics"])
# print(info["age"])
# print(info["is adult"])

# info["lname"]= "Sharma"
# print(info["lname"])
# print(info)


student ={
    "name" : "shivam",
    "subjets" : {
        "phy": 85,
        "math" :89,
    }
}

print(type(student))
print(student.keys())
print(student.values())
student["name"]="ashu"
print(student)
print(student["subjets"])
print(student["subjets"]["phy"])
