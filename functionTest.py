def get_user():
    '''打印哈喽'''
    print("hello")
def get_user_1(username):
    '''打印哈喽'''
    print("hello :" +username)
def get_user_2(animal_type ,animal_name):
    print(f"\n 我有一个 {animal_type}")
    print(f" 他叫{animal_name}")
def get_user_3(animal_type ,animal_name="无名氏"):
    """使用默认值参数,带有默认值的参数必须放在最后一个"""
    print(f"\n 我有一个 {animal_type}")
    print(f" 他叫{animal_name}")
def get_full_name(first_name,last_name):
    return f"\n 你的全名是:{first_name}{last_name}";
def get_full_name_with_middle_name(fist_name ,last_name ,mide_name=""):
    if mide_name:
        return f"\n {fist_name}{mide_name}{last_name}"
    else:
        return f"\n {fist_name}{last_name}"
def get_full_name_map(first_name,last_name):
    return {"firstName":first_name , "lastName": last_name}
def get_name (*names):
    for name in names:
        print(name)
def get_name_with_age (age,*names):
    print(f"\n你的年龄是{age}")
    for name in names :
        print(name)
def get_profile(first , last, **user_info):
    '''**user_info能够创建一个名为user_info的字典'''
    user_info['first_name']=first
    user_info["last_name"]=last
    return user_info

get_user()
get_user_1("wby")
get_user_2("cat","大白")
"""指定位置参数"""
get_user_2(animal_name="小黑",animal_type="奶牛猫")
get_user_3("狗")
get_user_3("鱼","大鲨鱼")
fullname=get_full_name("吴","丙寅")
print(fullname)

full_name_with_middle_name=get_full_name_with_middle_name("吴","丙寅","王")
print(full_name_with_middle_name)
full_name_with_middle_name2=get_full_name_with_middle_name("吴","丙寅")
print(full_name_with_middle_name2)

full_name_map=get_full_name_map("wang "," wei")
print(full_name_map)

flag = True
while flag:
    print(f"输入你的名字 ,如果要退出请输入 'quit'")
    first_name=input("first_name: ")
    if first_name.lower() == 'quit' :
        break
    last_name=input("last_name: ")
    if last_name.lower() == 'quit' :
        break
    age=int(input("你的年龄"))
    print(f"你的信息是: 你的全名:{first_name}{last_name}, 你今年是{age}岁")

get_name("吴丙寅","王威","拉格朗日","土豆泥")
get_name_with_age(16,"吴丙寅","王威","拉格朗日","土豆泥")


user_profile=get_profile("吴","丙寅",lacation='杭州',address='爵士风情')
for value in user_profile.values():
    print(f"\n{value}")
print(user_profile)
