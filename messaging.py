__author__ = 'smileya'


# class to represent an individual message
#
# "messages": [{
#            "_id": "534651198ce6da797248c1a3",
#            "match_id": "53464b0728ac73976d0a3fbf",
#            "to": "53430689ab3c04c13e006ffb",
#            "from": "533a59ea52046fc077002815",
#            "message": "hi  .... how is it going?",
#            "sent_date": "2014-04-10T08:06:49.800Z",
#            "created_date": "2014-04-10T08:06:49.800Z",
#            "timestamp": 1397117209800
class Message:
    def __init__(self):
        #I'm assuming this is a unique id given to a message?
        self.message_id = None
        #the id of the match?
        self.match_id = None
        #who the message was to?
        self.recipient = None
        #the sender of the message?
        self.sender = None
        #the sent date
        self.sent_date = None
        #the created date
        self.created_date = None
        #timestamp
        self.timestamp = None





