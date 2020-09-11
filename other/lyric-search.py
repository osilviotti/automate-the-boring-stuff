"""
Takes an artist name and scrapes all the lyrics for that artist
from lyricswiki.com. Saves them in a folder called lyrics.
Used to generate searchable content for chapter_8/search.py
"""

from bs4 import BeautifulSoup
from pathlib import Path
import re
import requests
import sys

base_url = 'http://lyricswiki.com'
headers = {'User-Agent': 'XXX'}

def sanitise_name(name):
  return re.sub(r'[^ \w]', '', name).replace(' ', '-')

def get_all_links(artist):
  url = f'{base_url}/search.html'
  params = {'a': 1, 'start': 0, 'c': artist}
  per_page = 50
  links = []
  has_next_page = True

  while has_next_page:
    response = requests.get(url, params = params, headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    new_links = soup.select('.morelink')

    if len(new_links) > 0:
      links = links + [f"{base_url}/{link['href']}" for link in new_links]
      params['start'] += per_page
    else:
      has_next_page = False
  
  return links

def get_lyric_data(url):
  response = requests.get(url, headers = headers)
  soup = BeautifulSoup(response.content, 'html.parser')
  base_selector = ' '.join(['table'] * 6)
  selector_for_row = lambda row: f'{base_selector} tr:nth-child({row}) td:nth-child(2)'
  
  artist = soup.select_one(selector_for_row(2)).text
  album = soup.select_one(selector_for_row(3)).text
  song = soup.select_one(selector_for_row(4)).text
  lyrics = soup.select_one(selector_for_row(10)).text

  return {'artist': artist, 'album': album, 'song': song, 'lyrics': lyrics}

def save_to_files(data):
  base_path = Path(f"./lyrics/{sanitise_name(data[0]['artist'])}")
  base_path.mkdir(parents=True, exist_ok=True)

  for song_data in data:
    album_path = Path(f"{base_path}/{sanitise_name(song_data['album'])}")
    album_path.mkdir(parents=True, exist_ok=True)
    lyric_filepath = Path(f"{album_path}/{sanitise_name(song_data['song'])}.txt")
    lyric_filepath.touch(exist_ok=True)
    file = open(lyric_filepath, 'w')
    file.write(song_data['lyrics'])
    file.close()

try:
  artist = sys.argv[1]
  links = get_all_links(artist)

  if len(links) > 0:
    data = [get_lyric_data(link) for link in links]
    save_to_files(data)
  else:
    print(f'No lyrics found for artist "{artist}".')
except IndexError:
  print('No artist provided.')
  sys.exit()
