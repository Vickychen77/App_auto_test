import subprocess
import time

confirm=input('please press enter to confirm lifekit was update，or press any button to break          ')

if confirm=='':
	#delete old folders
	subprocess.call(['adb shell rm -rf sdcard/apk_lifekit'],shell=True)
	time.sleep(1)

	#create new folder
	subprocess.call(['adb shell mkdir sdcard/apk_lifekit'],shell=True)
	time.sleep(1)

	# prepare for monkey test
	subprocess.call(['adb push /Users/chenqi1/Desktop/APP_Files/Tools/sysMonkey_prd.apk sdcard/apk_lifekit/'],shell=True)  
	subprocess.call(['adb push /Users/chenqi1/Desktop/APP_Files/Tools/monkey.apk sdcard/apk_lifekit/'],shell=True)
    
    #init LIFEKIT version
	subprocess.call(['adb push /Users/chenqi1/Desktop/LifeKit_v2.5.5_2017-12-12_meizu_prd.apk sdcard/apk_lifekit/'],shell=True)
	#new LIFEKIT version for reinstall
	subprocess.call(['adb push /Users/chenqi1/Desktop/LifeKit_v2.6_2017-12-28_meizu_prd.apk  sdcard/apk_lifekit/'],shell=True)
else:
    print('bye-bye')





