# coding: UTF-8

from flask.ext import restful
from flask.ext.restful import reqparse
from baby.models.baby_model import *
from baby.util.others import *


def format_baby(baby, resp_suc):
    """
        格式化baby对象
    """
    baby_pic = pickler.flatten(baby)
    baby_pic['picture_path'] = baby.rel_path + baby.picture_name
    baby_birthday = baby.born_birthday
    baby_pic['time'] = time_diff(baby_birthday)
    resp_suc['baby_list'].append(baby_pic)


class BabyList(restful.Resource):
    """
        婴儿列表
    """
    @staticmethod
    def get():
        """
            所需参数：
                page: 分页，传入当前页码
                type：1列表，0收藏
        """
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=str, help=u'分页page，传入当前页')

        args = parser.parse_args()
        page = args['page']

        resp_suc = success_dic().dic
        resp_fail = fail_dic().dic
        resp_suc['baby_list'] = []
        baby = baby_list(page)
        if baby:
            if type(baby) is list:
                for bb in baby:
                    format_baby(bb, resp_suc)
            else:
                format_baby(baby, resp_suc)
            return resp_suc
        else:
            return resp_fail
