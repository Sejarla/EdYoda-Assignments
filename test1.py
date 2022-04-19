
adm = {"ajay":"Ajay@143"}
users = {"Ajay":["90","hh","jj","Ajay@143"]}
Items = {1:["Chicken","ll","220INR"],2: ["Tandoori","cc","223INR"]}
Items_sel = {}
Ordered = []
class User:
    def __init__(self):
        pass
    
    def register(self):
        self.name = input("Enter Full Name: ")
        self.Phno = input("Enter the phone number: ")
        self.email = input("Enter the email: ")
        self.add = input("enter the address: ")
        self.pwd = input("Enter the Password: ")
        users[self.name] = [self.Phno,self.email,self.add,self.pwd]

    def options_3(self):
        print("1.Place New Order \n2.Order History \n3.Update Profile\nPlease choose one in the above")
        self.choice = int(input("Select the options by giving 1 or 2 or 3"))
        return self.choice
    def view_items(self):
        k =1
        for i in Items:
            Items_sel[k] = Items[i]
            k += 1
        for l in Items_sel:
            print(l,Items_sel[l][0],Items_sel[l][1],Items_sel[l][2],sep = " ")
  
    def place_new_order(self):
        self.view_items()
        self.sel = input("enter the elements with")
        


def user_login():
    username = input("enter username: ")
    if users.get(username) == None:
        print("Please register by providing the follwoing details")
        k = User()
        k.register()
        print(f"Registered Successfully with {username}and given password")
        user_login()
        
    else:
        password = input("enter the password: ")
        if users[username][3] == password:
            print("success")
            k = User()
            choice = k.options_3()
            if choice == 1:
                k.place_new_order()
        else:
            print("pass incorrect please try again ")
            user_login()


user_login()