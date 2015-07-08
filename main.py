__author__ = 'smileya'
from messaging import Message
from authentication import Authenticator
import urls
#https://www.facebook.com/connect/login_success.html#access_token=CAAGm0PX4ZCpsBAKAZCS8vbuNy7hE1zB0jdScFiWPLboaB1hodBvvGmX10lb4ZA51j4tZBslYOo64ckaV2bRoCsRjZBYR3L6cBvsuuMPVAcwJHks9emOPmifDEHbu0IBBOOk0bPQGgZBUF5y5bvlIze3ZBOscHTXCuJIZAIYUrWAQQKpEYKfXzCy5AHAmzpJX5F8pAYZBfAbZAco61Rh0TY7kJZB&expires_in=3857
# ok so we'll need an access token and user ID andrew.smiley.90




# so let's try to send a basic request
#guess we should commit too
auth = Authenticator("CAAGm0PX4ZCpsBAOcrXW79ctGQ5IERvBr8A2zA5jUSiObrL27Y2bN9qil4VNl5bkKvp1yN1BmcR96f977MBkFpIJQwxWBbIqWY5gfPnRzLAFEFniXrUJTJiGisaMerDXykU85YGN271qATigljzX5AWxRuvJmdcbkrsZBcD5QTIkMMXCgE0RFIdREKZASy8QainaIEpGDrAeF73PZALID", "andrew.smiley.90")
auth.login()