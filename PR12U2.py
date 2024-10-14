

def add(name,phone,github):
    fh=open("file5.txt",'a+')
    fh.write("\nName : "+name+"\nPhone : "+phone+"\nGithub : "+github)
    fh.flush()
    fh.close()


def remove(name,phone,github):
    fh1=open("file5.txt","r+")
    content=fh1.read()
    print("Content : ",content)
    f="Name : "+name+"\nPhone : "+phone+"\nGithub : "+github
    print("passed ",f)
    newc=content.replace(f,"")
    print("remove : ",newc)
    fh1.seek(0)
    fh1.write(newc)
    fh1.flush()
  
# add("ashwin","8780283086","akdesai1")
remove("ashwin","8780283086","akdesai1")
print("Done")
# fh.close()


    