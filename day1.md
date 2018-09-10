# python基础

1. 改变python编码使其支持中文
   在页面的最开头加入一句编码

   ```
       # -*- coding:utf-8 -*-
   ```
2. python编程常见快捷方式

    * Ctrl+d 复制
    * Ctrl+x 删除当前行
    * Ctrl+/ 注释

3. python输入输出控制语句

    1. 输入语句

    ```
        num=input('请输入数字\n')
    ```
    > 注意python语法中没有分号，没有各种括号，用缩进表示语句控制域，缩进最好使用Tab方便统一格式。

    2. 输出语句，输出变量

    ```
        age=12
        print('年龄：',age)
    ```

    3. 带输出类型的输出语句
        * 常见输出类型
        符号|含义|
        ---|---|
        %d|数字占位符
        %s|字符串占位符
        %f|浮点型占位符

        * 个人名片小程序示例：

        ```
            name=input('请输入名字：\n')
            tel=input('请输入电话：\n')
            company=input('请输入公司名称：\n')
            print('===============\n姓    名：%s\n电    话：%s\n公司名称：%s\n==============='%(name,tel,company))
        ```

3. 关键字import常用用法

    ```
        import sys
        print(sys.path)
    ```

4. 赋值操作
    * =表示赋值 从右向左执行

    ```
        num = 12
        num = 3
        # 先开辟一块空间存放12，再让num指向12，再开辟一块空间存放3，让num指向3，再利用回收机制回收12
    ```

    * 多变量同时赋值，注意多一个少一个都不行

    ```
        a, b, c = 1, 2, 'num'
    ```

5. 常见标准数据类型

    * Numbers(int,long,float,complex)

    * String(单双引号均可）

    * bool(True,False)

    * List,Tuple,Dictionary

    * 数据类型转换,int,float,string相互转换,int()取整float()浮点型str(),float不能直接转化为int

    ```
        f = -3.14
        n = int(f)
        print(n)
    ```

    * 输出变量类型type

    ```
        c='abcc'
        print(type(c))
    ```

    * 字符串分片与索引







