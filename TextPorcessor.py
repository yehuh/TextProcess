import paramiko
import time


nowTime = int(time.time()) # 取得現在時間
struct_time = time.localtime(nowTime) # 轉換成時間元組
str_today = time.strftime("%Y-%m-%d", struct_time) # 將時間元組轉
#str_today = "2022-07-12"

#file_name = (str_today+".txt").strip()
file_name = "2022-08-01.txt"
ip_addr = "10.56.40.163"#"10.56.30.120"#"10.56.40.153"
username='myuser'
password='a'
path = "C:\\AGVLog\\system\\"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip_addr, 22, username, password, timeout=10)
sftp_client = client.open_sftp()
remote_file = sftp_client.open(path + file_name)#open("2022-07-02.txt", "r", encoding='UTF-8')
output_path = 'remoteFile_' +str_today+".txt"
out_file = open(output_path, 'w')

line_cnt = 0
for line in remote_file.readlines():
    out_file.write(line.strip()+"\n")
    line_cnt = line_cnt+1
    #if "Time Out" not in line:
    #    continue
    if line_cnt < 10:
        continue
    #if "parseTagData" not in line:
    #    continue
    #if "Update StateObject.current_NodeNo" in line:
    #    continue
    str_buff = "Line " + str(line_cnt)+": "
    print((str_buff + line).strip())
remote_file.close()
out_file.close
