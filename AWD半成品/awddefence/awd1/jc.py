import requests
import hashlib
import time
import os

url = ""
txt_url = url + "/.attack_log.txt"
save_dir = "./awdlogs/"

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

