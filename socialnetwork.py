##THE SOCIAL NETWORK


    

class User:
    def __init__(self, firstName, lastName, username, bio, userID ):
        self.firstName= firstName
        self.lastName= lastName
        self.username= username
        self.bio= bio
        self.userID= userID
        self.friends=[]
        self.posts=[]

    def addFriend(self,username):
        self.friends.append(username)

##            def unfriend():

    def viewNewsFeed(self,friends):
        self.friends.append(posts)

if __name__ == "__main__":
    firstName = "Daniel"
    lastName = "Chavez"
    username = "XXDC"
    bio = "HI"
    userID = "4142"


    Daniel = User(firstName, lastName, username, bio, userID)
    Bobby = User("Bobby", "BobbyBrown", "BobbyBrownJr.", "Hello", "6578")
    Steve = User("Steve", "SteveJones", "SJ", "Hi", "8765")
    print(Daniel.firstName)
    print(Bobby.firstName)
    print(Steve.firstName)

    Daniel.addFriend("Bobby")
    Daniel.addFriend("Steve")
    print(Daniel.friends)
    Daniel.posts.append("IM HUNGRY")
    Bobby.posts.append("IM LAZY")
    Steve.posts.append("IM TIRED")
    print(Daniel.posts)
    print(Bobby.posts)
    print(Steve.posts)

    Daniel.viewNewsFeed(username)
