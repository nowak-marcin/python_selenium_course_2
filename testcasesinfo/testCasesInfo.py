
"""
--------------------------------------------------------------
tc_001
--------------------------------------------------------------
Szczecin Główny,Szczecin Główny,Szczecin Główny,Szczecin Główny,
Gryfino,Gryfino,Gryfino,Gryfino,
10.04.25,10.04.25,10.04.25,10.04.25, -> tomorrow dates
15:00,15:23,15:30,15:54,16:00,16:23, -> arr/dep after expected hour only (15:00)
0,0,0,0, -> 0 => trains changes
REG ticket options: > 0
TLK/IC ticket options: >= 0
selected first button: REG - buy ticket
open operator ticket page in new tab: Wyniki wyszukiwania mPOLREGIO
DB: test user - <order number> - Szczecin Główny - Gryfino
--------------------------------------------------------------
tc_002
--------------------------------------------------------------
Szczecin Główny,Szczecin Główny,Szczecin Główny,Szczecin Główny,
Warszawa Zachodnia,Warszawa Zachodnia,Warszawa Zachodnia,Warszawa Zachodnia,
16.04.25,16.04.25,17.04.25,17.04.25, -> today or tommorrow dates
0,0,0,0,
EIC ticket buttons: > 0
EIP ticket buttons: >= 0
selected active button in second row: EIC/EIP - buy ticket
open operator ticket page in new tab: e-IC2 - Internetowa rezerwacja miejsc
DB: test user - <order number> - Szczecin Główny - Warszawa Zachodnia
"""
