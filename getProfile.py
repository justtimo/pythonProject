def get_profile(first, last, **user_info):
    ''' **user_info能够创建一个名为user_info的字典 '''
    user_info['first_name'] = first
    user_info["last_name"] = last
    print(user_info)
