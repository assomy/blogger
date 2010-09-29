#build your blog as make-blog.conf
import os 
import commands
import re 

conf=open('make-blog.conf')
datausername=conf.readline()
datapassword=conf.readline()
datablogtitle=conf.readline()
datablogdomain=conf.readline()


def make_user():
    usern=re.search(r'([\w.]+)=([\w.]+)',datausername)
    username=usern.group(2)
    replace="sed -i 's/bloguser/"+username+"/g' ouput/database/sql.sql "
    commands.getstatusoutput(replace)
    passwd1=re.search(r'([\w.]+)=([\w.]+)',datapassword)
    passwds=passwd1.group(2)
    replace="sed -i 's/blogpaswd/"+passwds+"/g' ouput/database/sql.sql "
    commands.getstatusoutput(replace)
    btitle1=re.search(r'([\w.]+)=([\w.]+)',datablogtitle)
    btitle2=btitle1.group(2)
    replace="sed -i 's/blogtitle/"+btitle2+"/g' ouput/database/sql.sql "
    commands.getstatusoutput(replace)
    
def make_appache():      
    bdomain1=re.search(r'([\w.]+)=([\w.]+)',datablogdomain)
    bdomain=bdomain1.group(2)
    replace="sed -i 's/myblog/"+bdomin+"/g' ouput/etc/appache "
    commands.getstatusoutput(replace)

def make_index():
    bdomain=re.search(r'([\w.]+)=([\w.]+)',datablogdomain)
    bdomain=bdomain.group(2)
    replace="sed -i 's/myblog/"+bdoamin+"/g' ouput/etc/appache "
    commands.getstatusoutput(replace)
        



make_user()
make_appache()
make_index()
conf.close()
    
