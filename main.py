from extract import *
from freq import *

source=['CNN','IBN','BBC']


cnn=['CNNtop','CNNworld','CNNbusiness','CNNtechnology','CNNentertainment','CNNsport','CNNhealth','CNNpolitics','CNNtravel']
ibn=['IBNtop','IBNworld','IBNbusiness','IBNtechnology','IBNentertainment','IBNsport','IBNhealth','IBNpolitics','IBNtravel']
bbc=['BBCtop','BBCworld','BBCbusiness','BBCtechnology','BBCentertainment','BBCsport','BBChealth','BBCpolitics','BBCtravel']

i=0
while i<len(source):	
	out=FILEOPEN(source[i])
	if i==0:CNNNEWS(out,len(cnn),cnn)
	if i==1:IBNNEWS(out,len(ibn),ibn)
	if i==2:BBCNEWS(out,len(bbc),bbc)
	i=i+1

def compare():
	f1,f2=split(bbc[0],ibn[0])
	n1=update(f1)
	n2=update(f2)
	new1=open("array1.txt","w")
	new2=open("array2.txt","w")
	n1=json.dumps(n1)
	new1.write(n1)
	n2=json.dumps(n2)
	new2.write(n2)
	k1=json.loads(n1)
	k2=json.loads(n2)
	update1(k1,k2)
compare()
