from Vozac import Vozac
import timeit
import os

# Ovo je funkcija koja ucitava bazu zaposljenih i iz nje vuce id, login podatke i rank svih zaposlenih
# Nakon toga prodje kroz podatke dok ne nadje ispravni username/password kombo i vraca id i rank
def login(username, passwd):
    users = []

    with open("Data/Zaposljeni.txt") as fp:
        lines = fp.readlines()
        for line in lines:
            l = line.strip().split('|')
            users.append({'id': l[0], 'rank': l[1], 'k_ime': l[5], 'k_lozinka': l[6]})
    
    for user in users:
        if username == user['k_ime'] and passwd == user['k_lozinka']:
            return user['id'], user['rank']
        else:
            return None, None

def main():
    id = None

    while id == None:
        username = input('\033[0;36;40m        Korisnicko ime: \033[0;37;40m')
        password = input('\033[0;36;40m        Unesite lozinku: \033[0;37;40m')
        
        id, rank = login(username, password)

        if id == None:
            print("\033[0;31;40m        Korisnicko ime ili lozinka nisu ispravni. Pokusajte ponovo.\033[0;37;40m ")


    os.system('clear')
    start_time = timeit.default_timer()
    
    if rank == '0':
        Vozac(id).start()
    elif rank == '1':
        # Menadzer.start()
        pass
    else:
        print('Nepoznat rank!')

    stop_time = timeit.default_timer()
    print(f'''\033[0;36;40m
        Sesija gotova!
        Vreme koriscenja: \033[0;35;40m{(stop_time-start_time):.2f}\033[0;36;40m s
        Dovidjenja!\033[0;37;40m
    ''')

if __name__ == '__main__':
    main()