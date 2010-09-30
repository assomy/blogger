#build your blog as make-blog.conf
import os 
import commands
import re 

conf=open('make-blog.conf')
datausername=conf.readline()
datapassword=conf.readline()
datablogtitle=conf.readline()
datablogdomain=conf.readline()

commands.getstatusoutput('rm output/* -R')
commands.getstatusoutput('cp default/* output/ -R')
def make_user():
    usern=re.search(r'([\w.]+)=([\w.]+)',datausername)
    username=usern.group(2)
    replace="sed -i 's/bloguser/"+username+"/g' output/database/sql.sql "
    commands.getstatusoutput(replace)
    passwd1=re.search(r'([\w.]+)=([\w.]+)',datapassword)
    passwds=passwd1.group(2)
    replace="sed -i 's/blogpaswd/"+passwds+"/g' output/database/sql.sql "
    commands.getstatusoutput(replace)
    btitle1=re.search('(?<==)\??.+',datablogtitle)
    btitle2=btitle1.group(0)
    replace="sed -i 's/blogtitle/"+btitle2+"/g' output/database/sql.sql "
    commands.getstatusoutput(replace)
    return username,passwds,btitle2
    
def make_appache():      
    bdomain1=re.search(r'([\w.]+)=([\w.]+)',datablogdomain)
    bdomain=bdomain1.group(2)
    replace="sed -i 's/myblog/"+bdomain+"/g' output/etc/appache "
    commands.getstatusoutput(replace)

def make_index():
    bdomain=re.search(r'([\w.]+)=([\w.]+)',datablogdomain)
    bdomain=bdomain.group(2)
    replace="sed -i 's/myblog/"+bdomain+"/g' output/wp/index.html "
    commands.getstatusoutput(replace)
    usern=re.search(r'([\w.]+)=([\w.]+)',datausername)
    username=usern.group(2)
    replace="sed -i 's/bloguser/"+username+"/g' output/wp/index.html"
    commands.getstatusoutput(replace)
    btitle1=re.search('(?<==)\??.+',datablogtitle)
    btitle2=btitle1.group(0)
    replace="sed -i 's/blogtitle/"+btitle2+"/g' output/wp/index.html "
    commands.getstatusoutput(replace)

        
def mk_dir_home():
    bdomain1=re.search(r'([\w.]+)=([\w.]+)',datablogdomain)
    bdomain=bdomain1.group(2)
    my_dir_command="mkdir output/home/"+bdomain
    commands.getstatusoutput(my_dir_command)
    return bdomain


def write_log():
    log=open('log.conf','a')
    status='we have make a blog for username: '+username+ ' at domain '+bdomain+'...\n'
    log.write(status)

username,passwds,btitle2= make_user()
print username, passwds , btitle2
make_appache()
my_dir_command=make_index()
bdomain=mk_dir_home()
commands.getstatusoutput('cp -r output/* ROOT/')
conf.close()
write_log()
