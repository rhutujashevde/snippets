from urllib2 import urlopen
import base64

bank_statement_url = "url"
file_object = urlopen(bank_statement_url)
base64_file = base64.b64encode(file_object.read())

f= open("fileencoded.txt","w+")

f.write(base64_file)

f.close()

f = open("fileencodedd.txt", "r")
print(f.read()) 
