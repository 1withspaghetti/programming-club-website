
class actions:
    def valid_login(username, password):
        if username != None and password != None:
            return True
        return False
    
    def login_user(username):
        '''login action using stuff from accounts.py'''