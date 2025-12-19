# class User:
#      pass


# user_1 = User()
# user_1.id = "001"
# user_1.username = "Alice" # Assigning username attribute (an attribute is attached to a variable using dot notation)

# print(user_1.username)

class User:
    def __init__(self, user_id, username):  # __init__ is a special method called a constructor
        self.id = user_id                  # Attributes are defined within the constructor
        self.username = username
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Harry")
user_2 = User("002", "Hermione")


user_1.follow(user_2)
print(user_1.followers)  # Output: 0
print(user_1.following)  # Output: 1
print(user_2.followers)  # Output: 1    
print(user_2.following) # Output: 0
