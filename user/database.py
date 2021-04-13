import json

class Constant:
    EMAIL = None

def logged_in(email, password):
    with open("user/data.json","r") as file:
        info=json.load(file)["info"]
    for user_dict in info:
        if user_dict["email"] == email and user_dict["password"] == password:
            Constant.EMAIL = email
            return True
    return False


def signed_up(name, email, password):
    with open("user/data.json","r") as file:
        info=json.load(file)["info"]
    info.append(
        {
            "name": name,
            "email": email,
            "password": password,
            "task_list": [
            ]
        }
    )
    upload(info)
    return True

def add_new_task(priority, task_name):
    with open("user/data.json","r") as file:
        info=json.load(file)["info"]
    for user_dict in info:
        if user_dict["email"] == Constant.EMAIL:
            user_dict["task_list"].append(
                {
                    "priority": priority,
                    "task_name": task_name,
                }
            )
            upload(info)
            return True
    return False


def delete_task(task_name):
    with open("user/data.json","r") as file:
        info=json.load(file)["info"]
    for user_dict in info:
        if user_dict["email"] == Constant.EMAIL:
            for each_task in user_dict["task_list"]:
                if task_name == each_task["task_name"]:
                    user_dict["task_list"].remove(each_task)
                    upload(info)
            return True
    return False


def upload(info):
    full_content = {"info": info}
    with open("user/data.json","w") as file:
        json.dump(full_content, file, indent=4)
    return True

def advanced_task_list():
    result = []
    with open("user/data.json","r") as file:
        info=json.load(file)["info"]
    for user_dict in info:
        if user_dict["email"] == Constant.EMAIL:
            temp = []
            for each_task in user_dict["task_list"]:
                temp.append((each_task["priority"],each_task["task_name"]))
            for priority,task_name in sorted(temp, reverse=True):
                result.append(task_name)
    return result            

def update_task(old_task_name, new_task_name, new_task_priority):
    delete_task(old_task_name)
    add_new_task(new_task_priority,new_task_name)
    return True