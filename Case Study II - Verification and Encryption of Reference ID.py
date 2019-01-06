import base64
import re
class defendhackers():
    def __init__(self,a):
        self.a = a
    def encodereferenceid(self):
        b = self.a.encode('utf-8')
        reference_id = base64.b64encode(b)
        for i in self.a:
            if len(self.a)!=12:
                print("With your reference ID you will be hacked")
                break
            elif not re.search('[a-z]',self.a):
                print("With your reference ID you will be hacked")
                break
            elif not re.search('[A-Z]',self.a):
                print("With your reference ID you will be hacked")
                break
            elif not re.search('[0-9]',self.a):
                print("With your reference ID you will be hacked")
                break
            elif not re.search('[$#@]',self.a):
                print("With your reference ID you will be hacked")
                break
            else:
                print("Congratulation!!! Your Reference id is encrypted, You are safe from Hackers:",reference_id.decode('utf-8'))
                break

x = input("Enter your reference ID, please make sure it should with 12 digits with captial,lower,numbers,special character combination : ")

s = defendhackers(x)
s.encodereferenceid()


class decoderesults():
    def __init__(self,a):
        self.a = a        
    def decodereferenceid(self):
        b = base64.decodebytes(self.a)
        print("Your reference id is ",b.decode('utf-8'))
        
y = input("Enter Encode details : ").encode('utf-8')
s1 = decoderesults(y)
s1.decodereferenceid()


