# 字符串以及List数组

1. 字符串输出及内部函数
    1. 字符串输出

    ```
        print('%20s'%'hello')#右对齐20占位符
        print('%-20s'%'hello')#左对齐20占位符
    ```

    2. 字符串格式输出

    ```
        ame='tom'
        age=20
        print('i am {0},and i am {1} years old'.format(name,age))
        print('i am {0:10s},and i am {1} years old'.format(name,age))
    ```

    3. 字符串常用内部函数

        * count()方法测算字符串出现的频率，如果存在返回值是正整数（出现的次数），不存在则返回0

        ```
            s1='hello nihao hello welcom'
            print(s1.count('o'))#4
        ```

        * find()检测字符串是否存在，存在返回所在索引值，否则返回-1

        ```
            s2=s1.find('hello',1,5)   # 起始值，终止值
            print(s2) #-1
        ```

        * replace()替换部分字符串

        ```
            s3=s1.replace('hello','hi',2)   # 替换次数
            print(s3)   # hi nihao hi welcom
        ```

        * split()字符串截断

        ```
            date='2018-4-15'
            times=date.split('-')
            print(times)    # ['2018', '4', '15']
        ```

        * join()字符串连接

        ```
            s4='python'
            s5='-'
            s6=s5.join(s4)
            print(s6)   #   p-y-t-h-o-n
        ```

        * isdigit()是否是纯数字,isalpha()是否都是字母,isalnum()是否是字母或者数字

        ```
            s1='abc'
            print(s1.isdigit()) # False
            print(s1.isalpha()) # True
            print(s1.isalnum()) # False
        ```

        * 判断字符串是否有字母数字下划线组成

        ```
            pwd='jiji_123'
            flag=True
            for i in pwd:
                if not (i.isalnum() or i=='_'):
                    flag=False
            print(flag) # True
        ```

        * upper(),lower(),s1.strip()去掉左右空格rstrip()右边空格,lstrip()左边空格

        * 查看帮助

        ```
            print(dir(s1))
        ```

        * 字符串编码

        ```
            ss_en=s1.encode('utf-8')  # 字节码
            ss_de=ss_en.decode('utf-8')
        ```

    4. 存放文档内容变量__doc__

    ```
    '''
    这是文档内容，只能放在文档开头
    '''
    print(__doc__)  #输出文档内容
    ```

    5. 切片

        * 数字，字符串，元祖不可变性(不可修改),存储空间内容不会更改

        * 切片 起始位置索引：终止位置索引，不包括终止位置

        ```
            s2="abcdefghijk"
            c=s2[1:3]
            c1=s2[-3:-1]
            c2=s2[-2:]
            c3=s2[-6:-2]
            print(c)    # bc
            print(c1)   # ij
            print(c2)   # jk
            print(c3)   # fgji
        ```

        * 字符串长度len()

        ```
            l=len(s2)
            print(s2[l-1])  # K
            a='ab'
            b='ab'
            print(a is b)
        ```
        >python机制,a,b会指向同一块空间，里面存储这'ab',每次赋值系统都会寻找一遍有没有所要赋的值，有的话不会再开辟新的空间

        * 跳跃切片,参数是步长

        ```
            print(s2[-3:2:-1])
            print(s2[::-1])
            print(s2[::-2])
        ```

        * 所有的奇数个

        ```
            print(s2[1::2])
        ```

        * 判断用户名是否都是小写字母

        ```
        if len(userid)==6:
            for i in userid:
                if not ('0'<=i<='9'):
                    print('含有非法字符')
                    break
            else:
                print('yes')
        else:
            print('长度不是六位')
        ```

        * 长句简写

        ```
        content='这条语句太长了，预知后事如何请听下回分解，话说从前'
        con=content if len(content)<=20 else content[0:20]+'...'
        print(con)
        ```

        * 连接符

        ```
            s1='py'
            s2='thon'
            s3=s1*5
            s4=s1+s2
            print(s3)
            print(s4)
        ```

2. List数组

    * List 数据项不需要相同的数据类型,内容可变

    ```
        arr3=[]
        arr2=[1,2,3,'a']
        print(len(arr2))    # 4
        arr2[2]='java'
        print(arr2) # [1, 2, 'java', 'a']
    ```

    * 遍历List

    ```
        for i in arr2:
        print(i,end='  ')
    ```

    * 改变数组

    ```
        arr1=[1,2,3]
        for i in range(len(arr1)):
            arr1[i]=arr1[i]*2
        print(arr1)
    ```

    * index()查询子串所在索引值

    ```
        fruits=['asas','sqwq','dadad']
        print(fruits.index('banana'))
    ```

    * 反转改变数组本身的顺序

    ```
        fruits.reverse()
        print(fruits)
    ```

    * sort()排序

    ```
        fruits.sort()
        print(fruits)
    ```








