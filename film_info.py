import requests
import json
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", "--title", dest = 'title', help = 'Title of the film')
parser.add_option("--id", dest = 'include_id', default = False, help = 'include id in the resaults', action="store_true")
parser.add_option("--release-date", dest = 'include_release_date', default = False, help = 'include release date in the resaults', action="store_true")
parser.add_option("--year", dest = 'include_year', default = False, help = 'include year in the resaults', action="store_true")
parser.add_option("--stars", dest = 'include_stars', default = False, help = 'include stars in the resaults', action="store_true")
parser.add_option("--awards", dest = 'include_awards', default = False, help = 'include awards in the resaults', action="store_true")
parser.add_option("--rating", dest = 'include_rating', default = False, help = 'include rating in the resaults', action="store_true")
parser.add_option("--url", dest = 'include_url', default = False, help = 'include url in the resaults', action="store_true")
parser.add_option("--all", "-a", dest = 'all_true', default = False, help = "include all parameters", action='store_true')
(options, args) = parser.parse_args()

if options.all_true == True:
    options.include_id = True
    options.include_release_date = True
    options.include_year = True
    options.include_stars = True
    options.include_awards = True
    options.include_rating = True
    options.include_url = True

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

film = options.title
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
            if options.include_id == True:
                print('Id:' ,TheFilm.id)
            if options.include_release_date == True:
                print('Release Date:', TheFilm.releaseDate)
            if options.include_stars == True:
                print('stars:', TheFilm.stars)
            if options.include_awards == True:
                print('awards:', TheFilm.awards)
            if options.include_rating == True:
                print('imdb Rating:', TheFilm.imdbRating)
            if options.include_year == True:
                print('year:', TheFilm.year)
            if options.include_url == True:
                print('Url:', imdb_film_url)
            print("-------------------------------------")
        else:
            print("wrong input")
            exit()
    except:
        print("[!] Unknown ERROR")
        exit()






