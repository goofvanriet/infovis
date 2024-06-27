# De Economische en Sociale Dimensies van CO2-Uitstoot

[Click here to read the data story. ](https://goofvanriet.github.io/infovis/docs/story.html)

**Authors**
- Anou Prins: 13427644
- Efehan Kuznek: 14012847
- Tom Kuin: 13186280
- Goof van Riet: 14715988

Terwijl economische groei lange tijd werd gezien als een manier om de wereldwijde levensstandaarden te verbeteren, roept deze ontwikkeling de laatste decennia vragen op over de duurzaamheid ervan. Hoewel nieuwe wetten en beleid zijn ingevoerd die gericht zijn op het verminderen van wereldwijde CO2-emissies, blijft het een onopgelost probleem. We zien dit terug in het nieuws en in protesten, die zich vooral voordoen in westerse, welvarende landen.

Om de huidige staat van CO2-emissies te visualiseren, zien we in onderstaand figuur de verdeling van CO2-emissies per bron. Deze verdeling benadrukt dat olie in 2022 de dominante bron van CO2-uitstoot is, en dat grondstoffen als steenkool nog steeds een groot aandeel van de CO2-emissies vormen. Het feit dat koolstof, een bekend milieuonvriendelijke grondstof, nog steeds een aanzienlijke bijdrage levert, laat de relevantie van dit probleem zien.

```python
%run notebooks/co2_sources_2022.ipynb


In dit onderzoek willen wij onderzoeken hoe de welvaart van landen correleert met trends in CO2-uitstoot. In het bijzonder zullen we de correlatie tussen jaarlijkse CO2-uitstoot en de Human Development Indicator (HDI) verkennen. HDI is een samengestelde index die de menselijke ontwikkeling meet aan de hand van levensverwachting, onderwijsniveau en inkomen per capita (BBP).

Naast CO2-uitstoot en HDI, willen we gaan kijken naar de verduurzaming van energiebronnen en de relatie daarvan met HDI. We zullen ons focussen op het verband tussen de transitie naar duurzamere energiebronnen en de ontwikkeling van een land volgens de HDI.

We zullen gebruikmaken van een uitgebreide dataset over CO2-emissies, beschikbaar gesteld door Our World In Data (Ritchie et al., 2023), om de emissietrends over de jaren heen te analyseren. Voor de HDI-gegevens gebruiken we een dataset van de Human Development Reports (UNDP, 2023). Ten slotte gebruiken we een dataset over kosten van de Levelized Costs of Energy (LCOE) (Our world in Data, 2024).
Datasets

1. Ritchie, H., Roser, M., & Rosado, P. (2023). CO2 and Greenhouse Gas Emissions Data. Our World in Data. Retrieved from https://github.com/owid/co2-data/blob/master/owid-co2-codebook.csv

2. United Nations Development Programme (UNDP). (2023). Human Development Index (HDI). Human Development Data Center. Retrieved from https://hdr.undp.org/data-center/human-development-index#/indicies/HDI

3. Our World in Data. (n.d.). Levelized cost of energy by technology. Retrieved June 27, 2024, from https://ourworldindata.org/grapher/levelized-cost-of-energy

