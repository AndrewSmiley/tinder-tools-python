__author__ = 'smileya'
import requests


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




