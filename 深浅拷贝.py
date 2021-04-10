# -*- coding = utf-8 -*-
# @Time : 2021/4/2 1:32
# @Author : 郭庭宇
# @File : 深浅拷贝.py
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

    # Tmp = []
    # for i in Element:
    #     Tmp.append(i)
    # CopyList.append(Tmp)


if __name__ == "__main__":
    list1 = [1, [11, 22], {"a": 3}]
    # ret = '{}'.format(type(list1))
    # print(ret)

    #print(str(type(list1)) == "<class 'list'>")
    '''
    #  浅拷贝
    list2 = list1.copy()
    print(id(list1),id(list2))
    list1[0] = 2
    print(list1[0],list2[0])
    list1[1][0] = 22
    list1[1][1] = 33
    print(list1[1],list2[1])
    '''

    #深拷贝
    # list2 = MyDeepcopy(list1)
    # # print(id(list1), id(list2))
    # list1[0] = 2
    # print(list1[0], list2[0])
    #
    # list1[1][0] = 22
    # list1[1][1] = 33
    # print(list1[1], list2[1])
    #
    # list1[2]["a"] = 4
    # print(list1[2], list2[2])
    #
    # print(list1,list2)

    direc = {"123": 2, "234": 3}
    direc2 = MyDeepcopy(direc)

    direc['123'] = 3
    print(direc)
    print(direc2)




























