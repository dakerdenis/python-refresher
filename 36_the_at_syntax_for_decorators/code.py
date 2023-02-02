import functools
    
user = {"username": "jose", "access_level": "admin"}




def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"]  =="admin":
            return func()
        else:
            return f"No admin permission for {user['username']}."
    
    return secure_function


@make_secure   #get_admin_password = make_secure(get_admin_password)
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"
    



print(get_password("billing"))





