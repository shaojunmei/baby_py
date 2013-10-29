# coding: UTF-8

from flask.ext import restful
from flask.ext.restful import reqparse

from baby.util.others import pickler, time_diff, success_dic, fail_dic

from ..services.baby_service import baby_collect_list, baby_list


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


class BabyCollect(restful.Resource):
    """
        婴儿收藏列表
    """
    @staticmethod
    def get():
        """
            所需参数：
                doctor_id：登录医生id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('doctor_id', type=str, required=True, help=u'登录医生id')
        parser.add_argument('page', type=str, required=True, help=u'分页，传入当前page页码')

        args = parser.parse_args()
        doctor_id = args['doctor_id']
        page = args['page']
        resp_suc = success_dic().dic
        resp_fail = fail_dic().dic
        resp_suc['baby_list'] = []
        baby_collect = baby_collect_list(page, doctor_id)
        if baby_collect:
            if type(baby_collect) is list:
                for baby_c in baby_collect:
                    format_baby(baby_c, resp_suc)
            else:
                format_baby(baby_collect, resp_suc)
            return resp_suc
        else:
            return resp_fail

