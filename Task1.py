dict = {'Sagar': 80,'Tarun': 75,'Vikas': 78,'Siddharth': 74}

name = input("Enter the student's name: ")
try:
    print(name,"'s marks: ", dict[name])
except:
    print("student not found")
