import re
import orodja


bloki = re.compile(r'<tr class="f.*?tr>', flags=re.DOTALL)

podatki_igralcev = re.compile(r'<a href=.*?>(?P<ime>.*?)<'
                              r'.*?data-stat="pos" >(?P<pozicija>.*?)<'
                              r'.*?data-stat="age" >(?P<starost>.*?)<'
                          
                              r'.*?data-stat="g" >(?P<odigrane_tekme>.*?)<'
                              r'.*?data-stat="gs" >(?P<prva_postava>.*?)<'
                              r'.*?data-stat="mp_per_g" >(?P<igralni_cas>.*?)<'
                              r'.*?data-stat="fg_per_g" >(?P<uspesni_meti>.*?)<'
                              r'.*?data-stat="fga_per_g" >(?P<poskusi_metov>.*?)<'
                              r'.*?data-stat="fg_pct" >(?P<procent_metov>.*?)<'
                              r'.*?data-stat="fg3_per_g" >(?P<meti_za_tri>.*?)<'
                              r'.*?fg3a_per_g" >(?P<poskusi_za_tri>.*?)<'
                              r'.*?fg3_pct" >(?P<procent_za_tri>.*?)<'
                              r'.*?fg2_per_g" >(?P<met_za_dve>.*?)<'
                              r'.*?fg2a_per_g" >(?P<poskus_za_dve>.*?)<'
                              r'.*?fg2_pct" >(?P<procent_za_dve>.*?)<'
                              , flags=re.DOTALL)


def igralci_na_strani():
    ime_datoteke = 'podatki.html'
    vsebina = orodja.vsebina_datoteke(ime_datoteke)
    igralci = []
    for blok in bloki.finditer(vsebina):
        igralci.append(blok.group(0))
    return igralci


igralci = []
for igralec in igralci_na_strani():
    podatki = podatki_igralcev.search(igralec).groupdict()
    if podatki:
        igralci.append(podatki_igralcev.search(igralec).groupdict())


orodja.zapisi_csv(
    igralci, ['ime', 'pozicija', 'starost', 'odigrane_tekme', 'prva_postava', 'igralni_cas', 'uspesni_meti', 'poskusi_metov',
    'procent_metov', 'meti_za_tri', 'poskusi_za_tri', 'procent_za_tri', 'met_za_dve', 'poskus_za_dve',
    'procent_za_dve'], 'obdelani-podatki/avtomobili.csv'
    )