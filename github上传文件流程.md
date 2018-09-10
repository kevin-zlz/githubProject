# github上传文件基本流程

1. 先登录github账号，并创建一个云端仓库用来存储你要上传的项目


2. 打开git bash命令行窗口


3. 第一次需要配置你的用户名和用户邮箱。在git bash命令行窗口上输入一下代码。

		git config --global user.email "you@example.com"
  		git config --global user.name "Your Name"

4. 定位到你在本地即将要创建的仓库所在的位置,比如说我在G盘根目录创建仓库。

		cd /G

5. 将你在云端创建的仓库克隆到G盘根目录。我在云端创建的仓库名叫githubProject

		$ git clone https://github.com/你的用户名/githubProject.git
		Cloning into 'githubProject'...
		warning: You appear to have cloned an empty repository.

6. 在本地G盘找到刚刚克隆好的仓库文件夹（文件夹名称就是你云端仓库的名称），并将你要上传的文件或项目复制到该文件夹下。

7. 定位到你本地仓库文件夹的位置

		
		$ cd /G/githubProject

8. 确定你要上传的文件目录
		
		$ ls

9. 添加并提交所有的仓库中的文件，引号里面的是你上传文件或项目的注释

		$ git add .
		$ git commit -m "md文档"
		$ git push origin master

10. 登录github以后刷新就可以查看你上传的项目或文件了



		


		

	