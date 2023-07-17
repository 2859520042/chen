import requests
import paramiko
import os
import stat
import hashlib
import time

def download_txt_fil(url, save_dir):
    url = url
    save_dir = save_dir
    def download_txt_file(url, save_dir):
        response = requests.get(url)
        if response.status_code == 200:
            # 使用当前时间生成文件名
            timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
            save_path = os.path.join(save_dir, f"awdlog_{timestamp}.txt")
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print("文件已下载")
            return save_path
        else:
            print("无法访问 URL")

    def calculate_md5(file_path):
        with open(file_path, 'rb') as file:
            content = file.read()
            md5_hash = hashlib.md5(content).hexdigest()
        return md5_hash

    # 创建保存目录
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # 创建 latest_awdlog.txt 文件（如果不存在）
    latest_link_path = os.path.join(save_dir, "latest_awdlog.txt")
    if not os.path.exists(latest_link_path):
        with open(latest_link_path, 'w') as file:
            file.write("")

    # 获取初始的 MD5 值
    current_md5 = calculate_md5(os.path.join(save_dir, "latest_awdlog.txt"))

    while True:
        # 请求网站上的 TXT 文件
        response = requests.get(txt_url)
        if response.status_code == 200:
            # 获取下载文件的 MD5 值
            new_md5 = hashlib.md5(response.content).hexdigest()

            if new_md5 != current_md5:
                # 文件内容发生变化，进行下载
                new_file_path = download_txt_file(txt_url, save_dir)
                current_md5 = new_md5
            else:
                print("文件内容未发生变化")
        else:
            print("无法访问 URL")

        # 设置监测间隔为 1 秒
        time.sleep(1)


def shabu(url):
    url = url + '/.c/.c_sha.php'  # 杀不死马的php文件路径
    while (1):
        timeout_seconds = 3
        try:
            a = requests.get(url=url, timeout=timeout_seconds)
        except requests.Timeout:
            # 响应超时
            print("触发了杀不死马文件")
        except requests.RequestException as e:
            # 其他请求异常
            print("触发了一次杀不死马文件")
        a = eval(input("是否继续(1)"))
        if a == 1:
            continue
        else:
            break


def sc(host, port, username, password):
    # SSH连接信息
    # 连接信息
    host = host
    port = port
    username = username
    password = password

    # 本地文件路径和远程目标路径
    local_file = '.c_sha.php'
    remote_path = '/var/www/html/'

    # 建立SSH连接
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(host, port=port, username=username, password=password)

        # 创建SFTP对象
        sftp = client.open_sftp()

        # 上传文件
        sftp.put(local_file, remote_path + 'sha.php')

        print('文件上传成功！')
    finally:
        # 关闭连接
        if sftp:
            sftp.close()
        client.close()


def scf(host, port, username, password):
    # 连接信息
    # 连接信息
    host = host
    port = port
    username = username
    password = password

    # 本地目录和远程目录
    local_folder = 'html'
    remote_folder = '/var/www/html/'

    # 建立SSH连接
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=username, password=password)

    # 创建SFTP对象
    sftp = client.open_sftp()

    # 递归上传文件夹中的所有文件
    def upload_folder(sftp, local_path, remote_path):
        for item in os.listdir(local_path):
            local_item_path = os.path.join(local_path, item)
            remote_item_path = os.path.join(remote_path, item).replace("\\", "/")  # 使用正斜杠作为路径分隔符
            if os.path.isfile(local_item_path):
                sftp.put(local_item_path, remote_item_path)  # 上传文件
            elif os.path.isdir(local_item_path):
                try:
                    sftp.mkdir(remote_item_path)  # 创建远程文件夹
                except Exception as e:
                    print(f"创建远程文件夹失败 或已存在：{e}")
                else:
                    upload_folder(sftp, local_item_path, remote_item_path)

    # 上传文件夹
    upload_folder(sftp, local_folder, remote_folder)

    # 关闭连接
    sftp.close()
    client.close()


def scfc(host, port, username, password, url):
    # 连接信息
    # 连接信息
    host = host
    port = port
    username = username
    password = password

    # 本地目录和远程目录
    local_folder = '.c'
    remote_folder = '/var/www/html/.c/'

    # 建立SSH连接
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=username, password=password)

    # 创建SFTP对象
    sftp = client.open_sftp()

    # 递归上传文件夹中的所有文件
    def upload_folder(sftp, local_path, remote_path):
        for item in os.listdir(local_path):
            local_item_path = os.path.join(local_path, item)
            remote_item_path = os.path.join(remote_path, item).replace("\\", "/")  # 使用正斜杠作为路径分隔符
            if os.path.isfile(local_item_path):
                sftp.put(local_item_path, remote_item_path)  # 上传文件
            elif os.path.isdir(local_item_path):
                try:
                    sftp.mkdir(remote_item_path)  # 创建远程文件夹
                except Exception as e:
                    print(f"创建远程文件夹失败 或已存在：{e}")
                else:
                    upload_folder(sftp, local_item_path, remote_item_path)

    # 上传文件夹
    try:
        sftp.mkdir(remote_folder)  # 创建远程文件夹
    except Exception as e:
        print(f"创建远程文件夹失败或已存在：{e}")
    else:
        upload_folder(sftp, local_folder, remote_folder)
    # upload_folder(sftp, local_folder, remote_folder)

    # 关闭连接
    sftp.close()
    client.close()
    url = url
    timeout_seconds = 3
    try:
        a = requests.get(url=url, timeout=timeout_seconds)
        print("触发了写流量监测脚本的脚本")
    except requests.Timeout:
        # 响应超时
        print("触发了写流量监测脚本失败")
    except requests.RequestException as e:
        # 其他请求异常
        print("触发了写流量监测脚本失败")


def scfr(host, port, username, password):
    # 连接信息
    # 连接信息
    host = host
    port = port
    username = username
    password = password

    # 本地目录和远程目录
    local_folder = 'html'
    remote_folder = '/var/www/html/'

    # 建立SSH连接
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=port, username=username, password=password)

    # 创建SFTP对象
    sftp = client.open_sftp()

    # 递归上传文件夹中的所有文件
    def upload_folder(local_path, remote_path):
        for item in os.listdir(local_path):
            local_item_path = os.path.join(local_path, item)
            remote_item_path = os.path.join(remote_path, item)
            if os.path.isfile(local_item_path):
                sftp.put(local_item_path, remote_item_path)  # 覆盖上传文件
            elif os.path.isdir(local_item_path):
                try:
                    sftp.mkdir(remote_item_path)  # 创建远程文件夹
                except Exception as e:
                    print("创建远程文件夹失败：%s" % str(e))
                else:
                    upload_folder(local_item_path, remote_item_path)

    # 上传文件夹
    upload_folder(local_folder, remote_folder)

    # 关闭连接
    sftp.close()
    client.close()


def xzf(host, port, username, password):
    # 连接信息
    # 连接信息
    hostname = host
    port = port
    username = username
    password = password

    # 本地目录和远程目录
    local_folder = 'html'
    remote_folder = '/var/www/html/'

    # 建立SSH连接
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=port, username=username, password=password)

    # 创建SFTP对象
    sftp = client.open_sftp()

    # 递归下载远程目录中的所有文件
    def download_folder(sftp, remote_path, local_path):
        try:
            os.makedirs(local_path)  # 创建本地文件夹
        except OSError:
            pass

        remote_items = sftp.listdir_attr(remote_path)
        for item in remote_items:
            remote_item_path = remote_path + '/' + item.filename
            local_item_path = os.path.join(local_path, item.filename)

            if stat.S_ISDIR(item.st_mode):
                download_folder(sftp, remote_item_path, local_item_path)  # 递归下载子目录
            else:
                sftp.get(remote_item_path, local_item_path)  # 下载文件

    # 下载文件夹
    download_folder(sftp, remote_folder, local_folder)

    # 关闭连接
    sftp.close()
    client.close()


def zx(ming, host, port, username, password):
    # 连接信息
    host = host
    port = port
    username = username
    password = password

    # 建立SSH连接
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, username, password)

    # 执行命令
    stdin, stdout, stderr = client.exec_command(ming)

    # 输出命令执行结果
    print(stdout.read().decode())

    # 关闭SSH连接
    client.close()


def userinput():
    url = input("请输入你的url")
    host = input("主机名")
    port = input("连接的端口")
    username = input("用户名")
    password = input("密码")
    return host, port, username, password, url


def moren():  # 需要默认自己设置
    host = ""
    port = "22"
    username = ""
    password = ""
    url = ""
    return host, port, username, password,url

def users():
    host = ""
    port = ""
    username = ""
    password = ""
    url = ""
    a = [host,port,username,password,url]
    with open('users.txt', 'r') as file:
        i = 0
        for line in file:
            string = line.strip()
            a[i] = string
            i = i + 1
            # 在这里对每一行的字符串进行处理或使用
    print(a)
    return a[0], a[1],  a[2], a[3], a[4]


user_input = input("是否从用户输入主机信息(1) 是否从文件读取主机信息(2)")
if eval(user_input) == 1:
    host, port, username, password, url = userinput()
if eval(user_input) == 2:
    host, port, username, password, url = users()
else:
    host, port, username, password, url = moren()

while (1):
    user_input = input(
        "上传文件（html下的）修站 （1） 下载文件（html下的）备站（2）上传杀不死马文件 （3） 执行命令（4）上传流量检测脚本(5) 进行流量监测(6)")
    if eval(user_input) == 1:
        print("修站成功")
        scf(host, port, username, password)
    elif eval(user_input) == 2:
        print("备站成功")
        xzf(host, port, username, password)
    elif eval(user_input) == 3:
        print("上传杀不死马文件成功")
        sc(host, port, username, password)
        shabu(url)
    elif eval(user_input) == 4:
        ming = input("输入要执行的命令：")
        # print("执行命令成功")
        zx(ming, host, port, username, password)
    elif eval(user_input) == 5:
        print("上传流量检测脚本")
        url = url + "/.c/.c_waf.php"
        # print("执行命令成功")
        scfc(host, port, username, password, url)
    elif eval(user_input) == 6:
        print("流量检测脚本运行中")
        txt_url = url + "/.attack_log.txt"
        save_dir = "./awdlogs/"
        # print("执行命令成功")
        download_txt_fil(url, save_dir)

