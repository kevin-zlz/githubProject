# List 与str常见函数

1. String

    ||string
    |---|---
    find()|返回找到元素的第一个索引值
    replace('')|替换指定区间字符串
    split()|以指定字符分割割字符串
    join()|字符串连接
    isdigit()|字符串是否是纯数字
    isalpha()|是否都是字母
    isalnum()|是否是字母或者数字
    strip()|去掉左右空格
    upper()|全部大写
    lower()|全部小写
    encode('utf-8')|按指定编码格式编码
    decode('utf-8')|按指定编码格式解码

2. List与String公共方法


    ||List|String
    |---|---|---
    len()|返回数组长度|返回字符串长度
    count()|返回元素出现频率|返回字符串出现频率
    index()|返回元素索引值，若不存在会出错|返回元素索引值，若不存在会出错

3. List

    ||List
    |---|---
    reverse()|反转改变数组本身的顺序
    sort()|排序
    sum()|对元素均为数值类型的进行求和
    max()|对元素均为数值类型的进行求最大值
    min()|对元素均为数值类型的进行求最小值
    append()|list末尾追加list元素
    appendleft()|list头部追加list元素
    extend()|list末尾追加数组
    insert()|数组指定索引插入元素
    remove()|删除单个元素
    del friuts[1:3]|删除多个元素
    pop()|删除末尾元素
    popleft()|删除头部元素
    clear()|清空所有元素

4. Tuple

    * Tuple是不可修改类型，没有增删改的方法只有查的方法支持切片，其他方法和数组类似，若元素为数值类型则有sum(),max(),min()等方法

    * Tuple与string的转换

    ```
        s='hello'
        s_t=tuple(s)#字符串转化为tuple
        t_s=str(s_t)
        ''.join(t_s)#tuple转化为字符串
    ```

    * Tuple与list的转换

    ```
        list1=[1,2,3,4]
        t_l=tuple(list1)#数组转化为Tuple
        l_t=list(t_l)#Tuple转化为数组
    ```

3.  Set

    * set集合，无序且不重复，可哈希的值，集合成员可以做字典里面的键，可修改类型,set不支持索引下角标，没有index()方法，不可以用切片

    ||set
    |---|---
    |add(value)|添加元素
    |clear()|清空集合元素
    |copy()|复制set集合
    |discard(value)|移除元素，移除不存在的数据不会报错
    |remove(value)|移除元素，移除不存在的会报错
    |pop()|移除末尾元素
    |intersection(set1)|取交集，返回set集合，不改变原集合
    |intersection_update(set1)|取交集，无返回值，改变原set
    |union(set1)|取并集，返回set类型，不改变原set
    |symmetric_difference(set1)|返回set，合并不同项
    |b1.issubset(s1)|b1是否是s1的子集
    |b1.isdisjoint(s1)|b1是否与s1有交集
    |b1.issuperset(s1)|b1是否是s1的父集

    * set集合的初始化

    ```
        set1=set()# 空集合
    ```

5. Dict

    * 字典，键值对,可变类型

    * 字典初始化

    ```
        uu={}   # 空字典
        uu['title']='python' # 添加键值对
        uu['score']=90
    ```
    >注意set与dict的区别

    * 字典访问，不支持索引，不支持切片

    ```
        user={"name":"tom","age":12,"address":"苏州"}
        print(user['name'])
    ```

    *  字典删除键值对

    ```
        del uu['title']
        uu.clear()  # 清除所有数据
        uu.pop('title')  # 清除指定键对应的值
        uu.popitem()    # 随机返回并删除字典一对键值对
    ```

    * 字典可以单独访问键或值

    ```
        print(user.values())
        for k,v in user1.items():
            print(k,v)
        for k in sorted(user.keys()):
            print(k)
    ```

    * 键值对可以是数值，可以是字符串，可以是数组，集合，字典

3. list,str,set,tuple,dict区别与联系

    1. list,dict，set是可修改类型,都有自己对应的增删改方法

    ```
        list1=[]
        set1=set()
        dict1={}

        # 增加方法
        list1.append(value) # list 尾部追加元素
        list1.appendleft(value) # list 头部追加元素
        list1.insert(0,value) # list 指定位置插入元素
        list1.extend(list2) # list 追加list
        set1.add(value) # set添加元素
        dict1['name']='jack' # dict 添加键值对

        # 删除
        list1.remove(value) # 如果删除不存在会报错
        del list1[1:3]
        list1.pop() #删除末尾元素
        list1.popleft() # 删除头部位置
        list1.clear() # 清空数组
        set1.remove(value) # 删除指定元素
        set1.pop()  # 删除末尾元素
        set1.discard(value) # 不会报错
        set1.clear() # 清空集合
        dict1.pop('name')   # 删除name键值对
        dict1.clear() # 清空字典
        dict1.popitem() # 随机删除一个键值对
        del dict1['name']   # 删除name键值对
    ```

    3. str,tuple不可修改类型，没有常规删除修改增加方法








