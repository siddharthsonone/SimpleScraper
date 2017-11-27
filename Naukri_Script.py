import time
import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup

with open('output.csv','wb') as file:
    writer = csv.writer(file)
    for page_no in range(0,60):
        url = 'https://www.naukri.com/python-jobs-%d'%page_no
        r = requests.get(url)
        time.sleep(1)
        if r.status_code == 200:
            souppy = BeautifulSoup(r.text,'lxml')
            job_tiles = souppy.find_all('div', class_= 'row ')
            for job_tile in job_tiles:
                add_title = job_tile.find('li', class_='desig').text
                job_title = job_tile.find('span', class_='org').text
                exp_required = job_tile.find('span', class_='exp').text
                job_loc = job_tile.find('span', class_='loc').text
                skill_required = job_tile.find('span', class_='skill').text
                salary = job_tile.find('span', class_= 'salary').text
                print add_title
                lambda txt : txt.enocode('ascii','ignore')
                writer.writerow(map(lambda txt : txt.encode('ascii','ignore'),[add_title
                                 ,job_title
                                 ,exp_required
                                 ,job_loc
                                 ,skill_required
                                 ,salary
                                ]))
        else:
            print 'Failed for %s with status code %s'% (url,r.status_code)
    

file.close()
print 'Done'




