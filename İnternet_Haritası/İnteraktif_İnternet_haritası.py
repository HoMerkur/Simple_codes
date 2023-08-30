import pandas
import folium
import requests
from bs4 import BeautifulSoup


veri = pandas.read_excel("world_coronavirus_cases.xlsx")

ulkeler = list(veri["Ülke"])
enlemler = list(veri["Enlem"])
boylamlar = list(veri["Boylam"])

enlem_boylam = list()
enlem_boylam_liste = list()
ulke_sozluk = {}

internet_hizi_haritasi = folium.FeatureGroup(name="İndirme Hızları")

url = "https://www.speedtest.net/global-index"
headers = {
    'User_Agent': "TheUserAgent"}
response = requests.get(url, headers=headers)
content = response.content
html_veri = BeautifulSoup(content, "html.parser")
div_element = html_veri.find("div", {"id":"column-fixedMedian"})

def internet_hizi_radius(hiz):
    if hiz < 25:
        return 400000
    elif hiz < 50:
        return 300000
    elif hiz < 100:
        return 150000
    elif hiz < 200:
        return 75000
    else:
        return 50000
def internet_hizi_renk(hiz):
    if hiz < 25:
        return "red"
    elif hiz < 50:
        return "orange"
    elif hiz < 100:
        return "yellow"
    elif hiz < 200:
        return "green"
    else:
        return "blue"

internet_isimler= list()
duzgun_internet_isimler=list()
for i in div_element.find_all("td",{"class":"country"}):
    internet_isimler.append(i.text)
for i in internet_isimler:
    i = i.replace("\n","")
    i = i.strip()
    duzgun_internet_isimler.append(i)

internet_hizlari = list()
duzgun_internet_hizlari = list()

for i in div_element.find_all("td", {"class":"speed"}):
    internet_hizlari.append(i.text)
for i in internet_hizlari:
    i = i.replace("\n","")
    i = i.strip()
    duzgun_internet_hizlari.append(i)
internet_hizlari_sozluk = {}

for i,j in zip(duzgun_internet_isimler,duzgun_internet_hizlari):
    internet_hizlari_sozluk[i] = j




for i, j in zip(enlemler, boylamlar):
    enlem_boylam.append(i)
    enlem_boylam.append(j)

    enlem_boylam_liste.append(enlem_boylam)
    enlem_boylam = []


for i, j in zip(enlem_boylam_liste, ulkeler):
    ulke_sozluk[j] =i

for i in internet_hizlari_sozluk:
    if i in ulke_sozluk:
            internet_hizi_haritasi.add_child(folium.Circle(location=(ulke_sozluk[i][0], ulke_sozluk[i][1]),
                                                           radius=internet_hizi_radius(float(internet_hizlari_sozluk[i])),
                                                           color=internet_hizi_renk(float(internet_hizlari_sozluk[i])),
                                                           fill_color=internet_hizi_renk(float(internet_hizlari_sozluk[i])), fill_opacity=0.3))
world_harita = folium.Map(tiles="Cartodb Dark_matter")
world_harita.add_child(internet_hizi_haritasi)
world_harita.add_child(folium.LayerControl())
world_harita.save("World_harita.html")
