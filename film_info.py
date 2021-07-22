import requests
import json


class Film():
    def __init__ (self, name, id, rank, cast):
        self.name = name
        self.id = id
        self.rank = rank
        self.cast = cast
        json_res = json.loads(requests.get(url = f"https://imdb-api.com/en/API/Title/k_q271udqt/{self.id}").text)
        self.year = json_res['year']
        self.releaseDate = json_res['releaseDate']
        self.awards = json_res['awards']
        self.stars = json_res['stars']
        self.imdbRating = json_res['imDbRating']
    def return_imdb_film_url(self):
        return f"https://www.imdb.com/title/{self.id}/?ref_=nv_sr_srsg_0"

film = input("film: ")
imdb_search_url = f"https://v2.sg.media-imdb.com/suggestion/{film[0]}/{'_'.join(film.split())}.json"
imdb_search_req = requests.get(url = imdb_search_url)
imdb_search_res = json.loads(imdb_search_req.text)

n = 0
for sth in imdb_search_res['d']:
    n += 1
    print(f"[{n}]> {sth['l']}")

tmp_ans = input(">>")
tmp_answers = tmp_ans.split()


for tmp_answer in tmp_answers:
    try:
        tmp_ans = int(tmp_answer)
        TheFilm = Film(imdb_search_res['d'][tmp_ans-1]['l'], imdb_search_res['d'][tmp_ans-1]['id'], imdb_search_res['d'][tmp_ans-1]['rank'], imdb_search_res['d'][tmp_ans-1]['s'])
        imdb_film_url = TheFilm.return_imdb_film_url()
        if tmp_ans-1 in range(len(imdb_search_res['d'])):
            print("\n"*2)
            print("-------------------------------------")
            print('Name:' ,TheFilm.name)
            print('Id:' ,TheFilm.id)
            print('Release Date:', TheFilm.releaseDate)
            print('stars:', TheFilm.stars)
            print('awards:', TheFilm.awards)
            print('imdb Rating:', TheFilm.imdbRating)
            print('Url:', imdb_film_url)
            print("-------------------------------------")
        else:
            print("wrong input")
            exit()
    except:
        print("[!] Unknown ERROR")
        exit()






