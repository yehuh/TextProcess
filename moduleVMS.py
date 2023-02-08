from datetime import datetime

def strDivide(notSplitLine):
    strss = notSplitLine.split()
    for div in strss:
        if div == "\t":
            strss.remove(div)
    return strss
    

def GetLogInfos(readed_lines, startLine = 0, endLine = -1):
    if(endLine == -1):
        endLine = len(readed_lines)
    
    info_strs = []
    last_info_end=0
    info_str_buff = ""
    
    for line_no in range(startLine,endLine):
        str_buff = strDivide(readed_lines[line_no])
        
        next_str_buff = ""
        if(line_no < endLine-1):
            next_str_buff = strDivide(readed_lines[line_no+1])
        
         
        try:
            date_str = str_buff[1]
            date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
            #no except => str_buff is info start
            last_info_end = line_no-1
            info_str_buff=readed_lines[line_no]
        except:
            info_str_buff+=readed_lines[line_no]
            
        try:
            date_str = next_str_buff[1]
            date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
            #no except => next_str_buff is info start => str_buff is info end
            info_strs.append(info_str_buff)
        except:
            last_info_end = 0
            #next line is not info start
    
    return info_strs

'''module test


test_str = "haha hah hhhhhhh"
rslt = strDivide(test_str)

for chara in rslt:
    print(chara)
    
module test'''