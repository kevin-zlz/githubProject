# python运算符与逻辑结构

1. 赋值运算符

    1. 常用函数

        * eval()用来执行括号内部python表达式，例如

        ```
            rex = '12+3.5'
            rex = 'print("hello world")'
            eval(rex)
        ```

        * float()函数

        ```
            f = 3.1485
            f_f = float('%2.2f' % f)
            print(f_f)//输出结果3.15，保留两位小数
        ```

        * round()函数,四舍五入

        ```
            f_2 = round(f, 2)
            print(f_2)//输出结果3.15，保留两位小数
        ```

    2. 赋值运算符

        * 多变量同时赋值，将字符串拆分开给每个变量，多一个少一个都不行

        ```
            a, b, c, d = 'spam'
            print(a)//a='s',b='p',c='a',d='m'
        ```

        * 匹配赋值，*表示剩余值

        ```
            x,*y = 'spam'
            print(x)//x='s'
            print(y)//y='pam'
        ```

    3. 算术运算符，/除，//整除(向下取整)，int()去掉小数位,round()四舍五入取整,%取余,**幂运算

        ```
            m=-12.7
            n=2
            res1=m/n
            res2=m//n
            res3=int(m)
            res4=round(m)
            print(res1)//-6.35
            print(res2)//-7.0
            print(res3)//-12
            print(res4)//-13
            print(3**3)//27
        ```

    4. 注意：python没有自增自减运算符

    5. 算术运算符的运用的小示例秒转化为时间

        ```
            second=float(input('请输入秒'))
            hour=second//3600
            minute=second%3600//60
            sec=second%60
            print('%d小时%d分钟%d秒'%(hour,minute,sec))
        ```
    6. 关系运算符,>,<,<=,>=,==,!=,<>

    7. 逻辑运算符，or ,and ,not, 1<=a<=5也能表示a>=1 and a<=5，短路原则

        ```
            a=12
            res=False and a<5
            res1=True or a>100
            print(res1)
        ```

    8. 成员运算符in ,not in,后面一定接的是集合

        ```
            name='python'
            res='py' in name
            res1='na' not in name
            print(res1)//False
        ```

    9. 身份运算符,is不仅比较类型还要比较值，==只比较值，is not

        ```
            num1=12
            num2=12.0
            res1=num1 is num2
            res2=num1==num2
            print(res1)//False
            print(res2)//True
        ```

    10. 短路原则应用

        ```
            # 0,空字符串都是False，非0，非空字符串为True
            str='hello'
            str and print(str)
            # 默认值用法
            n=''
            name=n or 'python'
            print(name)
        ```

2. 循环分支结构

    1. while循环，注意要点，当条件满足时执行循环体中语句，不满足时执行else语句中内容

        ```
            i=1
            total=0
            while i<=100:
                total=total+i
                i += 1
            else:
                print(total)
        ```

    2. 嵌套循环，

        ```
        i=0
        while i<10:
            j=0
            while j<10:
                print('*',end=' ')
                j+=1
            print()
            i+=1
        ```

    3. for in循环（遍历）,in后面的变量一定是集合,range()第一个参数起始值，第二个参数是终止值，第三个参数是步长,字符串可以连乘

        ```
            s='fhjfghjhg'
            c=s*3
            for i in range(0,100,2):
                print(i)
            print(len(s))
        ```