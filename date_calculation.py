#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/28 21:12
# @Author : karinlee
# @FileName : date_calculation.py
# @Software : PyCharm
# @Blog : https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/
# @Personal website : https://karinlee.cn/

import datetime

def get_string_sub_date_month(date1:str, date2:str) -> str:
    """
    计算两个日期之间的社保缴费月数(日期为6位字符串格式yyyymm)
    :param date1: 日期1
    :param date2: 日期2
    :return: 社保缴费月数
    """
    try:
        if int(date1) > int(date2):
            date1,date2 = date2,date1
        year1 = datetime.datetime.strptime(date1, "%Y%m").year
        year2 = datetime.datetime.strptime(date2, "%Y%m").year
        month1 = datetime.datetime.strptime(date1, "%Y%m").month
        month2 = datetime.datetime.strptime(date2, "%Y%m").month
        months = (year2 - year1) * 12 + (month2 - month1) + 1
        return str(months)
    except ValueError:
        return 'ERROR'

if __name__ == '__main__':
    print(get_string_sub_date_month('201512','201412'))