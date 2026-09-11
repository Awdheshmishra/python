class bms:   # class--> blueprint
    def __init__  (f,name,id):
        f.name=name # instance variable
        f.id=id
    def showdata(f):  # instance method
        print(f.name," ",f.id)
user1=bms("arun", 121)
user2=bms("arundhati", 141) #object --> real world entity
user1.showdata()
user2.showdata()

# self represents the specific object (instance) that you are currently creating or manipulating. It acts as a reference pointer, allowing an object to access its own attributes and methods.

