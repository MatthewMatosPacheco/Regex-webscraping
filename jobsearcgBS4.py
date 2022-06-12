from bs4 import BeautifulSoup
import requests, time
print('Type so Skills that you dont know')
unfamiliar_skill= input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup= BeautifulSoup(html_text,'lxml')
    jobs= soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        posted_date = job.find('span', class_='sim-posted').span.text
        if 'few' in posted_date:
            comp_name=job.find('h3',class_= 'joblist-comp-name').text.replace(' ','')#replaces the useless spaces
            skills= job.find('span', class_= 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:#w = writing in file, as f string
                    f.write(f"Company Name: {comp_name.strip()} \n")
                    f.write(f"Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info}")
                print('file saved')

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'waiting {time_wait} minutes')
        time.sleep(time_wait*60)

