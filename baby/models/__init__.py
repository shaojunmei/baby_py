# coding: UTF-8

from baby.models.hospital_model import *
from baby.models.baby_model import Baby
from baby.models.feature_model import *

from baby.models.database import db
from baby.models.database import Base, engine
# todo-lyw 如何实现更好的包导入规则，init里面的导入无法事项相对路径，这个文件 <-
# -> 夹里面的包可以使用.导入不能使用..导入，这个如何处理
#
# if __name__ == '__main__':
#     Base.metadata.create_all(engine)  #