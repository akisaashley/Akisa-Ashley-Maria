class User:
    def get_dashboard(self):
        return "User Dashboard"

class Admin(User):
    def get_dashboard(self):  
        return "Admin Dashboard with controls"

print(User().get_dashboard())   
print(Admin().get_dashboard())  
