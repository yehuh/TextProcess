import paramiko
import time


nowTime = int(time.time()) # 取得現在時間
struct_time = time.localtime(nowTime) # 轉換成時間元組
str_today = time.strftime("%Y-%m-%d", struct_time) # 將時間元組轉

#file_name = (str_today+".txt").strip()
file_name = "2022-02-08-3_153_1400_1409_VMS.txt"
ip_addr = "10.56.30.188"#"10.56.30.120"#"10.56.40.153"
username='MyUser'
password='a'
path = "C:\\Users\\P1507\\TextProcess\\logSolve\\TianHung\\"
#"C:\\Users\\P1507\\TextProcess\\logSolve\\Uchi\\"
# "C:\\AGVLog\\system\\" 
# 

'''
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip_addr, 22, username, password, timeout=10)
sftp_client = client.open_sftp()
remote_file = sftp_client.open(path + file_name)
'''

#remote_file = open(path + file_name, "r", encoding='UTF-8')
f = open(path + file_name, "rb")
text = f.read().decode(errors='replace')
#print(text)
div_text = text.split("\n")

import moduleVMS

infos = moduleVMS.GetLogInfos(div_text)

print(infos[0])