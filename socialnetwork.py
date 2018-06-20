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

    def unFriend(self,like):
        for friend in friends:
            if friend.username==like.username:
               self.friends.remove(like)
            
    def viewNewsFeed(self,friends):
        for friend in self.friends:
            print(friend.posts)

    def viewFriends(self, friends):
        for people in friends:
            print(people.username)

class User:
    def __init__ (self,username):
        self.username=username


        friends=[]
        posts=[]

    def createPost(self,content):
        mypost = post(content)
        self.posts.append(mypost)
        mypost.createPostID(len(posts))

class Post:
    def __init__(self,content):
        self.content=content
        self.postID=" "
        self.comments=[]

    def createPostID(self,num):
        self.postID=num

class Network:
    def __init__(self):
        self.users= []

    def createUser(self, username):
        myuser=User(username)
        self.Users.append(myUser)
        myUser.createUserID(len(users))


if __name__ == "__main__":
##    username = "NBA(O)DCHAVEZ"

    network = Network()


    network.createUser("Daniel")
    Bobby = createUser("BobbyBrownJr")
    Steve = User("SteveJones")

##    print(Daniel.firstName)
##    print(Bobby.firstName)
##    print(Steve.firstName)
##
##    Daniel.addFriend(Bobby)
##    Daniel.addFriend(Steve)
##
##    Daniel.posts.append("IM HUNGRY")
##    Bobby.posts.append("IM LAZY")
##    Steve.posts.append("IM TIRED")
##
##    Daniel.viewFriends(Daniel.friends)
##    Daniel.viewNewsFeed(Daniel.friends)
##    Daniel.unFriend(Steve)
##    Daniel.viewFriends(Daniel.friends)
##   ##    print (Daniel.posts)
##   ##    print (Bobby.posts)
##   ##    print (Steve.posts)
