class bank:
    def __init__(f,bank,ifsc):
        f.bank=bank
        f.ifsc=ifsc
    def showdata(f):
         print(f.bank," ",f.ifsc)
user1=bank("sbi", "SBIN0015684")
user2=bank("PBL", 1413) #object --> real world entity
user1.showdata()
user2.showdata()
