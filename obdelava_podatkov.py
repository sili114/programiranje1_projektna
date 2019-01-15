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
                              r'.*?data-stat="ft_per_g" >(?P<prosti_met>.*?)<'
                              r'.*?data-stat="fta_per_g" >(?P<poskus_prosti_met>.*?)<'
                              r'.*?data-stat="ft_pct" >(?P<prosti_met_procent>.*?)<'
                              r'.*?data-stat="orb_per_g" >(?P<napadalni_skok>.*?)<'
                              r'.*?data-stat="drb_per_g" >(?P<obrambni_skok>.*?)<'
                              r'.*?data-stat="trb_per_g" >(?P<skok>.*?)<'
                              r'.*?data-stat="ast_per_g" >(?P<podaje>.*?)<'
                              r'.*?data-stat="stl_per_g" >(?P<ukradene_zoge>.*?)<'
                              r'.*?data-stat="blk_per_g" >(?P<blokade>.*?)<'
                              r'.*?data-stat="tov_per_g" >(?P<izgubljene_zoge>.*?)<'
                              r'.*?data-stat="pf_per_g" >(?P<osebne_napake>.*?)<'
                              r'.*?data-stat="pts_per_g" >(?P<tocke>.*?)<'

                              , flags=re.DOTALL)


def igralci_na_strani():
    ime_datoteke = 'podatki.html'
    vsebina = orodja.vsebina_datoteke(ime_datoteke)
    igralci = []
    for blok in bloki.finditer(vsebina):
        igralci.append(blok.group(0))
    return igralci

def pocist_podatke(blok):
    igralecc = podatki_igralcev.search(blok).groupdict()
    if len(igralecc['pozicija']) > 2:
        igralecc['pozicija'] = igralecc['pozicija'][:2]
    return igralecc

igralci = []
for igralec in igralci_na_strani():
    podatki = pocist_podatke(igralec)
    if podatki:
        igralci.append(pocist_podatke(igralec))


orodja.zapisi_csv(
    igralci, ['ime', 'pozicija', 'starost', 'odigrane_tekme', 'prva_postava', 'igralni_cas', 'uspesni_meti', 'poskusi_metov',
    'procent_metov', 'meti_za_tri', 'poskusi_za_tri', 'procent_za_tri', 'met_za_dve', 'poskus_za_dve',
    'procent_za_dve', 'prosti_met', 'poskus_prosti_met', 'prosti_met_procent', 'napadalni_skok', 'obrambni_skok', 'skok', 'podaje'
    , 'ukradene_zoge', 'blokade', 'izgubljene_zoge', 'osebne_napake', 'tocke'], 'obdelani-podatki/igralci.csv'
    )


bloki_za_place = re.compile(r'http://www.espn.com/nba/player.*?/td></tr><tr', flags=re.DOTALL)

place_igralcev = re.compile(r'id.*?>(?P<ime>.*?)<'
                            r'.*?text-align:right;">(?P<placa>.*?)<', flags=re.DOTALL)



def placa(st_strani):
    igralci = []
    for i in range(1, st_strani + 1):
        ime = 'podatki/place{}'.format(i)
        vsebina1 = orodja.vsebina_datoteke(ime)
        for blok in bloki_za_place.finditer(vsebina1):
            igralci.append(blok.group(0))
    return igralci


def pocist_place(blok):
    igralec = place_igralcev.search(blok).groupdict()

    igralec['placa'] = int(igralec['placa'][1:].replace(',', ''))
    return igralec

def nared():
    igr = []
    sez = placa(12)
    print(sez)
    for igralec in sez:
        pod = pocist_place(igralec)
        igr.append(pod)
    return igr

n = nared()
print(len(n))

orodja.zapisi_csv(
    n, ['ime', 'placa'] , 'obdelani-podatki/place_igralcev.csv')
