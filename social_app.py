import json 

"""
Goals: 
- Load Data
- Compute per-user stats:
    - # of followers
    - # number of users they are following 
    - # of posts they have created
    - total number of likes they recieved across all their posts
"""
class User():
    def __init__(self, id, username, follower=None, following=None, posts=None):     
        self.id = id 
        self.username = username
        self.follower = []
        self.following = []
        self.posts = []

    def print_summary(self):
        print(f"""
{self.username} (id={self.id})
followers: {self.follower_count()}
following: {self.following_count()}
posts: {self.posts_count()}
likes_recieved: {self.likes_count(self.posts)}
""")
    
    #Follower functions
    def add_follower(self, user):
        self.follower.append(user)

    def remove_follower(self, user):
        self.follower.remove(user)

    def follower_count(self):
        return len(self.follower)
    
    #Following Functions
    def add_following(self, user):
        self.following.append(user)

    def remove_following(self, user):
        self.following.remove(user)

    def following_count(self):
        return len(self.following)
    
    #Posts Functions
    def add_post(self, Posts):
        self.posts.append(Posts)

    def remove_post(self, Posts):
        self.posts.remove(Posts)

    def posts_count(self):
        return len(self.posts)
    
    #Likes Function
    def likes_count(self):
        like_count = 0
        for post in self.posts:
            like_count+= len(post.liked_by) 
        return like_count
        

class Follows: 
    def __init__(self, follower, followee):
        self.follower = follower 
        self.followee = followee 

class Posts: 
    def __init__(self, id, author_id, content, created_at, liked_by=None):
        self.id = id 
        self.author_id = author_id
        self.content = content 
        self.created_at = created_at 
        self.liked_by = [] 

class Likes: 
    def __init__(self, user_id, post_id):
        self.user_id = user_id 
        self.post_id = post_id

#Loading Data and Creating Objects: 
with open("social_data.json", "r") as file: 
    data = json.load(file)

users_data = data['users']
follows_data = data['follows']
posts_data = data['posts']
likes_data = data['likes']

#Create User Objects
users_list = []
for u in users_data: 
    user_obj = User(u["id"], u["username"])
    users_list.append(user_obj)

#Create Following Objects
follower_list = []
for f in follows_data: 
    follows_obj = Follows(f["follower_id"], f["followee_id"])
    follower_list.append(follows_obj)

#Create Posts Objects
posts_list = []
for p in posts_data:
    posts_obj = Posts(p["id"], p["author_id"], p["content"], p["created_at"])
    posts_list.append(posts_obj)

#Create Likes List 
likes_list = []
for l in likes_data:
    likes_obj = Likes(l["user_id"],l["post_id"])
    likes_list.append(likes_obj)

#Wiring Logic

#Lookup tables
user_by_id = {user.id: user for user in users_list}
post_by_id = {post.id: post for post in posts_list}

#Wire posts to authors
for post in posts_list:
    author = user_by_id[post.author_id]
    author.posts.append(post)

for rel in follower_list:
    follower_id = rel.follower
    followee_id = rel.followee

    follower_user = user_by_id[follower_id]
    followee_user = user_by_id[followee_id]

    follower_user.following.append(followee_user)
    followee_user.follower.append(follower_user)

for like in likes_list:
    user_id = like.user_id
    post_id = like.post_id

    liker = user_by_id[user_id]
    post = post_by_id[post_id]

    post.liked_by.append(liker)

for user in users_list:
    user.print_summary()