 ##THE SOCIAL NETWORK


    

class User:
    def __init__(self,username):
        self.username= username
        self.firstName= ""
        self.lastName= ""
        self.bio= ""
        self.friends=[]
        self.posts=[]
        
    def addfirstName(self,firstName):
        self.firstName= firstName

    def addlastName(self,lastName):
        self.lastName= lastName

    def addbio(self,bio):
        self.bio= bio

    def addFriend(self,obj):
        self.friends.append(obj)

    def addposts(self,posts):
        self.posts.append(posts)

    def unFriend(self,username):
        for friend in friends:
            if friend.username==username:
               self.friends.remove(User(username))
            
    def viewNewsFeed(self,friends):
        for friend in self.friends:
            print(friend.posts)

    def viewFriends(self, friends):
        for people in friends:
            print(people.username)

if __name__ == "__main__":
    username = "NBA(O)DCHAVEZ"


    Daniel = User(username)
    Bobby = User("BobbyBrownJr")
    Steve = User("SteveJones")

    print(Daniel.firstName)
    print(Bobby.firstName)
    print(Steve.firstName)

    Daniel.addFriend(Bobby)
    Daniel.addFriend(Steve)

    Daniel.posts.append("IM HUNGRY")
    Bobby.posts.append("IM LAZY")
    Steve.posts.append("IM TIRED")

    Daniel.viewFriends(Daniel.friends)
    Daniel.viewNewsFeed(Daniel.friends)
   ##    print (Daniel.posts)
   ##    print (Bobby.posts)
   ##    print (Steve.posts)
