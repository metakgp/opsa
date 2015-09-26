import json
import re
import os
import glob,os
from pprint import pprint
from datetime import datetime

##directory of files
dir_proj = "/home/aytas32/opsa"
archive_folder = "Metakgp Slack export Sep 21 2015"
markdown_folder = "MKD_OUTPUT"

#find all channels(i.e the folders)
with open(archive_folder +'/channels.json') as channel_data:
	channelData = json.load(channel_data)
channel_data.close()
channels=[];
for i in range(0,len(channelData)):
	channels.append(channelData[i]['name'].encode("ascii"))
fileNames = [[] for x in xrange(len(channels))]

#get all filenames by directory
for i in range(0,len(channels)):
	#os.system("pwd")
	os.chdir(dir_proj)
	os.chdir(archive_folder)
	os.chdir(channels[i])
	for file in glob.glob("*.json"):
		fileNames[i].append(file)
	fileNames[i].sort()
os.chdir(dir_proj)


#create a mapping from user id to user name
with open(archive_folder +'/users.json') as user_data:
	userData = json.load(user_data)
user_data.close()
#print len(userData)
users = {'none':'do not know'}
for i in range(0,len(userData)):
	users.update({userData[i]['id'].encode("ascii"):userData[i]['name'].encode("ascii")})


out=[];

for i in range(0,len(channels)):
	#print channels[i]
 	target = open(dir_proj+"/" +markdown_folder+"/"+channels[i].encode("ascii")+".md", 'w')#open file for a channel
 	out.append("|**time**|  *user*| text| \n")##add starting elements of file
  	out.append("|-----------------|-----------------|----------------------------------------------| \n")
  	for j in range(0,len(fileNames[i])):

  		os.chdir(dir_proj)
  		os.chdir(archive_folder)
  		os.chdir(channels[i])
    
		with open(fileNames[i][j]) as data_file:
      			data = json.load(data_file)##data read from json
    		data_file.close()##json file closed
	
	    	for k in range(0,len(data)):
			Keys = data[k].keys()
			for p in range(0,len(Keys)):
				Keys[p]= Keys[p].encode("ascii")
			key1 = 'user'
			if key1 not in Keys:
				continue
			
	    		data[k]['text']=data[k]['text'].replace('|',' ')
	    		s= data[k]['text'].encode("ascii",'ignore')
	    		s= s.replace('\r','  ')
	    		t = datetime.fromtimestamp(float(data[k]['ts']))
	    		pool= str(t.strftime('%D %H:%M'))
	    		#s= re.sub('<.*?>', '', s)
	    		out.append("|**%s**|  *%s*| %s| \n"%(pool, users[data[k]['user'].encode("ascii")] ,s.replace('\n','  ')))
	for l in range(0,len(out)):
		target.write(out[l])##write list to file
	target.close()
	del out[:]
  
os.system("cd ..")
os.system("cd ..")
for i in range(0,len(channels)):
	os.system("grip /home/aytas32/opsa/MKD_OUTPUT/"+channels[i]+".md")





