# coding: UTF-8

from ..models.baby_model import Baby
from ..models.feature_model import Collect
from ..util.seesion_query import *
from ..util.others import page_utils


def baby_list(page):
    """
        全部婴儿列表
    """
    baby_count = Baby.query.filter().count()
    page, per_page = page_utils(baby_count, page)
    if baby_count > 1:
        babys = Baby.query.filter()[per_page*(page-1):per_page*page]
        return babys
    else:
        baby = Baby.query.filter().first()
        return baby


def baby_collect_list(page, doctor_id):
    """
        得到医生收藏婴儿列表
            page: 分页，当前页
            doctor_id: 医生的id
    """
    result_count = session.query(Baby). \
        filter(Collect.doctor_id == doctor_id, Collect.type == 'baby').count()
    page, per_page = page_utils(result_count, page)
    if result_count > 1:
        results = session.query(Baby).\
            filter(Collect.doctor_id == doctor_id, Collect.type == 'baby')[per_page*(page-1):per_page*page]
        return results
    else:
        result = session.query(Baby).\
            filter(Collect.doctor_id == doctor_id, Collect.type == 'baby').first()
        return result