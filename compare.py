from nltk.corpus import stopwords
import json
import difflib as d


t=[]
def split(bbc,ibn):
	f1=open(str(bbc)+".txt","r").read() 
	f2=open(str(ibn)+".txt","r").read() 
	i=0
	f1=json.loads(f1)
	f2=json.loads(f2)
	stop=stopwords.words('english')
	while i<5:
		c1=f1[i]['des']
		s1=c1.split()
		j=0
		
		while j<5:
			c2=f2[j]['des']
			s2=c2.split()
			comp=compare(s1,s2)
			if comp==True: break
			j=j+1
		if comp==True:
			print f1[i]['des']+'\n'+f2[j]['des']
			#examp=open("sample.txt","w")
			#sin={'title':f1[i]['title'],'des':f1[i]['des'],'link1':f1[i]['link'],'link2':f2[k]['link']}
			#t.append(sin)
		
		i=i+1
	#jsf=json.dumps(t)
	#examp.write(jsf)
	#examp.close()


def compare(

'''def compare(s1,s2):
	c=0
	s=d.get_close_matches
	for k in s1:
		if s(k,s2):
			c=c+1
	per=(float(c) / float(len(s1))*100)
	if per>30:
		return True
	else: 
		return False

#	k=0
#	while k<len(s1):
#		l=0
#		while l<len(s2):
#			if s1[k]==s2[l]:
#				c=c+1
#			l=l+1
#		k=k+1
#	if c>4:
#		return True'''
