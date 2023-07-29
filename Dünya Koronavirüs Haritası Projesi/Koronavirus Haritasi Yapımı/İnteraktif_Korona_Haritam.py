import pandas
import folium

veri = pandas.read_excel("world_coronavirus_cases.xlsx")

enlemler = list(veri["Enlem"])
boylamlar = list(veri["Boylam"])
toplam_vaka =list(veri["Toplam Vaka"])
vefatlar = list(veri["Vefat Edenler"])
aktifler = list(veri["Aktif Vakalar"])
nufus = list(veri["Nüfus"])
toplam_test = list(veri["Toplam Test"])



vaka_sayisi_haritasi = folium.FeatureGroup(name="Toplam Vaka Sayısı Haritası")
olum_orani_haritasi = folium.FeatureGroup(name="Ölüm Oranı Haritası")
aktif_vaka_haritasi = folium.FeatureGroup(name="Aktif Vaka Haritası")
test_orani_haritasi = folium.FeatureGroup(name="Test Oranı Haritası")
nufus_dagilim_haritasi = folium.FeatureGroup(name="Nüfus Dağılım Haritası")


def vaka_sayisi_renk(vaka):
    if vaka < 100000:
        return "green"
    elif vaka < 300000:
        return "white"
    elif vaka < 750000:
        return "orange"
    else:
        return "red"

def vaka_sayisi_radius(vaka):
    if vaka < 100000:
        return 75000
    elif vaka < 300000:
        return 100000
    elif vaka < 750000:
        return 200000
    else:
        return 400000

def vefat_orani_radius(vefat,vaka):
    oran = (vefat/vaka)*100

    if oran < 2.5:
        return 40000
    elif oran < 5:
        return 100000
    elif oran < 7.5:
        return 200000
    else:
        return 400000

def vefat_orani_renk(vefat, vaka):
    oran = (vefat / vaka) * 100

    if oran < 2.5:
        return "green"
    elif oran < 5:
        return "white"
    elif oran < 7.5:
        return "orange"
    else:
        return "red"


def aktif_vaka_renk(aktif):
    if aktif < 10000:
        return "green"
    elif aktif < 25000:
        return "white"
    elif aktif < 50000:
        return "orange"
    else:
        return "red"

def aktif_vaka_radius(aktif):

    if aktif < 10000:
        return 75000
    elif aktif < 25000:
        return 100000
    elif aktif < 50000:
        return 200000
    else:
        return 400000

def test_orani_renk(test, nufus):
    oran = (test / nufus) * 100

    if oran < 2.5:
        return "red"
    elif oran < 5:
        return "orange"
    elif oran < 7.5:
        return "white"
    else:
        return "green"

def test_orani_radius(test, nufus):
    oran = (test / nufus) * 100

    if oran < 2.5:
        return 400000
    elif oran < 5:
        return 100000
    elif oran < 7.5:
        return 50000
    else:
        return 10000





world_harita = folium.Map(tiles="Cartodb Dark_matter")


for enlem, boylam, vaka in zip(enlemler,boylamlar, toplam_vaka):
    vaka_sayisi_haritasi.add_child(folium.Circle(location=(enlem,boylam),
                                                 radius=vaka_sayisi_radius(vaka),
                                         color=vaka_sayisi_renk(vaka),
                                         fill_color=vaka_sayisi_renk(vaka), fill_opacity=0.3))

for enlem, boylam, vaka, vefat in zip(enlemler, boylamlar, toplam_vaka, vefatlar):
    olum_orani_haritasi.add_child(folium.Circle(location=(enlem,boylam), radius=vefat_orani_radius(vefat, vaka),
                                         color=vefat_orani_renk(vefat, vaka),
                                         fill_color=vefat_orani_renk(vefat, vaka), fill_opacity=0.3))

for enlem, boylam, aktif in zip(enlemler,boylamlar, aktifler):
    aktif_vaka_haritasi.add_child(folium.Circle(location=(enlem,boylam),
                                                 radius=aktif_vaka_radius(aktif),
                                         color=aktif_vaka_renk(aktif),
                                         fill_color=aktif_vaka_renk(aktif), fill_opacity=0.3))

for enlem, boylam, ulke_nufus, test in zip(enlemler,boylamlar, nufus, toplam_test):
    test_orani_haritasi.add_child(folium.Circle(location=(enlem,boylam),
                                                 radius=test_orani_radius(test,ulke_nufus),
                                         color=test_orani_renk(test,ulke_nufus),
                                         fill_color=test_orani_renk(test,ulke_nufus), fill_opacity=0.3))

nufus_dagilim_haritasi.add_child(folium.GeoJson(data=(open("world.json", "r", encoding="utf-8-sig").read()),
                                    style_function = lambda x: {"fillColor":"green"
                                    if x ["properties"]["POP2005"] < 20000000 else
                                    "white" if 20000000 <= x["properties"]["POP2005"] <= 50000000
                                    else "orange" if 50000000 <= x["properties"]["POP2005"] <= 100000000
                                    else "red"}))


world_harita.add_child(vaka_sayisi_haritasi)
world_harita.add_child(olum_orani_haritasi)
world_harita.add_child(aktif_vaka_haritasi)
world_harita.add_child(test_orani_haritasi)
world_harita.add_child(nufus_dagilim_haritasi)

world_harita.add_child(folium.LayerControl())

world_harita.save("World_harita.html")


