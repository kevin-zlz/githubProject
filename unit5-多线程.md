# 多线程
1. 什么是多线程

	多线程类似于同时执行多个不同程序，多线程运行有如下优点：
	
	* 使用线程可以把占据长时间的程序中的任务放到后台去处理。
	* 用户界面可以更加吸引人，这样比如用户点击了一个按钮去触发某些事件的处理，可以弹出一个进度条来显示处理的进度
	* 程序的运行速度可能加快
	* 在一些等待的任务实现上如用户输入、文件读写和网络收发数据等，线程就比较有用了。在这种情况下我们可以释放一些珍贵的资源如内存占用等等。

	>每个线程都有他自己的一组CPU寄存器，称为线程的上下文，该上下文反映了线程上次运行该线程的CPU寄存器的状态。
指令指针和堆栈指针寄存器是线程上下文中两个最重要的寄存器，线程总是在进程得到上下文中运行的，这些地址都用于标志拥有线程的进程地址空间中的内存。
	
	Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
	
	由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
	
	threading用于提供线程相关的操作，线程是应用程序中工作的最小单元。python当前版本的多线程库没有实现优先级、线程组，线程也不能被停止、暂停、恢复、中断。

	threading模块提供的类：  
	　　Thread, Lock, Rlock, Condition, [Bounded]Semaphore, Event, Timer, local。
	
		
	threading 模块提供的常量：
	
	　　threading.TIMEOUT_MAX 设置threading全局超时时间。
2. 开启线程的两种方式-函数

		import threading
		import time
		#方法一：将要执行的方法作为参数传给Thread的构造方法
		
		def action(arg):
		    time.sleep(1)
		    print(threading.current_thread())
		
		    print('the arg is:{0}'.format(arg))
		
		for i in range(4):
		    t =threading.Thread(target=action,args=(i,))
		    t.start()
		
		if __name__ == '__main__':
		    print(threading.current_thread())
		    print('main thread end!')
3. 开启线程的两种方式-用类来包装线程对象

		class MyThread(threading.Thread):
		    def __init__(self,arg):
		        super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
		        self.arg=arg
		    def run(self):#定义每个线程要运行的函数
		        time.sleep(1)
		        print 'the arg is:%s\r' % self.arg
		
		for i in xrange(4):
		    t =MyThread(i)
		    t.start()
		    
	Thread类
	
	构造方法： 
	* Thread(group=None, target=None, name=None, args=(), kwargs={}) 
	
	* group: 线程组，目前还没有实现，库引用中提示必须是None；
	　　 
	* target: 要执行的方法； 
	　　
	* name: 线程名； 
	　　
	* args/kwargs: 要传入方法的参数。
	
	实例方法： 
	* isAlive(): 返回线程是否在运行。正在运行指启动后、终止前。 
	* get/setName(name): 获取/设置线程名。 
	
	* start():  线程准备就绪，等待CPU调度
	
	
	start(): 启动线程。
	 
	join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。
4. threading 模块提供的常用方法： 
	
	* threading.currentThread(): 返回当前的线程变量。 
	* threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。 
	* threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。


5. 后台线程和前台线程
	
	is/setDaemon(bool): 获取/设置是后台线程（默认前台线程（False））。（在start之前设置）
	
	1. 如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程和后台线程均停止
	
	1. 如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止

	
			if __name__ == '__main__':
			    for i in range(4):
			        t = MyThread(i)
			        t.setDaemon(True)
			        t.start()
			
			    print('main thread end!')
6. join()

	 join()阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout，即使设置了setDeamon（True）主线程依然要等待子线程结束。
	 
	 线程必须先start()然后再join()
	 
	 **错误的做法是**
	 
	 	if __name__ == '__main__':
		    for i in range(4):
		        t = MyThread(i)
		        t.start()
		        t.join()
	>可以看出此时，程序只能顺序执行，每个线程都被上一个线程的join阻塞，使得“多线程”失去了多线程意义。
	
	**☝️这样**
		
		if __name__ == '__main__':
		    th=[]
		    for i in range(4):
		        t = MyThread(i)
		        th.append(t)
		        t.start()
		
		
		    for tt in th:
		        tt.join()
		    #设置join之后，主线程等待子线程全部执行完成后或者子线程超时后，主线程才结束
		    print('main thread end!')
6. 	线程同步-Lock、Rlock类

	由于线程之间随机调度：某线程可能在执行n条后，CPU接着执行其他线程。为了多个线程同时操作一个内存中的资源时不产生混乱，我们使用锁。

	Lock（指令锁）是可用的最低级的同步指令。Lock处于锁定状态时，不被特定的线程拥有。Lock包含两种状态——锁定和非锁定，以及两个基本的方法。

	可以认为Lock有一个锁定池，当线程请求锁定时，将线程至于池中，直到获得锁定后出池。池中的线程处于状态图中的同步阻塞状态。

	RLock（可重入锁）是一个可以被同一个线程请求多次的同步指令。RLock使用了“拥有的线程”和“递归等级”的概念，处于锁定状态时，RLock被某个线程拥有。拥有RLock的线程可以再次调用acquire()，释放锁时需要调用release()相同次数。

	可以认为RLock包含一个锁定池和一个初始值为0的计数器，每次成功调用 acquire()/release()，计数器将+1/-1，为0时锁处于未锁定状态。
	
	实例方法： 
		
	* acquire([timeout]): 尝试获得锁定。使线程进入同步阻塞状态。 
	　　
	* release(): 释放锁。使用前线程必须已获得锁定，否则将抛出异常。

	
		```
		import threading
		import time
		
		
		# 方法一：将要执行的方法作为参数传给Thread的构造方法
		count=0
		lock = threading.RLock()
		def action(arg):
		    lock.acquire()
		    time.sleep(1)
		    global count
		    count+=1
		    
		    print(threading.current_thread())
		    count-=1
		    print('the arg is:{0},count is:{1}'.format(arg,count))
		    lock.release()
		ths=[]
		for i in range(4):
		
		    t =threading.Thread(target=action,args=(i,))
		    # t.setDaemon(True)
		    ths.append(t)
		
		for tt in ths:
		    tt.start()
		
		for tt in ths:
		    tt.join()
		
		if __name__ == '__main__':
		    # print(threading.current_thread())
		    # print(threading.enumerate())
		    # print(threading.activeCount())
		    print('main thread end!')
		```
1. Lock对比Rlock

		import threading
		lock = threading.Lock() #Lock对象
		lock.acquire()
		lock.acquire()  #产生了死锁。
		lock.release()
		lock.release()
		print lock.acquire()
		 
		 
		import threading
		rLock = threading.RLock()  #RLock对象
		rLock.acquire()
		rLock.acquire() #在同一线程内，程序不会堵塞。
		rLock.release()
		rLock.release()
2. Condition类

	Condition（条件变量）通常与一个锁关联。需要在多个Contidion中共享一个锁时，可以传递一个Lock/RLock实例给构造方法，否则它将自己生成一个RLock实例。
	
	可以认为，除了Lock带有的锁定池外，Condition还包含一个等待池，池中的线程处于等待阻塞状态，直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进入锁定池等待锁定。
	
	构造方法： 
	Condition([lock/rlock])
	
	实例方法： 
	
	* acquire([timeout])/release(): 调用关联的锁的相应方法。 
	* wait([timeout]): 调用这个方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。 
	* notify(): 调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池）；其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。 
	* notifyAll(): 调用这个方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。

			# encoding: UTF-8
			import threading
			import time
			
			# 商品
			product = None
			# 条件变量
			con = threading.Condition()
			
			
			# 生产者方法
			def produce():
			    global product
			
			    if con.acquire():
			        while True:
			            if product is None:
			                print ('produce...')
			                product = 'anything'
			
			                # 通知消费者，商品已经生产
			                con.notify()
			
			            # 等待通知
			            # con.wait()
			            time.sleep(2)
			
			
			# 消费者方法
			def consume():
			    global product
			
			    if con.acquire():
			        while True:
			            if product is not None:
			                print('consume...')
			                product = None
			
			                # 通知生产者，商品已经没了
			                con.notify()
			
			            # 等待通知
			            con.wait()
			            time.sleep(2)
			
			
			t1 = threading.Thread(target=produce)
			t2 = threading.Thread(target=consume)
			t2.start()
			t1.start()
	
		生产者消费者模型
			
			import threading
			import time
			
			condition = threading.Condition()
			products = 0
			
			class Producer(threading.Thread):
			    def run(self):
			        global products
			        while True:
			            if condition.acquire():
			                if products < 10:
			                    products += 1
			                    print("Producer(%s):deliver one, now products:%s" %(self.name, products))
			                    condition.notify()#不释放锁定，因此需要下面一句
			                    condition.release()
			                else:
			                    print("Producer(%s):already 10, stop deliver, now products:%s" %(self.name, products))
			                    condition.wait()#自动释放锁定
			                time.sleep(2)
			
			class Consumer(threading.Thread):
			    def run(self):
			        global products
			        while True:
			            if condition.acquire():
			                if products > 1:
			                    products -= 1
			                    print("Consumer(%s):consume one, now products:%s" %(self.name, products))
			                    condition.notify()
			                    condition.release()
			                else:
			                    print("Consumer(%s):only 1, stop consume, products:%s" %(self.name, products))
			                    condition.wait()
			                time.sleep(2)
			
			if __name__ == "__main__":
			    for p in range(0, 2):
			        p = Producer()
			        p.start()
			
			    for c in range(0, 3):
			        c = Consumer()
			        c.start()
		condition.notifyAll()
		
			import threading
	
			alist = None
			condition = threading.Condition()
			
			
			def doSet():
			    if condition.acquire():
			        while alist is None:
			            condition.wait()
			        for i in range(len(alist))[::-1]:
			            alist[i] = 1
			            print(alist[i])
			        condition.notify()
			        condition.release()
			
			
			def doPrint():
			    if condition.acquire():
			        while alist is None:
			            condition.wait()
			        for i in alist:
			            print(i)
			
			        print()
			        condition.notify()
			        condition.release()
			
			
			def doCreate():
			    global alist
			    if condition.acquire():
			        if alist is None:
			            alist = [0 for i in range(10)]
			            condition.notifyAll()
			        condition.release()
			
			
			tset = threading.Thread(target=doSet, name='tset')
			tprint = threading.Thread(target=doPrint, name='tprint')
			tcreate = threading.Thread(target=doCreate, name='tcreate')
			tset.start()
			tprint.start()
			tcreate.start()

