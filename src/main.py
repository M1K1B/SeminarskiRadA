from Vozac import Vozac
from Menadzer import Menadzer
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

    print('''
    \033[0;31;40m ____  ____  ____  ____   __  ____  ____   __   __ _  ____  ____   __  ____  ____ 
    \033[0;31;40m/ ___)(  __)(  _ \(  _ \ /  \(_  _)(  _ \ / _\ (  ( \/ ___)(  _ \ /  \(  _ \(_  _)
    \033[0;36;40m\___ \ ) _)  )   / ) _ ((  O ) )(   )   //    \/    /\___ \ ) __/(  O ))   /  )(  
    \033[0;37;40m(____/(____)(__\_)(____/ \__/ (__) (__\_)\_/\_/\_)__)(____/(__)   \__/(__\_) (__)

    Dobrodosli u SerboTransport menadzment program. Za listu komanda napisite `\033[0;36;40mpomoc\033[0;37;40m`
    ''')

    start_time = timeit.default_timer()
    
    if rank == '0':
        Vozac(id).start()
    elif rank == '1':
        Menadzer(id).start()
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