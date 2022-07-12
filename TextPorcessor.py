import paramiko
import time

nowTime = int(time.time()) # 取得現在時間
struct_time = time.localtime(nowTime) # 轉換成時間元組
str_today = time.strftime("%Y-%m-%d", struct_time) # 將時間元組轉
file_name = (str_today+".txt").strip()
paramiko.util.log_to_file('C:\\AGVLog\\system\\{}'.format(file_name))  # 日誌記錄
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.56.40.153', 22, username='myuser', password='a', timeout=10)
sftp_client = client.open_sftp()
remote_file = sftp_client.open('C:\\AGVLog\\system\\{}'.format(file_name))
#(stdin, stdout, stderr) = client.exec_command('tail -10 /etc/passwd')
path = "./Jedi/2022-05-30.txt"
#f = open(path, 'r', encoding="utf-8")
line_cnt = 0
for line in remote_file.readlines():
    line_cnt = line_cnt+1
    if line_cnt < 1393:
        continue
    #if "parseTagData" not in line:
    #    continue
    #if "Update StateObject.current_NodeNo" in line:
    #    continue
    str_buff = "Line " + str(line_cnt)+": "
    print((str_buff + line).strip())
remote_file.close()

