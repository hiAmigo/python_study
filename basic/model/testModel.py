#!/usr/bin/env python3
# -%- coding: utf-8 -%-

# 上面第一行注释可以让文件直接在Linux/Mac/Unix上运行 第二行说明.py使用utf-8作为编码

'a test model'
# 任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Lee'
#写入作者变量

import sys
#导入sys模块

def test():
    args = sys.argv
    if len(args) == 1：
        print('hello world')
    elif len(args) == 2:
        print('Hello, %s' % args[1])
    else:
        print('Too many arguments')

if __name__ = '__main__':
    test()


