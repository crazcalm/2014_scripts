"""
Build a reddit search web service. Your service should use the reddit api’s to perform the search and return the results as described below.
 
Helpful urls 
     - Reddit Api -  http://www.reddit.com/dev/api
     - Example reddit search call -  http://www.reddit.com/r/subreddits/search.json?q=test
Service requirements
     - sort the results by author name
     - return the results in any format you see fit. (JSON, XML, YAML, plain text,  etc…..)
Constraints 
     - You can use any libraries or frameworks you see fit
     - You must use Python as your programming language
"""

"""
Python 3.4
"""
from reddit_py import accounts, users, subreddits
import getpass

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        return accounts.user_login(self.username, self.password)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Username: %s" % self.username

def initialize_user():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    user = User(username, password)
    return user

if __name__ == "__main__":
    user = initialize_user()
    print(user)
