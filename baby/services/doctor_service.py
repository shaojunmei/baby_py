# coding: UTF-8

from ..models.hospital_model import Doctor


def doctor_info(doctor_id):
    """
        获得医生个人资料
            doctor_id: 医生的id
    """
    doctor = Doctor.query.filter(Doctor.id == doctor_id).first()
    return doctor