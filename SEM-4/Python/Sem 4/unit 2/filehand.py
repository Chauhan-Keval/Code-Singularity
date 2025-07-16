import os

class Aboutus():
    def create(self):
        file = open("kevale2.doc","w")
        file.write("Hello world")
        file.close()
        print("Success!!!!")
    def read(self):
        try:
            file = open("kevale2.doc","r")
            print(file.read())
            file.close()
        except:
            print("ERROR File not found")
    def append(self):
        file = open("kevale2.doc","a")
        file.write("yo bro !!!")
        file.close()
    def delete(self):
        os.remove("kevale2.doc")
        print("Delete success")
obj = Aboutus()
obj.create()
obj.read()
obj.append()
obj.read()
obj.delete()
obj.read()