class Híres_katona:
    def __init__(self, név,foglalkozás,nemzetiség):
        self.név=név
        self.foglalkozás=foglalkozás
        self.nemzetiség=nemzetiség
    def előtag(self):
        if nemzetiség=='n':
            return 'Herr'
        else:
            return 'Mister'

híres_katona=[]
for _ in range(3):
    név=input('Kérem adja meg a katona nevét! ')
    foglalkozás=input('Kérem adja meg a katona rangját! ')
    nemzetiség=input('Kérem adja meg a nemzetiségét! (o,n)')
    híres_katona1=Híres_katona(név,foglalkozás,nemzetiség)
    híres_katona.append(híres_katona1)
    
for hkatona in híres_katona:
    print(f'{Híres_katona.elotag} {Híres_katona.név} egy híres {Híres_katona}')