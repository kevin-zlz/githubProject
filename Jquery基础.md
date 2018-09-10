#Jquery基础

1. jQuery 选择器

	1. jQuery 元素选择器

		$("p") 选取 p元素。

		$("p.intro") 选取所有 class="intro" 的p元素。

	2. jQuery 属性选择器

		$("[href]") 选取所有带有 href 属性的元素。

		$("[href='#']") 选取所有带有 href 值等于 "#" 的元素。
	
	3. jQuery CSS 选择器

		$("p").css("background-color","red");

2. jQuery 事件

	1. 下面是 jQuery 中事件方法的一些例子：


		$(document).ready(function)：当文档完成加载时
		$(selector).click(function)：单击事件
		$(selector).focus(function)：获取焦点时触发
		bind():向匹配元素附加一个或更多事件处理器
		blur():失去焦点
		change()：当文本框获取焦点和失去焦点内容发生改变时触发
		event.timeStamp：该属性返回从 1970 年 1 月 1 日到事件发生时的毫秒数。
		event.pageX：相对于文档左边缘的鼠标位置。
		event.pageY：相对于文档上边缘的鼠标位置。
		focus()：触发、或将函数绑定到指定元素的 focus 事件
		keydown()：keyup()：keypress()；
		resize()：触发、或将函数绑定到指定元素的 resize 事件
		toggle()：绑定两个或多个事件处理器函数，当发生轮流的 click 事件时执行。
		unbind()：从匹配元素移除一个被添加的事件处理器

	3. 隐藏和显示

		$("p").hide(1000);隐藏p

		$("p").show();显示p

		$("p").toggle();显示被隐藏的元素，并隐藏已显示的元素：

	3. 淡入淡出

		$("#div3").fadeIn(3000);用于淡入已隐藏的元素。

		$("#div3").fadeOut(3000);方法用于淡出可见元素。

		$("#div3").fadeToggle(3000);如果元素已淡出，则 fadeToggle() 会向元素添加淡入效果。如果元素已淡入，则 fadeToggle() 会向元素添加淡出效果。

		$("#div3").fadeTo("slow",0.7);方法允许渐变为给定的不透明度（值介于 0 与 1 之间）。

	4. 滑动

		$("#panel").slideDown(1000);方法用于向下滑动元素。

		$("#panel").slideUp();方法用于向上滑动元素。

		$("#panel").slideToggle();如果元素向下滑动，则 slideToggle() 可向上滑动它们。如果元素向上滑动，则 slideToggle() 可向下滑动它们。

	5. 动画

		$("div").animate({
    	left:'250px',
    	opacity:'0.5',
    	height:'150px',
    	width:'150px'});;方法用于创建自定义动画。

		$("div").animate({
    	left:'250px',
    	height:'+=150px',
    	width:'+=150px'});

	6. Chaining

		通过 jQuery，您可以把动作/方法链接起来。Chaining 允许我们在一条语句中允许多个 jQuery 方法（在相同的元素上）。$("#p1").css("color","red").slideUp(2000).slideDown(2000);

1. jQuery HTML

	1. 获得内容和属性

		* text() - 设置或返回所选元素的文本内容
		* html() - 设置或返回所选元素的内容（包括 HTML 标记
		* val() - 设置或返回表单字段的值
		* attr() 方法用于获取属性值。$("#w3s").attr("href")

	2. 添加元素

		* append() - 在被选元素的结尾插入内容 $("p").append("Some appended text.");
		* prepend() - 在被选元素的开头插入内容：$("p").prepend("Some prepended text.");
		* after() - 在被选元素之后插入内容：$("img").after("Some text after");
		* before() - 在被选元素之前插入内容：$("img").before("Some text before");

	3. 删除元素

		* remove() - 删除被选元素（及其子元素）$("#div1").remove(".italic");
		* empty() - 从被选元素中删除子元素 $("#div1").empty();

	4. 获取并设置 CSS 类

		* addClass() - 向被选元素添加一个或多个类$("div").addClass("important");
		* removeClass() - 从被选元素删除一个或多个类 $("h1,h2,p").removeClass("blue");
		* toggleClass() - 对被选元素进行添加/删除类的切换操作$("h1,h2,p").toggleClass("blue");
		* css() - 设置或返回样式属性
		* $("p").css("background-color");返回首个匹配元素的 background-color 值：
		* css("propertyname","value");设置指定的 CSS 属性
		* $("p").css({"background-color":"yellow","font-size":"200%"});设置多个 CSS 属性

	6. 尺寸

		* width() 方法设置或返回元素的宽度（不包括内边距、边框或外边距）
		* height() 方法设置或返回元素的高度（不包括内边距、边框或外边距）。
		* innerWidth() 方法返回元素的宽度（包括内边距）。
		* innerHeight() 方法返回元素的高度（包括内边距）。
		* outerWidth() 方法返回元素的宽度（包括内边距和边框）。
		* outerHeight() 方法返回元素的高度（包括内边距和边框）。

3. 遍历

	1. $("span").parent();方法返回被选元素的直接父元素。
	2. $("span").parents();返回被选元素的所有祖先元素
	3. $("span").parentsUntil("div");返回介于两个给定元素之间的所有祖先元素。
	4. $("div").children();返回被选元素的所有直接子元素。
	5. $("div").find("span");返回被选元素的后代元素，一路向下直到最后一个后代。
	6. 同胞

		siblings()返回被选元素的所有同胞元素。
		next()返回被选元素的下一个同胞元素。
		nextAll()返回被选元素的所有跟随的同胞元素。
		nextUntil()返回介于两个给定参数之间的所有跟随的同胞元素。
		prev()
		prevAll()
		prevUntil()

	7. 过滤

		* $("div p").first();方法返回被选元素的首个元素。
		* $("div p").last();返回被选元素的最后一个元素。
		* $("p").eq(1);返回被选元素中带有指定索引号的元素。

3. ajax

	 	$.ajax(
                    {
                        url:'http://0.0.0.0:8080/test',
                        type:"post",
                        data:data,
                        timeout:5000,
                        dataType:"json",
                        contentType:"application/json",
                        //header:{'token','121213'},
                        beforeSend:function (xhr) {
                            xhr.setRequestHeader('TOKEN','FDFDFDFDFDF');
                        },
                        complete:function (result) {
                            console.log(result)
                        },
                        success:function (result) {
                            console.log(result);
                        },
                        error:function () {

                        }
                    }
                )

	
		
	

		



		

		
		

	
		
		
		

		
		