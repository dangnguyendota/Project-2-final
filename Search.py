import requests


def getUrl(document_name, q):
    return "http://localhost:8983/solr/{}/select?q={}&rows=1000&start=0".format(document_name, q)


document_name = "project2_test"
comment_search = "trường"
post_search = "mediolas"
sentiment = "false"
q = ["positive_cmt:" + sentiment, "comment:" + comment_search.replace(' ', '%20').replace("\n", '%20'),
     'post_message:' + post_search.replace(' ', '%20').replace("\n", '%20')]

r = requests.get(getUrl(document_name, q[1]))
result = r.json()
for i in result['response']['docs']:
    try:
        print(i['comment'])
    except:
        print("None")
    print(i['comment_score'])
    print('-------------------------------------------------------------------------')
