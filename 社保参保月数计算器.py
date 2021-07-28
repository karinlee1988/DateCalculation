#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/7/28 22:49
# @Author : karinlee
# @FileName : 社保参保月数计算器.py
# @Software : PyCharm
# @Blog : https://blog.csdn.net/weixin_43972976
# @github : https://github.com/karinlee1988/
# @gitee : https://gitee.com/karinlee/
# @Personal website : https://karinlee.cn/

import PySimpleGUI as sg
from date_calculation import get_string_sub_date_month

class CalculationOfMonths(object):
    """
    计算器可视化界面
    """
    def __init__(self):
        # 设置pysimplegui主题，不设置的话就用默认主题
        sg.ChangeLookAndFeel('Purple')
        # 定义2个常量，供下面的layout直接调用，就不用一个个元素来调字体了
        # 字体和字体大小
        self.FONT = ("微软雅黑", 16)
        # 可视化界面上元素的大小
        self.SIZE = (10,1)
        # 界面布局
        self.layout = [
            [sg.Text('  社保参保月数计算器by英德关系李加林',font=("微软雅黑", 12))],
            [sg.Text('******************************', font=self.FONT)],
            # sg.Image()插入图片，支持gif和png
            [sg.Image(filename="images/peppa.png")],
            # sg.Text()显示文本
            [sg.Text('',font=self.FONT,size=self.SIZE)],
            # sg.Input()是输入框
            [sg.Text('   （日期格式：YYYYMM）', font=self.FONT, size=(20,1))],
            [sg.Text('', font=self.FONT, size=self.SIZE)],
            [sg.Text('日期1   ->',font=self.FONT,size=self.SIZE), sg.Input(key='_DATE1_',font=self.FONT,size=self.SIZE)],
            [sg.Text('日期2   ->',font=self.FONT,size=self.SIZE), sg.Input(key='_DATE2_',font=self.FONT,size=self.SIZE)],
            [sg.Text('参保月数   <-', font=self.FONT, size=self.SIZE), sg.Input(key='_VALUE_', font=self.FONT, size=self.SIZE,readonly=True)],
            [sg.Text('')],
            [sg.Btn('开始计算', key='_SUMMIT_', font=("微软雅黑", 16), size=(23, 2))],
        ]
        # 创建窗口，引入布局，并进行初始化
        # 创建时，必须要有一个名称，这个名称会显示在窗口上
        self.window = sg.Window('社保参保月数计算器', layout=self.layout, finalize=True)


    # 窗口持久化
    def run(self):
        # 创建一个事件循环，否则窗口运行一次就会被关闭
        while True:
            # 监控窗口情况
            event, value = self.window.Read()
            # 当获取到事件时，处理逻辑（按钮绑定事件，点击按钮即触发事件）
            if event == '_SUMMIT_':
                date1 = value['_DATE1_']
                date2 = value['_DATE2_']
                result = get_string_sub_date_month(date1,date2)
                # 将变量result的值更新至窗口相应元素上
                self.window.Element("_VALUE_").Update(result)
            # 如果事件的值为 None，表示点击了右上角的关闭按钮，则会退出窗口循环
            if event is None:
                break
        self.window.close()

if __name__ == '__main__':
    app = CalculationOfMonths()
    app.run()