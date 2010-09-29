#build your blog as make-blog.conf
import os 
import commands
import re 
import sys
def read_your_config:
    conf=open('make-blog.conf')
    datapassword=conf.readline()
    datablogtitle=conf.readline()
    datablogdomain=conf.readline()


def make_user:
    usern=re.search(r'([\w.]+)=([\w.]+)',datausername)
    username=usern.group(2)
    commands.getstatusoutput(" sed -i 's/love/kill/g' conf ")

    
            
def blog_domain:
    bdom=re.search(r'([\w.]+)=([\w.]+)',datablogdomain)
    blogdomain=bdom.group(2)
    
def main_maker:
                  
    
