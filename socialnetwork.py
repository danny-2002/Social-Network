 ##THE SOCIAL NETWORK



class User:
    def __init__(self,username):
        self.username= username
        self.firstName= ""
        self.lastName= ""
        self.bio= ""
        self.friends=[]
        self.userId=""
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

    def createuserID(self,num):
        self.userID=num


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

    def createComment(self,comment):
        self.comments.append(comment)

class Network:
    def __init__(self):
        self.users= []

    def createUser(self, username):
        myuser=User(username)
        self.users.append(myuser)
        myuser.createuserID(len(self.users))

    def addConnection(self, Bobby, Steve):

        user10OBJ= self.getOBJ(user1)
        user20OBJ= selfgetOBJ(user2)

        user10OBJ.addFriend(user20OBJ)
        user20OBJ.addFriend(user10OBJ)

    def getOBJ(self,username):
        userID=self.getUserID(username)
        userOBJ= self.users[userID-1]
        return userOBJ

    def getUserID(self, username):
        for i in self.users:
            if i.username == username:
                return i.userID


if __name__ == "__main__":
##    username = "NBA(O)DCHAVEZ"

    network = Network()
    
    network.createUser("Daniel")
    network.createUser("Bobby")
    network.createUser("Steve")

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
##    print (Daniel.posts)
##    print (Bobby.posts)
##    print (Steve.posts)

##    print("user created!")
