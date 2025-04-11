# TEST_TIMETABLE:
"""
--------------------------------------------------------------
tc_001
--------------------------------------------------------------
checkbox1 selected ->
checkbox2 unselected ->
checkbox3 unselected ->
checkbox4 selected ->
checkbox5 selected ->
Szczecin Główny,Szczecin Główny,Szczecin Główny,Szczecin Główny,
Gryfino,Gryfino,Gryfino,Gryfino,
10.04.25,10.04.25,10.04.25,10.04.25, -> tomorrow dates
15:00,15:23,15:30,15:54,16:00,16:23, -> arr/dep after expected hour (15:00)
0,0,0,0, -> count of train changes
REG ticket options: > 0
TLK/IC ticket options: >= 0
selected first button: REG - buy ticket
open operator ticket page in new tab: Wyniki wyszukiwania mPOLREGIO
DB: test user - <order number> - Szczecin Główny - Gryfino
PASSED END TESTING SESSION
===============================================================
"""
"""
--------------------------------------------------------------
tc_002
--------------------------------------------------------------
"""
