import requests
import json

class Film():
    def __init__ (self, name, id, rank, cast):
        self.name = name
        self.id = id
        self.rank = rank
        self.cast = cast
    def return_imdb_film_url (self):
        url = f"https://www.imdb.com/title/{self.id}/?ref_=nv_sr_srsg_0"
        return url

film = input("film: ")
imdb_search_url = f"https://v2.sg.media-imdb.com/suggestion/{film[0]}/{'_'.join(film.split())}.json"
imdb_search_req = requests.get(url = imdb_search_url)
imdb_search_res = json.loads(imdb_search_req.text)

n = 0
for sth in imdb_search_res['d']:
    n += 1
    print(f"[{n}]> {sth['l']}")
try:
    tmp_ans = int(input(">>"))
except:
    print("wrong input")
    exit()

TheFilm = Film(imdb_search_res['d'][tmp_ans-1]['l'], imdb_search_res['d'][tmp_ans-1]['id'], imdb_search_res['d'][tmp_ans-1]['rank'], imdb_search_res['d'][tmp_ans-1]['s'])

if tmp_ans in range(len(imdb_search_res['d'])):
    print("\n"*2)
    print("-------------------------------------")
    print('name:' ,imdb_search_res['d'][tmp_ans-1]['l'])
    print('id:' ,imdb_search_res['d'][tmp_ans-1]['id'])
    print('rank:' ,imdb_search_res['d'][tmp_ans-1]['rank'])
    print('cast:' ,imdb_search_res['d'][tmp_ans-1]['s'])
    print("-------------------------------------")
else:
    print("wrong input")
    exit()





