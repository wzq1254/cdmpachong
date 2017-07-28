
import urllib2
f=file("text.txt","a+")

 
url = "http://cdm.ccchina.gov.cn/newitemall0.aspx?page="


for i in range(11):
	response = urllib2.urlopen(url+str(i))
	f.write(response.read())



f.close()