import distance
import json
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stop=stopwords.words('english')
exp=['?','/','\\','"',"'",'.',';',':','{','}','[',']','|','+','-','_','*','=','!','@','#','$','%','^','&']
def split(bbc,cnn):
	f1=open("IBNworld.json","r").read() 
	f2=open("CNNworld.json","r").read() 
	i=0
	f1=json.loads(f1)
	f2=json.loads(f2)
	return f1,f2
	
	
	
ps=PorterStemmer()

'''def update1(k1,k2):
	i=0
	while i<len(k1):
		t1=k1[i]['T']
		j=0	
		while j<len(k2):
			k=0
			t2=k2[j]['T']
			minn=distance.levenshtein(t1[0],t2[0])
			for word1 in t1:
				su=0
				for word2 in t2:
					if distance.levenshtein(word1,word2)<minn:
						minn=distance.levenshtein(word1,word2)
						su=su+minn
			minsum=su
			for word1 in t1:
				su=0
				for word2 in t2:
					if distance.levenshtein(word1,word2)<minn:
						minn=distance.levenshtein(word1,word2)
						su=su+minn	
				if su<minsum:
					#minsum=su
					#k=j
					print t1
					print '\n'
					print t2
					print '\n-----------------------------------------------------------------------------------\n'
				
			j=j+1
		#print t1
		#print '\n'
		#print t2
		#print '\n-----------------------------------------------------------------------------------\n'
		i=i+1	
'''	
def update1(k1,k2):
	i=0
	while i<len(k1):
		t1=k1[i]['T']
		j=0
		flag=0
		while j<len(k2):
			k=0
			t2=k2[j]['T']
			#for word1 in t1:
			#	dist=0
			#	for word2 in t2:
			#		dist+=distance.lebenshtein(word1,word2)						
			dist=int(distance.levenshtein(t1,t2))
			#print dist			
			if dist<=18:
				flag=1
				break
			#print dist
			j=j+1
	
		
			#minsum=su
			#k=j
		i=i+1							




def update(f):
	t=[]
	i=0
	while i<len(f):
		ti=f[i]['title']
		de=f[i]['des']
		ti=ti.split()
		de=de.split()
		j=0
		titl=[]
		desc=[]

		for j in ti:
			if j not in stop:
				titl.append(j)
		for j in de:
			if j not in stop:
				desc.append(j)

		k=0
		
		fr=[]
		sent=''
		while k<len(titl):
			string=''
			
			let=''
			li=list(titl[k])
			for let in li:
				if let not in exp:
					string=string+let
			string=string.lower()
			#string=ps.stem(string)
			
			sent=sent+string+' '
			
			k=k+1
				
		#fr.sort()
		sin={'T':sent}
		t.append(sin)
		i=i+1
	#print t
	return t


'''def update(f):
	t=[]
	i=0
	while i<len(f):
		ti=f[i]['title']
		de=f[i]['des']
		ti=ti.split()
		de=de.split()
		j=0
		titl=[]
		desc=[]

		for j in ti:
			if j not in stop:
				titl.append(j)
		for j in de:
			if j not in stop:
				desc.append(j)

		k=0
		
		fr=[]
		#sent=''
		while k<len(titl):
			string=''
			
			let=''
			li=list(titl[k])
			for let in li:
				if let not in exp:
					string=string+let
			string=string.lower()
			#string=ps.stem(string)
			fr.append(string)
			#sent=sent+string+' '
			
			k=k+1
				
		fr.sort()
		sin={'T':fr}
		t.append(sin)
		i=i+1
	print t
	return t
'''
