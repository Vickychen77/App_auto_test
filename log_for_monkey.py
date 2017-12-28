import subprocess
import time
import os

isExist=os.path.exists('/Users/chenqi1/Desktop/lifekit_monkey_logs')

if not isExist:
	os.makedirs('/Users/chenqi1/Desktop/lifekit_monkey_logs')
	time.sleep(1)
else:
	pass


now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
log_name='log_'+now_time+'.txt'
subprocess.call(['adb shell dumpsys dropbox -p >/Users/chenqi1/Desktop/lifekit_monkey_logs/'+log_name],shell=True)
