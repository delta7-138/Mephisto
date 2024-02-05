from pre import *
from userDistanceGraph import *

"""
Loading for primary user
"""
uname1 = input("Enter username 1: ")
uname2 = input("Enter username 2: ")
query_user_1 = user.User(uname1)
query_user_2 = user.User(uname2)

query_user_1_d = parse_entries(user.user_diary(query_user_1))
query_user_2_d = parse_entries(user.user_diary(query_user_2))
frenv = find_friend_vector(query_user_1_d , query_user_2_d)
refv = np.array([frenv[0] , frenv[0] , 100])

print(find_distance(frenv , refv))

