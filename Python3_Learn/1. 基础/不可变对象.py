#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
str是不变对象，而list是可变对象。
对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
'''

# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
a = ['c', 'b', 'a']
a.sort()
print(a)

# 而对于不可变对象，比如str，对str进行操作呢：
a = 'abc'
b = a.replace('a', 'A')
print("id(a)：", id(a), "id(b)：", id(b))
'''
当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，
而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，
变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了
'''


