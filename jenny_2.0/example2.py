import logging
import requests

logging.basicConfig(filename='example2.log',level=logging.DEBUG)

logging.debug('Attempting to connect to Google')
requests.request("GET", "https://www.google.com/")

logging.debug('Attempting to connect to Twilio API')
requests.request("GET", "https://api.twilio.com/")

logging.debug('Done....')