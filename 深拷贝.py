# -*- coding = utf-8 -*-
# @Time : 2021/4/2 1:32
# @Author : BlackTeemo
# @File : 深拷贝.py
# @Software: PyCharm
def MyDeepcopy(list):
    if str(type(list)) != "<class 'list'>" and str(type(list)) != "<class 'dict'>":
        print("the list type is {} Please enter type <class 'list'>  ".format(type(list)))
        return 0
    elif str(type(list)) == "<class 'dict'>":
        CopyList = {}
        for Element in list:
            CopyList.update({Element: list[Element]})
        return CopyList
    CopyList = []
    for Element in list:
        if str(type(Element)) != "<class 'list'>" and str(type(Element)) != "<class 'dict'>":
            CopyList.append(Element)
            continue

        CopyList.append(MyDeepcopy(Element))

    return CopyList





























