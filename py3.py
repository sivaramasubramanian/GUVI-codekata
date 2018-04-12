import subprocess
import os

def getLength(filename):
	result = subprocess.Popen(["ffprobe", filename],stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
	duration=""
	for x in result.stdout.readlines():
                if "Duration" in x:
                        duration =x[12:23]                        
                        break
        return duration
  
  

def str2sec(strtime):
        if(len(strtime)>0):                
                print(strtime)
                list1=strtime.split(":")
                print(list1)
                h,m,s = strtime.split(":")
                return (int(h)*3600+int(m)*60+int(round(float(s))))
        else:
                return 0
                
  
path = os.path.dirname(os.path.realpath(__file__))
files = os.listdir(path)
i = 1

for file in files:
	i = i+1
	strduration = str(getLength(file))
	durationsec= str2sec(strduration)
	print(file+" --- "+str(durationsec))
	
    
