import time
from datetime import datetime as dt

hostsfile_path="/home/vatsan/github/py-tries/hosts-pyex"
redirect_ip="127.0.0.1"
website_list=["www.facebook.com","www.facebook.com","www.dub119.mail.live.com"]

while True:
    if (dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18)):
        with open(hostsfile_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect_ip+"   "+website+"\n")
        print ("Working Hours")
    else:
        with open(hostsfile_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print ("Fun Hours")
    time.sleep(5)
