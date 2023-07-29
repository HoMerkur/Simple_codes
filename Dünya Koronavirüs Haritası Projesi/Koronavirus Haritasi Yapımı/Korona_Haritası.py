import folium
import pandas

harita = folium.Map( tiles="Stamen Toner")

veri = pandas.read_excel("tr-cities.xlsx")

enlemler = list(veri["Enlem"])
boylamlar = list(veri["Boylam"])
isimler = list(veri["City"])

for enelm, boylam, isim in zip(enlemler,boylamlar, isimler):
    harita.add_child(folium.Marker(location=(enelm,boylam),
                                   icon=folium.Icon(color="blue"), popup=isim))



harita.save("Deneme.html")





