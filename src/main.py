def login(username, passwd):
    users = []

    with open("Zaposljeni.txt") as fp:
        lines = fp.readlines()
        for line in lines:
            l = line.strip().split('|')
            users.append({'id': l[0], 'k_ime': l[5], 'k_lozinka': l[6]})
    
    for user in users:
        if username == user['k_ime'] and passwd == user['k_lozinka']:
            return user['id']

def main():
    id = None

    while id == None:
        username = input('Korisnicko ime:')
        password = input('Unesite lozinku:')
        
        id = login(username, password)

        if id == None:
            print("Korisnicko ime ili lozinka nisu ispravni. Pokusajte ponovo.")



if __name__ == '__main__':
    main()