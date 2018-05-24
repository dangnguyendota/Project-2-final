import os
import json
import urllib
import pprint

# get Facebook access token from environment variable
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

# build the URL for the API endpoint
host = "https://graph.facebook.com"
path = "/me"
params = urllib.urlencode({"access_token": ACCESS_TOKEN})

url = "{host}{path}?{params}".format(host=host, path=path, params=params)

# open the URL and read the response
resp = urllib.urlopen(url).read()

# convert the returned JSON string to a Python datatype
me = json.loads(resp)

# display the result
pprint.pprint(me)