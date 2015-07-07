import feedparser
import re
import json


def FILEOPEN(source):
	out=open(str(source),"r")
	out=out.readlines()
	return out
	
def CNNNEWS(out,lo,cnn):
	i=0
	while i<lo:
		url = feedparser.parse(out[i])	
		l=len(url.entries)	
		k=0
		total=[]
		while k<l:
			item=url.entries[k]
			single={'title':item.title,'des':re.sub("<div.*","",item.description,flags=re.DOTALL),'link':item.link}
			total.append(single)
			k=k+1
		x=json.dumps(total)
		writ=open(str(cnn[i])+".json","w")
		writ.write(x)
		writ.close()	
		i=i+1
							    
def IBNNEWS(out,lo,ibn):
	i=0
	while i<lo:
		url = feedparser.parse(out[i])
		l=len(url.entries)	
		k=0
		total=[]
		while k<l:
			item=url.entries[k]
			single={'title':item.title,'des':re.sub("<img.*?/>","",item.description,flags=re.DOTALL),'link':item.link}
			total.append(single)
			k=k+1
		x=json.dumps(total)
		writ=open(str(ibn[i])+".json","w")
		writ.write(x)
		writ.close()	
		i=i+1
	


def BBCNEWS(out,lo,bbc):
	i=0
	while i<lo:
		url = feedparser.parse(out[i])
		l=len(url.entries)	
		k=0
		total=[]
		while k<l:
			item=url.entries[k]
			single={'title':item.title,'des':item.description,'link':item.link}
			total.append(single)
			k=k+1
		x=json.dumps(total)
		writ=open(str(bbc[i])+".json","w")
		writ.write(x)
		writ.close()	
		i=i+1
	




