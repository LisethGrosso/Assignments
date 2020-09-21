


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

    def describe_user(self):
        print(self.first_name+" "+self.last_name+", "+self.age+" years, User Name: "+self.user_name+", Email"+self.email+", Location:"+self.location+"\n")

    def greet_user(self):
        print("Hello ", self.first_name, self.last_name, sep=" ")
    
    def increment_login_attempts(self):
        self.login_attempts+=1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


##########################################################################################################
# P1: Restaurant Class

restaurant = Restaurant("Salvo Patria", "Colombian")
restaurant.describe_restaurant()
restaurant.open_restaurant()

##########################################################################################################
# P2: Restaurant Instances

r1 = Restaurant("Maido", "Peruvian")
r2 = Restaurant("Da Vittorio", "Italian")
r3 = Restaurant("Osaka", "Nikkei")
r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()

##########################################################################################################
# P3: User Class

u1 = User("Ellison", "Jones", 40, "elljones40", "elljones40@gmail.com", 1234445554, "US", "GA", "Atlanta", "30306")
u2 = User("Daniel", "Sailors", 50, "danielSailors14", "danielSailors14@gmail.com", 4803093762, "US", "CA", "San Diego", "92104")
u3 = User("Ben", "Johnson", 20, "benjohn", "benjohn@gmail.com", 5603034762, "US", "VA", "Richmond", "23249")


##########################################################################################################
# P4: Expanding the restaurant Class

r4 = Restaurant("Qun", "Nikkei", 1000 )
print(r4.number_served)
r4.number_served = 1300
print(r4.number_served)
r4.set_number_served(1555)
print(r4.number_served)


##########################################################################################################
# P5: Login Attempts for Users
u6 = User("Bob", "Walker", 72, "bobWalker", "bobWalker@gmail.com", 8790985674, "US", "OH", "Cincinnati", "45214")
u6.increment_login_attempts()
u6.increment_login_attempts()
u6.increment_login_attempts()
u6.increment_login_attempts()
print(u6.login_attempts)
u6.reset_login_attempts()
print(u6.login_attempts)