#-*- coding:utf-8 -*-
import cchardet  # 判断二进制数据是什么编码的

s = '中国'.encode()
s = cchardet.detect(s)
print(s)
