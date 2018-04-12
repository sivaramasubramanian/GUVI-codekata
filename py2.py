
import subprocess
import os
import requests
import isodate
import operator

URL = "https://www.googleapis.com/youtube/v3/playlistItems"

#playlistId=str(input("Enter playlist id: "))
part ='contentDetails'
playlistId ='PL6aB9AKiIjgs-ZjubWUpJLu48odxQ3DDk'
maxResults=50
key='AIzaSyCSqX0MFCdovB5qn-H6wtu0ih_1WgPc8X8'
PARAMS = {'part':part,'playlistId':playlistId,'key':key,'maxResults':maxResults}
r = requests.get(url = URL, params = PARAMS)
data = r.json()
youtubedict ={}


for x in data['items']:
 videoId= x['contentDetails']['videoId']
 videofindUrl = " https://www.googleapis.com/youtube/v3/videos"
 videoPart='snippet,contentDetails'
 params2 ={'part':videoPart,'id':videoId,'key':key}
 r2 = requests.get(url = videofindUrl, params = params2)
 data2 = r2.json()
 videoTitle = data2['items'][0]['snippet']['title']
 videoDuration = str(int(round(isodate.parse_duration(data2['items'][0]['contentDetails']['duration']).total_seconds())))
 youtubedict[videoTitle]=videoDuration
 print(videoTitle+"   ----   "+videoDuration)
 
sorted_dict1 = sorted(youtubedict.items(), key=operator.itemgetter(1))
print(sorted_dict1)


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
localdict ={}
i = 1

for file in files:
	i = i+1
	strduration = str(getLength(file))
	durationsec= str2sec(strduration)
	localdict[file]=durationsec
	print(file+" --- "+str(durationsec))


sorted_dict2 = sorted(localdict.items(), key=operator.itemgetter(1))
print(sorted_dict2)	
    
