#!/usr/bin/python3
# coding: utf-8


import dateutil.parser
import pytz

value = "20170404 "
tz = pytz.timezone('Asia/Shanghai')  # 创建一个时区对象
value = dateutil.parser.parse(value, fuzzy=True)
value = tz.localize(value)  # 设定timezone
print(value)
value = value.astimezone(pytz.utc)  # 对于设定了timezone的datetime对象，可以使用astimezone方法将timezone设定为另一个
print(value)

# pytz.all_timezones # 通过pytz模块查看当前全球都有哪些timezone