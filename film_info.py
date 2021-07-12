import requests
import json

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

# imdb_film_url = f""





