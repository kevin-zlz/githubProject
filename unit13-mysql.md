#unit5 mysql
1. 安装

	MySQLdb 只适用于python2.x，它在py3的替代品是： import pymysql
	
		pip install pymysql
	
	>而Django默认的还是使用 MySQLdb :执行会报： ImportError: No module named 'MySQLdb'
	解决：

	在站点的 __init__.py 文件中添加

		import pymysql
		pymysql.install_as_MySQLdb()
2. 创建数据库

		import pymysql  # 1.导入pymysql包

		db = pymysql.connect(host='localhost', user='root',
		    password='12345678',port=3306)  # 2.声明一个MySQL连接对象db,在远程host传入其公网ip
		cursor =db.cursor()  # 3.获得操作游标
		cursor.execute('SELECT VERSION()')  # 4.通过游标进行操作,execute()执行sql语句
		data = cursor.fetchone()  # 获得第一条数据
		print('Database version:', data)
		cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8") # 创建数据库,默认utf-8编码
		db.close()  # 5.关闭连接

2. 新建表

		try:
		    db = None
		    db = pymysql.connect(host='localhost', user='root',
		                         password='12345678', port=3306, db='spiders')  # 2.声明一个MySQL连接对象db,在远程host传入其公网ip
		    cursor = db.cursor()
		    sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,' \
		          ' name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
		    cursor.execute(sql)
		except Exception as ex:
		    print(ex)
		finally:
		    if db:
		        db.close()

3. 事务

	1. 原子性
	2. 一致性
	3. 隔离性

			try:
			    cursor.execute(sql)
			    cursor.commit()  # 提交,数据才被真正写到了数据库中
			except:
		   	 	db.rollback()  # 回滚操作,相当与没有进行操作
4. 插入数据
	4. 持久性

		data = {
		    'id': '2012001',
		    'name': 'Bob',
		    'age': 20
		}
		table = 'students'
		keys = ','.join(data.keys())
		values = ', '.join(['%s'] * len(data))
		sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
		try:
		    db = None
		    db = pymysql.connect(host='localhost', user='root',
		                         password='12345678', port=3306, db='spiders')  # 2.声明一个MySQL连接对象db,在远程host传入其公网ip
		    cursor = db.cursor()
		    if cursor.execute(sql, tuple(data.values())):
		        print('Successful')
		        db.commit()
		except:
		    print('Failed')
		    db.rollback()
		finally:
		    db.close()
	
	**注意 对于多个条件的情况，也可以使用下面的格式。但是不要忘记{0} 外面的单引号**
		
		sql = "insert into user(telephone,password,email,city_id) values('{0}','{1}','{2}','{3}')".format(id,password,email,city_id)

		
		
	不应该
		 
		sql = "insert into user(telephone,password,email,city_id) values({0},{1},{2},{3})"                            
	插入多条语句
		
		cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])
		
	
	**对于自动增长列，要获取值**
	
		 id=connect.insert_id()
		        
   		 print(connect.affected_rows()) 
4. 更新操作

		import pymysql
		try:
		    connect = None
		    connect = pymysql.connect(host='localhost', user='root',
		                         password='12345678', port=3306, db='jobapp')  # 2.声明一个MySQL连接对象db,在远程host传入其公网ip
		    cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
		    sql = "update user set city_id='19' where telephone={0}".format('15810001000')
		    result=cursor.execute(sql)
		    print(result)
		
		    connect.commit()
		
		except Exception as ex:
		    connect.rollback()
		finally:
		    if connect:
		        connect.close()
		        cursor.close()
5. 删除操作
3. 查询

		db = pymysql.connect(host='localhost', user='root',
		    password='12345678',port=3306,db='school')  # 2.声明一个MySQL连接对象db,在远程host传入其公网ip
		cursor =db.cursor()  # 3.获得操作游标
		sql='select * from user where name="{0}"'.format('tom')
		cursor.execute(sql)
		print(cursor)
		print('Count:', cursor.rowcount)  # rowcount属性获取查询结果的条数
		# 获取第一行数据
		one = cursor.fetchone()  # fetchone()方法，这个方法可以获取结果的第一条数据，返回结果是元组形式
		print('One:', one)
		# 获取前n行数据
		# row_2 = cursor.fetchmany(3)
		# 获取所有数据
		results = cursor.fetchall()  # fetchall()方法返回的是偏移指针指向的数据一直到结束的所有数据
		for uu in results:
		    print(uu)
		db.close()  # 5.关闭连接
		
	**注：在fetch数据时按照顺序进行，可以使用cursor.scroll(num,mode)来移动游标位置，**如：

	cursor.scroll(1,mode='relative')  # 相对当前位置移动 +1表示向后移动一条，-1表示向上移动一条
	
	cursor.scroll(2,mode='absolute') # 相对绝对位置移动
	
	关于默认获取的数据是元祖类型，如果想要或者字典类型的数据，即：
	
		cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
		

5. 调用存储过程


		sql="call getUsersByCity('石家庄市',@res)"  
		cursor.execute(sql)                     
		print('结果是'+str(cursor.fetchone()))     