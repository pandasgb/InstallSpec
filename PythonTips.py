# 时间函数
import datetime
# 当前时间
now = datetime.datetime.now()
# 转变格式
nowformat = now.strftime('%Y-%m-%d %H:%M:%S')
# 时间差值计算
timedelta = datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
timethen = now - timedelta

# 字符串转datetime
datetime.datetime.strptime('2018-1-1', '%Y-%m-%d')



# 按行读取文件
text = []
fpath = ''
with open(fpath,'r') as f:
  text += f.readlines()
  f.close()
