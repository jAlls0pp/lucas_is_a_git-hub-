import json

name = input("Enter name")#
age = input("Enter age")
street_num = input("Enter street number")
post_code = input("Enter postcode")


user_data = {"name" : name,
             "age" : age,
             "street_num" : street_num,
             "post_code" : post_code}

with open("json_data.json", "w") as file:
    json.dump(user_data,file,indent=4)

with open("json_data.json", "r") as file:
    new_user_dict = json.load(file)

print(new_user_dict)


print("I AM FINISHED")