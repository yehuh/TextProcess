import paramiko
import time


nowTime = int(time.time()) # 取得現在時間
struct_time = time.localtime(nowTime) # 轉換成時間元組
str_today = time.strftime("%Y-%m-%d", struct_time) # 將時間元組轉

#file_name = (str_today+".txt").strip()
file_name = "2022-06-03-1B.txt"
ip_addr = "10.56.30.188"#"10.56.30.120"#"10.56.40.153"
username='MyUser'
password='a'
path = "C:\\Users\\P1507\\TextProcess\\logSolve\\Uchi\\"
# "C:\\AGVLog\\system\\" 
# "C:\\Users\\P1507\\TextProcess\\logSolve\\TianHung\\"

'''
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip_addr, 22, username, password, timeout=10)
sftp_client = client.open_sftp()
remote_file = sftp_client.open(path + file_name)
'''

remote_file = open(path + file_name, "r", encoding='UTF-8')

#output_path = 'remoteFile_' +file_name+".txt"
#out_file = open(output_path, 'w')

the_str = "Recovery" #"StatusChangeReport"
cmd_str = "AGV->VMS"
AGVC_StartStr = "MCU firmware version"
agvcStartLineCnt = 0
agvcInitCnt = 0
line_cnt = 0
for line in remote_file.readlines():
    line_cnt = line_cnt+1
    if(AGVC_StartStr in line):
        agvcStartLineCnt = line_cnt
        agvcInitCnt = agvcInitCnt+1

line_cnt = 0
remote_file.seek(0, 0)
AGVC_START_SHIFT = 0
TOTAL_LINE_AFTER_START = 100;
for line in remote_file.readlines():
    #out_file.write(line.strip()+"\n")
    line_cnt = line_cnt+1
    #if (the_str not in line): #(cmd_str not in line):#or 
    #    continue
    if line_cnt < agvcStartLineCnt+AGVC_START_SHIFT:
        continue
    if line_cnt > agvcStartLineCnt+TOTAL_LINE_AFTER_START:
        continue
    if line_cnt > 1500:
        continue
    time_id = 0
    time_str_cnt = 22
    time_str = line[time_id: time_id + time_str_cnt] +" "
    str_buff = "Line " + str(line_cnt)+": "
    the_str_id = line.find(the_str)
    if(the_str_id == -1):
        the_str_id = line.find(cmd_str)
        
    cutted_str = line[the_str_id:]
    #print(('%-20s' % time_str + '%-12s' % str_buff + cutted_str).strip())
    print("Line: "+str(line_cnt)+"  "+line.strip())
    
print("\r\nLatest AGVC Start Line: {}\r\nAGVC Init Cnt: {}".format(agvcStartLineCnt, agvcInitCnt))
remote_file.close()
#out_file.close
