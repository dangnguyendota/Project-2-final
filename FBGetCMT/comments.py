import requests

class comment:
    def __init__(self, user_id, post_id, access_token, graph_api_version='v2.9'):
        self.__url = 'https://graph.facebook.com/{}/{}_{}/comments'.format(graph_api_version, user_id, post_id)
        self.__r = requests.get(self.__url, params={'access_token': access_token})
        self.__comments = []
        while True:
            __data = self.__r.json()

            if 'error' in __data:
                raise Exception(__data['error']['message'])

            for __comment in __data['data']:
                self.__comments.append({'created_time':__comment['created_time'], 'id':__comment['id'].split('_')[1], 'message':__comment['message']})

            if 'paging' in __data and 'next' in __data['paging']:
                self.__r = requests.get(__data['paging']['next'])
            else:
                break
    def get_all(self):
        return self.__comments

    def get_comments(self):
        result = []
        for i in self.__comments:
            result.append(i['message'])
        return result

    def get_id(self):
        result = []
        for i in self.__comments:
            result.append(i['id'])
        return result

    def get_create_time(self):
        result = []
        for i in self.__comments:
            result.append(i['created_time'])
        return result

