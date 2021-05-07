# -*- coding: utf-8 -*-
"""
Created on Tue May  4 08:13:53 2021

@author: ELCOT
"""
import requests
from bs4 import BeautifulSoup
import urllib,re

root_url='https://www.starmusiq.vip/'
main_url='https://www.starmusiq.vip/composers/collection-of-a.r.rahman-starmusiq.html/page-'

albums=[]
for i in range(1,14):
    re=requests.get(main_url+str(i))
    soup=BeautifulSoup(re.text,'html.parser')
    for tag in soup.find_all('div','row center-block'):
        for atag in tag.find_all('a',href=True):
            if atag['href'].startswith('/movies'):
                if atag['href'] not in albums:
                    albums.append(atag['href'])
                    
songs_links=[]                
for album in albums:                    
    req_album=requests.get(root_url+album)
    soup_album=BeautifulSoup(req_album.text,'html.parser')
    for album_tag in soup_album.find_all('a',href=True,class_='label label-info'):
        if album_tag['href'] not in songs_links:
            songs_links.append(album_tag['href'])
            
            
songs=[]
for song_link in songs_links:
    req_song=requests.get(song_link)
    soup_song=BeautifulSoup(req_song.text,'html.parser')
    for song_tag in soup_song.find_all('a',href=True,class_='btn btn-lg btn-success'):
        if song_tag['href'] not in songs:
            songs.append(song_tag['href'])
 
save_path='D:\AR Rahman\Songs\\'
mp3_root='http://www.mp3musiq.xyz/download-7s-sng-new/'

for song in songs:
    try:
        print('Downloding...')
        mp3_file_req=requests.get(mp3_root+song)
        filename=re.findall('filename=(.+)', mp3_file_req.headers.get('content-disposition'))[0].split('-')[0].replace('"','')
        open(save_path+filename+'.mp3','wb').write(mp3_file_req.content)
        print(filename+' Done')
    except:
        print('Error.....   '+song)
    
    
 
    


    




    