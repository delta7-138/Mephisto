import pre



"""
find friend vector between primary username 
and follower username for every follower
"""

def find_friend_vector(uname , fname): 
    
"""
Loading for primary user
"""
uname = input("Enter username : ")
query_user = user.User(uname)