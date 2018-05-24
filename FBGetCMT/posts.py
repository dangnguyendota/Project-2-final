import facebook
import json
import requests

class post:
    def __init__(self, my_token, user, limit):
        __graph = facebook.GraphAPI(access_token=my_token)
        self.__profile = __graph.get_object(user)
        __posts = __graph.get_connections(self.__profile['id'], 'posts', limit=5)
        self.__posts = []
        __Jstr = json.dumps(__posts)
        __JDict = json.loads(__Jstr)
        for p in __JDict['data']:
            self.__posts.append({'created_time': p['created_time'], 'id': p['id'], 'message': p['message']})
        __next = __JDict['paging']['next']
        limit -= 1
        while limit != 0:
            __r = requests.get(__next).json()
            for p in __r['data']:
                try:
                    self.__posts.append({'created_time':p['created_time'], 'id':p['id'],'message':p['message']})
                except:
                    try:
                        self.__posts.append({'created_time': p['created_time'], 'id': p['id'], 'message': p['story']})
                    except:
                        self.__posts.append({'created_time': p['created_time'], 'id': p['id'], 'message': "None"})
            if 'paging' in __r and 'next' in __r['paging']:
                __next = __r['paging']['next']
            else:
                break
            limit -= 1
    def get_all(self):
        return self.__posts

    def get_user_id(self):
        return self.__profile['id']

def get_user_id(token, user):
    graph = facebook.GraphAPI(access_token=token)
    profile = graph.get_object(user)
    return profile['id']