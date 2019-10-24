from urllib2 import urlopen
import base64

bank_statement_url = "https://lendenclub.s3-ap-southeast-1.amazonaws.com/media/documents/2019/08/10/C22E746984F4C1FB6C2BC229.pdf"
file_object = urlopen(bank_statement_url)
base64_file = base64.b64encode(file_object.read())

f= open("fileencoded.txt","w+")

f.write(base64_file)

f.close()

f = open("fileencodedd.txt", "r")
print(f.read()) 
