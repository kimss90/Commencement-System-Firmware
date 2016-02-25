"""
texter.py
"""
import json
import pprint as pp

import requests


class Texter:
    """
    Class for sending SMS through my Flask-Twilio page
    """

    def __init__(self, url='http://adb-sms.herokuapp.com/', key=None, message=None):
        self.url = url
        self.message = message
        self.key = key

    def __str__(self):
        return pp.pformat({
            'url': self.url,
            'current default message': self.message,
            'key': '*' * len(self.key) if self.key else None
        }, indent=4)

    def __repr__(self):
        return 'mymods.texter.Texter() object:\n' + self.__str__()

    def send(self, message=None):
        """
        Send the message off
        """
        # State checking
        if not self.url:
            raise RuntimeError('No target URL set.')
        if not message:
            if not self.message:
                print 'WARNING: No message string detected.'
            else:
                message = self.message

        # Send data
        res = requests.post(self.url, data=json.dumps({
            'message': message,
            'key': self.key
        }))

        # Handle response
        if res.status_code != 200:
            print "Received not 'OK' status code"
        else:
            print 'Sent'
        return res
