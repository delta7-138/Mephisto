from pre import *


"""
find friend vector between primary username 
and follower username for every follower
"""
def find_distance(root , v): 
    return np.linalg.norm(root - v)
    
def find_friend_vector(u_diary , f_diary): 
    final_vector_list = []
    final_vector_list.append(len(watchedFilmsWithRatings(u_diary)))
    final_vector_list.append(len(findCommonMovies(u_diary , f_diary)))
    final_vector_list.append(findCompatibility(u_diary , f_diary))
    # print(final_vector_list)
    return np.array(final_vector_list)

def query_followers(uobj): 
    u_diary = parse_entries(user.user_diary(uobj))
    u_followers = user.user_followers(uobj)
    v_dict = {}

    for fname in u_followers.keys(): 
        fobj = user.User(fname)
        f_diary = parse_entries(user.user_diary(fobj))
        if f_diary is None or len(f_diary) == 0: 
            continue 
        v_dict[fname] = find_friend_vector(u_diary , f_diary)
        print(v_dict)

    return v_dict 

"""
Loading for primary user
"""
# uname = input("Enter username : ")
# query_user = user.User(uname)

# print(query_followers(query_user))