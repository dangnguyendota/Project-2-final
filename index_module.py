from FBGetCMT.comments import *
from FBGetCMT.posts import *
from VNAnalysis import PosTagger
import os
import json


def index(token, user, path, core_name, limit=1, master=None):
    with open(os.path.join(path, 'comments.json'), 'r') as jsonData:
        try:
            data = json.load(jsonData)
        except ValueError:
            data = []
    tmp_post = post(token, user, limit)
    t = tmp_post.get_all()
    result = []
    for i in t:
        id = i['id'].split('_')
        tmp_comment = comment(id[0], id[1], token)
        c = tmp_comment.get_all()
        for j in c:
            __id = t[0]['id'].split('_')[0] + "-" + id[1] + "-" + j['id']
            __link = "https://www.facebook.com/{}".format(__id.replace("-", "_"))
            if not __existed(__id, data):
                print("Find a new comment!")
                tmp_1 = __encrypt(PosTagger.getScore(j['message']))
                tmp = {'page_id': t[0]['id'].split('_')[0], "post_id": id[1], "comment_id": j['id'],
                       'id': __id, "post_created_time": i['created_time'],
                       "comment_created_time": j['created_time'],
                       "post_message": i['message'], "comment": j['message'], "comment_score": tmp_1[0],
                       "positive_cmt": tmp_1[1], "link_cmt": __link}
                result.append(tmp)
                for tmpx in tmp:
                    print(tmpx + ":" + str(tmp[tmpx]))
                print("-----------------------------------------------------------------------------------------------")
                # __findNewComment(master, page_id=tmp['page_id'], post_id=tmp["post_id"], comment_id=tmp["comment_id"],
                #     post_created_time=tmp["post_created_time"],
                #   comment_created_time=tmp["comment_created_time"],
                #  post_message=tmp["post_message"], comment=tmp["comment"])
    result = data + result
    with open('{}\comments.json'.format(path), 'w', encoding='utf-8') as outfile:
        json.dump(result, outfile, indent=4)
    os.system(
        "java -jar -Dc={} -Dauto E:\solr-7.2.1\example\exampledocs\post.jar {}\comments.json".format(core_name, path))
    # master.add(message=index_message)


def __encrypt(input_dir):
    try:
        tmp = (input_dir['Surprise'] + input_dir['Joy'] + input_dir['Positive'] + input_dir['Anticipation'] - input_dir[
            'Sadness'] - input_dir['Negative'] - input_dir['Fear'] + input_dir['Trust'] - input_dir['Disgust'] -
               input_dir['Anger']) / input_dir['Sum']
    except:
        tmp = 0
    return [tmp, tmp >= 0]


def __existed(current_data, data_list):
    for i in data_list:
        if current_data == i['id']:
            return True
    return False


def __findNewComment(master=None, **kwargs):
    if not master:
        print("find a new comment")
    else:
        tmp = {}
        for kwarg in kwargs:
            tmp[kwarg] = kwargs[kwarg]
        master.add(message='new comment found! ' + kwargs['id'], content=tmp)
