import matplotlib.pyplot as plt

class Vozac:
    def __init__(self, id):
        self.id = id
        self.ime = ''
        self.prezime = ''
        self.jmbg = ''
        self.tel = ''

        self.getInfo(self.id)

    def getInfo(self, id):
        users = []

        with open("Data/Zaposljeni.txt") as fp:
            lines = fp.readlines()
            for line in lines:
                l = line.strip().split('|')
                users.append({'id': l[0], 'rank': l[1], 'ime': l[2], 'jmbg': l[3], 'tel': l[4]})
        
            for user in users:
                if id == user['id']:
                    self.ime = user['ime'].split()[0]
                    self.prezime = user['ime'].split()[1]
                    self.jmbg = user['jmbg']
                    self.tel = user['tel']

    def prikaziGraf(self, gradovi):
        fig = plt.figure('Posecenost gradova')
        ax = fig.add_axes([0,0,1,1])
        ax.axis('equal')
        imena = []
        posecenost = []
        for grad in gradovi:
            imena.append(grad['ime'])
            posecenost.append(grad['posecenost'])
        ax.pie(posecenost, labels = imena, autopct='%1.2f%%')
        ax.set_title('Posecenost gradova')
        plt.show()

    def pomoc(self):
        pomoc_vozac = '''\033[0;36;40m
        pomoc  .............. Ispise lisu komandi
        arute  .............. Pregled svih svojih aktivnih ruta
        rute   .............. Pregled svih svojih ruta
        zavrsi .............. Zavrsite svoju aktivnu rutu

        99     .............. Zavrsite sesiju i izadjite\033[0;37;40m
        '''

        print(pomoc_vozac)

    def nadjiAktivneRute(self, id):
        sveAktivneRute = []
        aRute = []

        with open("Data/AktivneRute.txt") as fp:
            lines = fp.readlines()
            for line in lines:
                l = line.strip().split('|')
                sveAktivneRute.append({'ruta': l[0], 'tovar': l[1], 'vozac_id': l[2]})
        
            for ruta in sveAktivneRute:
                if id == ruta['vozac_id']:
                    aRute.append(ruta)

        return aRute

    def aRute(self, aRute):
        for ruta in aRute:
            print('''
        \033[0;36;40mRuta:\033[0;37;40m {}
        \033[0;36;40mTovar:\033[0;37;40m {}
        \033[0;36;40mVozac:\033[0;37;40m {}
        \033[0;36;40mKilometraza:\033[0;37;40m ...
        \033[0;36;40mPutni troskovi:\033[0;37;40m ...

            '''.format(ruta['ruta'], ruta['tovar'], self.ime + ' ' + self.prezime))

    def sveRute(self, id):
        sveRute = []
        vozaceveRute = []
        gradovi = []
        brojac = 0

        with open("Data/Rute.txt") as fp:
            lines = fp.readlines()
            for line in lines:
                l = line.strip().split('|')
                sveRute.append({'ruta': l[0], 'tovar': l[1], 'vozac_id': l[2], 'kilometraza': l[3], 'troskovi': l[4]})
        
            for ruta in sveRute:
                if id == ruta['vozac_id']:
                    vozaceveRute.append(ruta)
                    brojac += 1
                    
                    grad1, grad2 = {'ime': ruta['ruta'].split('-')[0], 'posecenost': 1}, {'ime': ruta['ruta'].split('-')[1], 'posecenost': 1}
                    
                    if gradovi == []:
                        gradovi.append(grad1)
                        gradovi.append(grad2)
                    else:
                        _grad1 = False
                        _grad2 = False
                        for grad in gradovi:
                            if grad1['ime'] == grad['ime']:
                                grad['posecenost'] += 1
                                _grad1 = True
                            elif grad2['ime'] == grad['ime']:
                                grad['posvecenost'] += 1
                                _grad2 = True

                        if _grad1 == False:
                            gradovi.append(grad1)
                        elif _grad2 == False:
                            gradovi.append(grad2)

                        
        print(f'        Izvozili ste {str(brojac)} ruta:')
        br = 1
        for ruta in vozaceveRute:
            print('''           \033[0;36;40m{})\033[0;37;40m {} \033[0;36;40m|\033[0;37;40m {} \033[0;36;40m|\033[0;37;40m {} \033[0;36;40m|\033[0;37;40m {}rsd'''.format(br, ruta['ruta'], ruta['tovar'], ruta['kilometraza'], ruta['troskovi']))
            br += 1
        odgovor = input('        Da li zelite videti graf najposecenijih gradova? (da/ne): ')

        if odgovor == 'da':
            self.prikaziGraf(gradovi)

    def start(self):
        komanda = input('> ')
        while komanda != '99':
            if komanda == 'pomoc':
                self.pomoc()
            elif komanda == 'arute':
                self.aRute(self.nadjiAktivneRute(self.id))
            elif komanda == 'rute':
                self.sveRute(self.id)
            elif komanda == '':
                pass
            else:
                print('\n\033[1;31;40m    Nepoznata komanda.\n    Napisite `pomoc` da vidite listu komandi.\033[0;37;40m\n')
        
            komanda = input('> ')