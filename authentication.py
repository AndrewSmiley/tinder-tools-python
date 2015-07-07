__author__ = 'smileya'
import requests
from urls import LOGIN_URL

class Authenticator:
    ##on init, let's try to authenticate
    """
    This class will serve as basically a running authentication object.
    Keep track of our auth details
    :param access_token the Facebook auth token represented as a string
    :param user_id the Facebook user ID
    """

    def __init__(self, access_token, user_id):
        self.access_token = access_token
        self.user_id = user_id
        self.tinder_token = None
        # In the constructor we want to actually attempt to make the
        #auth request


    def login(self):
        r = requests.post(LOGIN_URL, data={"facebook_token": self.access_token, "facebook_id": self.user_id})
        print(r.status_code, r.reason, r.text)
