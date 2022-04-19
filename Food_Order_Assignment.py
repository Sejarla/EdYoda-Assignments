import uuid

adm = {"ajay":"Ajay@143"}
users = {"guest":"12345"}
Items = {}
m=0
class admin: 
    def __init__(self):
        pass
    def Add_new_fooditem(self,Name,Quantity,Price,Discount,Stock):
        self.Name = Name
        self.Quantity = Quantity
        self.Price = Price
        self.Discount = Discount
        self.Stock = Stock
        m = str(uuid.uuid1())
        Items[m] = [self.Name,self.Quantity,self.Price,self.Discount,self.Stock]

    def View_all_Food_Items(self):
        for i in Items:
            print(f'Food ID : {i} ---> Item details : {Items[i]}')

    def Validate_id(self,id):
        self.id =id
        while Items.get(self.id) == None:
            self.id = input("enter the correct food id: ")
        return self.id


    def edit_all_fooditem(self):
        self.View_all_Food_Items()
        self.id = input("enter food id which to be modify: ")
        self.id = self.Validate_id(self.id)
        self.Name = input("enter updated Item name: ")
        self.Quantity = input("enter updated Quantity: ")
        self.Price = input("enter updated Price: ")
        self.Discount = input("enter updated discount: ")
        self.Stock = input("enter the updated stock value: ")

        Items[self.id] = [self.Name,self.Quantity,self.Price,self.Discount,self.Stock]
    
    def remove_fooditem(self):
        self.View_all_Food_Items()
        self.id = input("enter food id which to be remove: ")
        self.id = self.Validate_id(self.id)
        Items.pop(self.id)
        print(f'{self.id} is removed from Items')

def login():
    while(True):
        user = input("select 1.User 2.Admin 3.Quit: ") 
        if (user == "Admin" or user=="2"):
            userid = input("enter userid: ")
            passwd = input("Enter Password: ")
            if passwd == adm[userid]:
                print("Success")

                
            else:
                print("Pass/Userid incorrect")
                login()
        if(user == '3' or user== "Quit"):
            break
    return 0
j = admin()
j.Add_new_fooditem("Ajay","a","b","c","d")
j.Add_new_fooditem("Anu","l","g","f","e")

j.edit_all_fooditem()
j.remove_fooditem()

