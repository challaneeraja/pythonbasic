from datetime import datetime
def get_date_time(func):
    def wrapper():
        print("Function name:"+func.__name__)
        print(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
        func()
    return wrapper
@get_date_time
def login():
    print("login")
@get_date_time
def logout():
    print("logout")
login()
logout()
