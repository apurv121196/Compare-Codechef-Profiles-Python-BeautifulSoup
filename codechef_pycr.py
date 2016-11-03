import urllib
import urllib.request
from bs4 import BeautifulSoup

def getQuestions(url1):
	page1 = urllib.request.urlopen(url1)
	soup_data = BeautifulSoup(page1,'html.parser')
	fetched_data = soup_data.findAll('p')
	questions=[]
	for i in fetched_data:
		if i.find('a')!=-1:
			tags=i.findAll('a')
			for i in tags:
				questions.append(i.get('href').split(',')[0].split('/')[-1])
	return questions

a=input('Enter your username:  ')
b=input("Enter friend's username:  ")

url='https://www.codechef.com/users/'
url1=url+a
url2=url+b

asolved=getQuestions(url1)
bsolved=getQuestions(url2)


da={}
db={}

for i in asolved:
	da[str(i)]=1
for i in bsolved:
	db[str(i)]=1
print('Problems which {} has solved but {} has not solved:'.format(a,b),end='\n')
for i in asolved:
	if db.get(i,-1)==-1:
		print(i,end=', ')
print()
print()
print('Problems which {} has solved but {} has not solved:'.format(b,a),end='\n')
for i in bsolved:
	if da.get(i,-1)==-1:
		print(i,end=', ')
print()