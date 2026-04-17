def login(user, pwd):
    if user == "admin" and pwd == "admin":
        print("success")
    else:
        print("fail")


def test():
    x = None
    print(x.upper())  # crash
