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
        self.follower = follower
        self.following = following
        self.posts = posts

    def print_summary(self):
        print(f"""{self.name} (id={self.id})
                followers: {self.followers_count()}
                following: {self.following_count()}
                posts: {self.posts_count}
                likes_recieved: {self.likes_count}
            """)
    
    def follower_count(self):
        return len(self.follower)
    
    def following_count(self):
        return len(self.following)
    
    def posts_count(self):
        return len(self.posts)
    
    def likes_count(self):
        return len(self.likes)
        

class Follows: 
    def __init__(self, follower, followee):
        self.follower = follower 
        self.followee = followee 


class Posts: 
    def __init__(self, id, author_id, content, created_at, likes = 0):
        self.id = id 
        self.authro_id = author_id
        self.content = content 
        self.creataed_at = created_at 
        self.likes = likes 

class Likes: 
    def __init__(self, user_id, post_id):
        self.user_id = user_id 
        self.post_id = post_id



#Loading Data and Creating Objects: 

with open("social_data.json", "r") as file: 
    data = json.load(file)

users_data = data['users']
follows_json = data['follows']
posts = data['posts']
likes = data['likes']

#Create User Objects
users_list = []
for u in users_data: 
    user_obj = User(u["id"], u["username"])
    users_list.append(user_obj)

print(users_list)

#Create Following Objecst

