


class Restaurant:
    def __init__(self, rname=0, ctype=None, number_served = 0):
        self.restaurant_name  = rname
        self.cuisine_type = ctype
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name+" is open!")
    def set_number_served(self, new_number_served):
        self.number_served = new_number_served
    def increment_number_served(self, customers_day=100):
        self.number_served += customers_day


class User:
    def __init__(self, first_name=None, last_name =None,age=0, user_name=None, email=None,phone = None, country = None, state = None, city= None, zipCode = None, login_attempts =0):
        self.first_name  = first_name
        self.last_name = last_name
        self.age= age
        self.user_name = user_name
        self.email = email
        self.phone = phone
        self.country = country
        self.state = state
        self.city = city
        self.zipCode = zipCode
        self.location = self.country + ", " + self.city+", " +self.state + " "+self.zipCode 
        self.login_attempts = login_attempts
    # def __str__(self):
    def describe_user(self):
        return (self.first_name+" "+self.last_name+", "+self.age+" years, User Name: "+self.user_name+", Email"+self.email+", Location:"+self.location+"\n")

    def greet_user(self):
        print("Hello ", self.first_name, self.last_name, sep=" ")
    
    def increment_login_attempts(self):
        self.login_attempts+=1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class IceCreamStand(Restaurant):
    def __init__(self, rname=0, ctype=None, number_served = 0, flavors=[]):
        super().__init__(rname, ctype, number_served)
        self.flavors = flavors

    def get_flavors(self):
        return self.flavors

class Admin(User):
    def __init__(self, first_name=None, last_name =None,age=0, user_name=None, email=None,phone = None, country = None, state = None, city= None, zipCode = None, login_attempts =0, privileges=[]):
        super().__init__(first_name, last_name ,age, user_name, email,phone, country, state, city, zipCode, login_attempts)
        self.privileges = privileges
    '''
    def __init__(self, first_name=None, last_name =None,age=0, user_name=None, email=None,phone = None, country = None, state = None, city= None, zipCode = None, login_attempts =0, privileges=[]):
        super().__init__(first_name, last_name ,age, user_name, email,phone, country, state, city, zipCode, login_attempts)
        self.privileges = Privileges(privileges)
    '''
    def XXshow_privileges(self):
        return self.privileges


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        return self.privileges

##########################################################################################################
# P1: Ice Cream Stand

ics1 = IceCreamStand("Orso", "Italian", 900, ["Cookies and Cream", "Cookie Dough", "Vanilla", "Brownie"] )
print(ics1.get_flavors)
##########################################################################################################
# P2: Admin

admin1 = Admin("Alan", "Torres", 35, "alantorres", "alantorres@gmail.com", 7861563456, "US", "IL", "Chicago", "60607", ["Can add post", "Can delete post", "Can ban user"])
print(admin1.XXshow_privileges())

##########################################################################################################
# P3: Privileges

admin2 = User("Candy", "Anderson", 30, "canderson", "canderson@gmail.com", 8641983567, "US", "OK", "Tulsa", "74137")
print(admin2.privileges.show_privileges())