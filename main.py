from email import header
import json
from wsgiref import headers
import requests
from salasanat import user_id
from refresh import Refresh


#Ohjelma näyttää käyttäjän Top50 kappaleet muutaman viimeisen vuoden ajalta. (tehty)
#Seuraavaksi käyttöliittymän valmistelu tälle toiminnolle (tehty)
#Seuraavaksi lisätään ohjelmaan viimeksi kuunnellut kappaleet (tehty)
#Seuraavaksi viimeksi kuunnelluiden kappaleiden perusteella "valence" eli mittari kuinka positiivisia kuunnellut kappaleet ovat olleet
#popularity? perusteella jonkinlainen ranking verrattuna muihin kappaleisiin


class Kappaleet:
    def __init__(self):
        self.user_id = user_id
        self.spotify_token = "spotifytoken"
        self.top50 = []
        self.viimeiset = []
        self.kappale_id = []
        self.id_valence = []

    def etsi_kappaleet(self):
        #hakee kuunnelluimmat kappaleet
        query = "https://api.spotify.com/v1/me/top/tracks?time_range=long_term&limit=100"

        response = requests.get(query,
                headers={"Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotify_token)})
            
        response_json = response.json()
        for i in response_json["items"]:
            self.top50.append(i["name"])
            
        for i in self.top50:
            return self.top50

    def viimeaikaiset(self):
        #hakee viimeksi kuunnellut kappaleet
        kysely = "https://api.spotify.com/v1/me/player/recently-played?limit=50"
        vastaus = requests.get(kysely,
                headers={"Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotify_token)})
        vastaus_json = vastaus.json()
        for i in vastaus_json["items"]:
            self.kappale_id.append(i["track"]["id"])
        print(self.kappale_id)

        for i in vastaus_json["items"]:
            self.viimeiset.append(i["track"]["name"])
        for i in self.viimeiset:
            print(self.viimeiset)
            return self.viimeiset

        

    def mood(self):
        #hakee kappaleen valencen kappale_id:n perusteella.
        for i in self.kappale_id:
            haku = f"https://api.spotify.com/v1/audio-features/{i}"
            vastaus = requests.get(haku,
                headers={"Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotify_token)})
            vastaus_json = vastaus.json()
            #print(vastaus_json["valence"])
            
            self.id_valence.append(vastaus_json["valence"])
        return self.id_valence
            
                

        

    def paivita(self):

        print("Päivitetään listaa..")

        paivitys = Refresh()

        self.spotify_token = paivitys.refresh()

#         self.viimeaikaiset()
#         self.mood()

# a = Kappaleet()
# a.paivita()


#+= ", " + str(ranking) +":"  +(i["name"])