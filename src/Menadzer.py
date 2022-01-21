import matplotlib.pyplot as plt

class Menadzer:
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

    def nadjiVozace(self):
        users = []
        drivers = []

        with open("Data/Zaposljeni.txt") as fp:
            lines = fp.readlines()
            for line in lines:
                l = line.strip().split('|')
                users.append({'id': l[0], 'rank': l[1], 'ime': l[2], 'jmbg': l[3], 'tel': l[4]})
        
            for user in users:
                if user['rank'] == '0':
                    drivers.append(user)

        return drivers

    def prikaziGraf(self, gradovi):
        imena = []
        posecenost = []
        x = []
        y = []
        colors = []
        for grad in gradovi:
            imena.append(grad['ime'])
            posecenost.append(int(grad['posecenost'])*100)

            with open("Data/MapCoords.txt") as fp:
                lines = fp.readlines()
                for line in lines:
                    l = line.strip().split('|')
                    if grad['ime'] == l[0]:
                        x.append(int(l[1]))
                        y.append(int(l[2]))

        im = plt.imread("map.png")
        fig, ax = plt.subplots()
        im = ax.imshow(im)
        ax.set_title('Posecenost gradova')

        for c in posecenost:
            colors.append(c/100)

        plt.scatter(x, y, c=colors, s=posecenost, alpha=0.7, cmap='cividis')
        plt.colorbar()
        plt.show()

    def nruta(self):
        vozaci = self.nadjiVozace()
        vozaciId = []
        gradovi = []

        print('        \033[0;36;40mSvi vozaci:\033[0;37;40m')
        for vozac in vozaci:
            print('''           \033[0;36;40m{})\033[0;37;40m {} \033[0;36;40m|\033[0;37;40m {} \033[0;36;40m|\033[0;37;40m {}'''.format(vozac['id'], vozac['ime'], vozac['jmbg'], vozac['tel']))
            vozaciId.append(vozac['id'])

        id = input('\n        \033[0;36;40mIzaberite vozaca (njegov id):\033[0;37;40m ')
        while id not in vozaciId:
            id = input('\n        \033[0;36;40mIzaberite vozaca (njegov id):\033[0;37;40m ')

        with open("Data/MapCoords.txt") as fp:
            lines = fp.readlines()
            for line in lines:
                l = line.strip().split('|')
                gradovi.append(l[0])

        for grad in gradovi:
            print('''           \033[0;36;40m{})\033[0;37;40m {}'''.format(gradovi.index(grad)+1, grad))
        grad1 = eval(input('\n        \033[0;36;40mIzaberite pocetnu lokaciju (grad id):\033[0;37;40m '))-1
        for grad in gradovi:
            if grad != gradovi[grad1]:
                print('''           \033[0;36;40m{})\033[0;37;40m {}'''.format(gradovi.index(grad)+1, grad))
        grad2 = eval(input('\n        \033[0;36;40mIzaberite krajnju lokaciju (grad id):\033[0;37;40m '))-1

        tovar = input('\n        \033[0;36;40mTovar:\033[0;37;40m ')

        for vozac in vozaci:
            if vozac['id'] == id:
                potvrda_poruka = '''\033[0;36;40m
           \033[0;36;40mVozac:\033[0;37;40m {}
           \033[0;36;40mPocetna lokacija:\033[0;37;40m {}
           \033[0;36;40mKrajnja lokacija:\033[0;37;40m {}
           \033[0;36;40mTovar:\033[0;37;40m {}
                '''.format(vozac['ime'], gradovi[grad1], gradovi[grad2], tovar)
                print(potvrda_poruka)
                potvrda = input('\n        \033[0;36;40mPotvrdi novu rutu(da/ne):\033[0;37;40m ')
        
        if potvrda == 'da':
            with open('Data/AktivneRute.txt', 'a') as file:
                line = gradovi[grad1] + '-' + gradovi[grad2] + '|' + tovar + '|' + id + '|_|_'
                file.write('\n'+line)

    def rute(self):
        vozaci = self.nadjiVozace()
        vozaciId = []

        print('        \033[0;36;40mSvi vozaci:\033[0;37;40m')
        for vozac in vozaci:
            print('''           \033[0;36;40m{})\033[0;37;40m {} \033[0;36;40m|\033[0;37;40m {} \033[0;36;40m|\033[0;37;40m {}'''.format(vozac['id'], vozac['ime'], vozac['jmbg'], vozac['tel']))
            vozaciId.append(vozac['id'])

        id = input('\n        \033[0;36;40mIzaberite vozaca (njegov id):\033[0;37;40m ')
        while id not in vozaciId:
            id = input('\n        \033[0;36;40mIzaberite vozaca (njegov id):\033[0;37;40m ')

        gradovi = []
        sveAktivneRute = []
        aRute = []
        brojacA = 0

        with open("Data/AktivneRute.txt") as fp:
            lines = fp.readlines()
            for line in lines:
                l = line.strip().split('|')
                sveAktivneRute.append({'ruta': l[0], 'tovar': l[1], 'vozac_id': l[2]})
        
            for ruta in sveAktivneRute:
                if id == ruta['vozac_id']:
                    aRute.append(ruta)
                    brojacA += 1

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
                                grad['posecenost'] += 1
                                _grad2 = True

                        if _grad1 == False:
                            gradovi.append(grad1)
                        elif _grad2 == False:
                            gradovi.append(grad2)

        sveRute = []
        vozaceveRute = []
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
                                grad['posecenost'] += 1
                                _grad2 = True

                        if _grad1 == False:
                            gradovi.append(grad1)
                        elif _grad2 == False:
                            gradovi.append(grad2)

        print(f'\n        \033[0;36;40mVozac ima {str(brojac)} zavrsenih ruta:\033[0;37;40m')
        br = 1
        for ruta in vozaceveRute:
            print('''           \033[0;36;40m{})\033[0;37;40m {} \033[0;36;40m|\033[0;37;40m {} \033[0;36;40m|\033[0;37;40m {} \033[0;36;40m|\033[0;37;40m {}rsd'''.format(br, ruta['ruta'], ruta['tovar'], ruta['kilometraza'], ruta['troskovi']))
            br += 1

        print(f'\n        \033[0;36;40mVozac ima {str(brojacA)} aktivnih ruta:\033[0;37;40m')
        br = 1
        for ruta in aRute:
            print('''           \033[0;36;40m{})\033[0;37;40m {} \033[0;36;40m|\033[0;37;40m {}'''.format(br, ruta['ruta'], ruta['tovar']))
            br += 1

        odgovor = input('        Da li zelite videti graf najposecenijih gradova? (da/ne): ')

        if odgovor == 'da':
            self.prikaziGraf(gradovi)

    def vozac(self):
        vozaci = self.nadjiVozace()
        vozaciId = []

        print('        \033[0;36;40mSvi vozaci:\033[0;37;40m')
        for vozac in vozaci:
            print('''           \033[0;36;40m{})\033[0;37;40m {} \033[0;36;40m|\033[0;37;40m {} \033[0;36;40m|\033[0;37;40m {}'''.format(vozac['id'], vozac['ime'], vozac['jmbg'], vozac['tel']))
            vozaciId.append(vozac['id'])

        id = input('\n        \033[0;36;40mIzaberite vozaca (njegov id):\033[0;37;40m ')
        while id not in vozaciId:
            id = input('\n        \033[0;36;40mIzaberite vozaca (njegov id):\033[0;37;40m ')
        
        for vozac in vozaci:
            if vozac['id'] == id:
                datumRodj = vozac['jmbg'][:2] + '.' + vozac['jmbg'][2:4] + '.' + ('20' if vozac['jmbg'][4:5] == '0' else '19') + vozac['jmbg'][4:6]
                info = '''\033[0;36;40m
        Podaci o vozacu:
           \033[0;36;40mIme vozaca:\033[0;37;40m {}
           \033[0;36;40mDatum rodjenja:\033[0;37;40m {}
           \033[0;36;40mJMBG:\033[0;37;40m {}
           \033[0;36;40mBroj telefona:\033[0;37;40m {}
                '''.format(vozac['ime'], datumRodj, vozac['jmbg'], vozac['tel'])
                print(info)

    def posao(self):
        vozaci = self.nadjiVozace()
        vozaciId = []
        opcije = ['zaposli', 'otpusti']

        izbor = input('\n        \033[0;36;40mIzaberite opciju (zaposli/otpusti):\033[0;37;40m ')
        while(izbor not in opcije):
            izbor = input('\n        \033[0;36;40mIzaberite opciju (zaposli/otpusti):\033[0;37;40m ')

        if (izbor == 'otpusti'):
            print('        \033[0;36;40mSvi vozaci:\033[0;37;40m')
            for vozac in vozaci:
                print('''           \033[0;36;40m{})\033[0;37;40m {} \033[0;36;40m|\033[0;37;40m {} \033[0;36;40m|\033[0;37;40m {}'''.format(vozac['id'], vozac['ime'], vozac['jmbg'], vozac['tel']))
                vozaciId.append(vozac['id'])

            id = input('\n        \033[0;36;40mIzaberite vozaca (njegov id):\033[0;37;40m ')
            while id not in vozaciId:
                id = input('\n        \033[0;36;40mIzaberite vozaca (njegov id):\033[0;37;40m ')

            odgovor = input('        \033[0;36;40mDa li sigurni da selite da otpustite vozaca? (da/ne):\033[0;37;40m ')

            if odgovor == 'da':
                for vozac in vozaci:
                    if vozac['id'] == id:
                        ime = vozac['ime']

                a_file = open("Data/Zaposljeni.txt", "r")
                lines = a_file.readlines()
                a_file.close()
                lineToDelete = id + '|0|' + ime
                newFile = ''

                for line in lines:
                    if lineToDelete not in line.strip("\n") and line.strip("\n") != "":
                        newFile += line

                if(newFile[-1:] == '\n'):
                    newFile = newFile[:-1]

                with open('Data/Zaposljeni.txt', 'w') as file:
                    file.write(newFile)
        else:
            ime = input('\n        \033[0;36;40mIme i prezime:\033[0;37;40m ')
            jmbg = input('\n        \033[0;36;40mJMBG (13 cifara):\033[0;37;40m ')
            while(len(jmbg) != 13):
                jmbg = input('\n        \033[0;36;40mJMBG (13 cifara):\033[0;37;40m ')
            tel = input('\n        \033[0;36;40mBroj telefona (+381 06X XXX XXXX):\033[0;37;40m ')
            user = input('\n        \033[0;36;40mKorisnicko ime:\033[0;37;40m ')
            passwd = input('\n        \033[0;36;40mLozinka:\033[0;37;40m ')

            brojac = 0
            with open("Data/Zaposljeni.txt") as fp:
                lines = fp.readlines()
                for line in lines:
                    brojac += 1

            with open('Data/Zaposljeni.txt', 'a') as file:
                line = str(brojac+1) + '|0|' + ime  + '|' + jmbg + '|' + tel + '|' + user + '|' + passwd
                file.write('\n'+line)
 
    def pomoc(self):
        pomoc_menadzer = '''\033[0;36;40m
        pomoc  .............. Ispise lisu komandi
        rute   .............. Pregled svih ruta vozaca
        nruta  .............. Kreiraj novu rutu za vozaca
        vozac  .............. Pregled vozaca
        posao  .............. Zaposljavanje i otpustanje vozaca

        izadji .............. Zavrsite sesiju i izadjite\033[0;37;40m
        '''

        print(pomoc_menadzer)

    def start(self):
        komanda = input('> ')
        while komanda != 'izadji':
            if komanda == 'pomoc':
                self.pomoc()
            elif komanda == 'rute':
                self.rute()
            elif komanda == 'nruta':
                self.nruta()
            elif komanda == 'vozac':
                self.vozac()
            elif komanda == 'posao':
                self.posao()
            elif komanda == '':
                pass
            else:
                print('\n\033[1;31;40m    Nepoznata komanda.\n    Napisite `pomoc` da vidite listu komandi.\033[0;37;40m\n')
        
            komanda = input('> ')