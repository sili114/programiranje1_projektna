# statistika NBA igralcev v sezoni 2017/2018

============================================

Analiziral bom statistike 540 igralcev s strani 
https://www.basketball-reference.com/leagues/NBA_2018_per_game.html

Za vsakega igralca bom zajel:
* ime in priimek
* igralno pozicijo
* starost
* ekipo za katero igrajo
* število igranih tekem
* število začetkov tekem na parketu
* število metov in procent zadetih metov
* število točk na tekmo
* število ukradenih žog

Delovne hipoteze:
* Je pozicija igralca povezana s številom doseženih točk?
* Imajo starejši igralci večji procent zadetih metov?
* So najboljši strelci metov za 3 točke tudi najboljši pri prostih metih? Ali velja tudi obrat?
* Ali imajo igralci z največ doseženimi točkami tudi najboljši izkoristek metov?

Delovni proces:

* Podatke zbrane v datoteki igralci.csv sem zajel s skriptami v datoteki orodja.py in uredil s skriptami v obdelava_podatkov.py.
* Datoteka igralci.csv vsebuje naslednje podatke za vsakega igralca:
    * Ime in priimek, igralna pozicija, starost, število odigranih tekem v sezoni, število začetkov tekem v prvi postavi, povprečen igralni čas, število poskusov in število zadetih metov in procent teh metov (vseh metov, metov za 2, metov za 3 in prostih metov), število napadalnih, obrambnih in vseh skokov, število podaj, blokad, ukradenih žog, izgubljenih žog, osebnih napak in točk.
* Na teh podatkih bom preveril zgoraj omenjene hipoteze in še mnoge druge.
    
