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

user_1 = User("001", "Harry")
user_2 = User("002", "Hermione")

print(user_1.id)