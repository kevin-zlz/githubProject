# 函数

1. 函数包括def、函数名、函数体、参数、返回值

2. 空函数

    ```
        def nop():
        pass
    ```

3. 函数参数，函数参数包括必选参数、默认参数、可变参数、命名关键字参数和关键字参数

    * 必备参数,不允许重名函数，参数必须和形参数目一致，没有函数重载

    ```
        def show(name,age):
            print('name:',name,'age:',age)
        show('zlz',22) # name:zlz age:22
    ```

    * 默认参数,可有可无,,必选参数在前，默认参数在后,默认参数必须指向不可变对象

    ```
        def show1(name,age,nation='china'):
        print('name:',name,'age:',age,'nation:',nation)
        show1('zlz',22) #name:zlz age:22 naion:china
        show1('zlz',22,'usa') #name:zlz age:22 naion:usa
    ```

    * 不定长参数,可以写多个参数，0~n个,args是元组类型

    ```
        def show2(name,age,*args):
            print('name:', name, 'age:', age) # name: tom age:12
            print(args)  # ('abc','ed')
        show2('tom',12,'abc','ed')
    ```

    * 关键字参数,other类型是字典类型,other 可缺省,除了必选参数外你可以输入任意个含参数名的参数,这些关键字参数自动组装成一个dict

    ```
        def add3(m,n,*args,**other):
            print(args)
            print(other)
        kw={'city':'suzhou','sex':'man'}
        add3(1,2,3,4,**kw)
        add3(1,2,3,4)
    ```

    * 命名关键字参数,不可缺省,限制关键字参数的名字,命名关键字参数需要一个特殊分隔符，*后面的参数被视为命名关键字参数。

    ```
        def person(name,age,*,city,job):
            print(age,name,city,job)
        person('rose',21,city='suzhou',job='chengxuyyuan')
    ```

3. 函数能够返回多个参数

    ```
        def func(a,b,c):
            m=a+b+c
            n=a*b*c
            return m,n
        res01=func(1,2,3) # 实质res01是一个元组类型
        res02,res03=func(1,2,3)
    ```

3. 访问函数内部函数方法

    ```
        def out():
            print('out')
            def a():
                print('in')
        return a
        out()() # out in
    ```

4. lambda匿名函数，仅用于简单逻辑

    ```
        func_b=lambda  s:print('this is lambda',s)
        func_b('py')
    ```

5. lambda函数与map()函数的混搭

    ```
        arr=[21,3,6,9,7,8]
        arr2=map(lambda  s:s*2 if s%2==0 else s,arr)
        print(list(arr2))
    ```

6. 变量的作用域

    * 循环语句没有作用域，函数有作用域函数内部变量是局部变量，外部无法访问，作用域链：访问不可修改，先找自己的作用域，再找外部函数，直至找到全局作用域

    ```
        a=2
        def func_out():
            a=1
            # a=a+1 如果这样用会出错，要使用外面的a必须使用 global a
            print(a)
        func_out()
        print(a)
    ```


