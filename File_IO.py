# with open("praties.txt", "w") as f:
#     f.write("Hi everyone\n")
#     f.write("We are learning File IO.\n")
#     f.write("using Python.\n")
#     f.write("I like programming in Python.")


with open("praties.txt","r") as f:
    data=f.read()
print(type(data))    
print(data)    
new_data=data.replace("Python","Java")
print(new_data)    

with open("praties.txt","w") as f:
    f.write(new_data)

# with open("praties.txt","r") as f:
#     data=f.read()
#     if(data.find("learning")):
#         print("found it")  
#     else:
#         print("Not found")    

def hek_for_line():
    word ="learning"
    data= True
    line =1
    with open("praties.txt","r") as f:
        while data :
            data=f.readline()
            if(word in data):
                print(line)
                return 
            else:
                line  +=  1  
    return -1
hek_for_line()