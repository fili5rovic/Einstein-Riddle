# region Uslovi
def plus_u_recniku(_key, _value):
    for key in dict:
        if key == _key:  # jeste od onog gde cuvam
            for i in range(len(dict[key])):
                if _value in dict[key][i]:
                    dict[key][i] = [_value]
                    samo_plusevi[i].insert(i, _value)
                    samo_plusevi[i].pop()

        else:
            for i in range(len(dict[key])):
                if _value in dict[key][i]:
                    for pojam in dict[key][i]:
                        if pojam == _value:
                            dict[key][i].remove(pojam)
                            if (len(dict[key][i]) == 1):
                                print("Skloni iz ostalih", dict[_key][i][0])
                                skloni_iz_ostalih(_key, i, dict[_key][i][0])
                            break


def plus_za_predmete(predmet1, predmet2):
    flag1 = False
    flag2 = False
    for key in dict:
        for i in range(len(dict[key])):
            if predmet1 in dict[key][i]:
                flag1 = True
            if predmet2 in dict[key][i]:
                flag2 = True
        if flag1 == flag2:
            break
        flag1 = False
        flag2 = False
    if flag1 is True and flag2 is True:
        print("Sve je okej")
        return True
    else:
        #print_c1("\nNetacan unos, resenje ne postoji.")
        return False


def skloni_iz_ostalih(_key, _i, _pojam):  # ne sklanjaj iz _key
    for key in dict:
        if key != _key and _pojam in dict[key][_i]:
            dict[key][_i].remove(_pojam)


def minus_u_recniku(_key, _value):
    for i in range(len(dict[_key])):
        if _value in dict[_key][i]:
            for pojam in dict[_key][i]:
                if pojam == _value:
                    dict[_key][i].remove(pojam)
                    # for key in dict:
                    #     if(len(dict[key][i]) == 1):
                    #         print("Izbacio sam",dict[_key][i][0])
                    #         skloni_iz_ostalih(_key,i,dict[_key][i][0])
                    return


def predmet_u_ostalim(_key, _val):
    for key in dict:
        if (key != _key):
            for i in range(len(dict[key])):
                for x in dict[key][i]:
                    if x == _val:
                        return True
    return False


def minus_za_predmete(predmet1, predmet2):
    flag1 = False
    flag2 = False
    for key in dict:
        for i in range(len(dict[key])):
            if predmet1 in dict[key][i]:
                flag1 = True
            if predmet2 in dict[key][i]:
                flag2 = True
        if flag1 and flag2:
            for i in range(len(dict[key])):
                if predmet2 in dict[key][i]:
                    dict[key][i].remove(predmet2)
                else:
                    pass
        flag1 = False
        flag2 = False
    # provera ako je ostala samo sveska recimo
    if flag1 is True and flag2 is True:
        for key in dict:
            for i in range(len(dict[key])):
                for x in dict[key][i]:
                    if not predmet_u_ostalim(key, x):
                        dict[key][i] = [x]


def proveri_jedan_element():
    for key in dict:
        for i in range(len(dict[key])):
            if (len(dict[key][i]) == 1):
                skloni_iz_ostalih(key, i, dict[key][i][0])
            elif (len(dict[key][i]) == 0):
                print("Greska!")
                return False
    return True


def unos_pojmova():
    for i in range(0, m - 1):
        unos = input().split(',')
        pojmovi.append(unos.copy())
    # dodajem sve pojmove na svakog
    for x in prvi_red:
        dict[x] = [pojmovi[i].copy() for i in range(m - 1)]


def obrada_uslova():
    konacno = True
    while (True):
        x = input()
        if (len(x) == 0): break
        if '+' in x:
            kljuc, pojam = x.split('+')
            if kljuc in dict:
                plus_u_recniku(kljuc, pojam)
            else:
                konacno = plus_za_predmete(kljuc, pojam)
                if konacno is False:
                    return konacno
        elif '-' in x:
            kljuc, pojam = x.split('-')
            if kljuc in dict:
                minus_u_recniku(kljuc, pojam)
            else:
                minus_za_predmete(kljuc, pojam)
        konacno = proveri_jedan_element()
        if konacno is False:
            return konacno
    return konacno


def vrati_tacne_pojmove():
    vracena = []
    for key in dict:
        x = []
        for lista in dict[key]:
            x.extend(lista)
        vracena.append(x)
    return vracena


# endregion


# region Stablo
class Node:
    def __init__(self, info=None):
        if info is None:
            info = []
            for i in range(0, m):
                niz = []
                for j in range(0, n - 1):
                    niz.append('_')
                info.append(niz)
        self.info = info
        self.lvl = 0
        self.next = None
        self.child = None

    def add_child(self, info):
        try:
            new_node = Node(info)
            node = self
            new_node.lvl = node.lvl + 1
            while (node.next != None):
                node = node.next
            node.next = new_node
            return new_node
        except TypeError:
            print("Prosledili ste None vrednost za cvor.")

    def add_next(self, info):
        try:
            new_node = Node(info)
            node = self
            new_node.lvl = node.lvl
            while (node.next != None):
                node = node.next
            node.next = new_node
            return new_node
        except TypeError:
            print("Prosledili ste None vrednost za cvor.")


def preorder(root):
    push(root)
    prev = None
    while (not empty_stack()):
        curr = pop()
        if (prev != None and curr.lvl > prev.lvl):
            print()
        while (curr != None):
            print(f"{curr.info} ({curr.lvl})", end=' ')
            if (curr.next != None):
                push(curr.next)
            prev = curr
            curr = curr.child


def replace_element_in_list(lst, old_value, i, j):
    new_value = pojmovi[i][j]
    if new_value in lst:
        print("Vec postoji u listi!")
        return lst
    for k in range(len(lst)):
        if lst[k] == old_value and k == i:
            if k > 0 and lst[k - 1] in pojmovi[i]:
                return lst
            lst[k] = new_value
            return lst
    return lst


def print_matrix_c1(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            print_c1(f"|{str(x[i][j]).center(9)}|", end='')
        print()
    print()


def print_matrix(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            print("|", str(x[i][j]).center(9), "|", end='')
        print()
    print()


def print_matrix_file(x):
    for i in range(len(x)):
        s = ''
        for j in range(len(x[0])):
            s += f"| {str(x[i][j]).center(9)} |"
        upisi_u_fajl(s)
    upisi_u_fajl('')


def prekopiraj_info(root):
    x = Node().info
    for i in range(len(root.info)):
        for j in range(len(root.info[0])):
            x[i][j] = root.info[i][j]
    return x


def jeste_u_matrici(pojam, matrica):
    for i in range(len(matrica)):
        for j in range(len(matrica[0])):
            if pojam == matrica[i][j]:
                return True
    return False


def is_in_matrix(p, mat):
    for i in range(len(mat)):
        if p in mat[i]:
            return True
    return False


def preklapa_se_sa_plusevima(matrix, k, i):
    if any(samo_plusevi[i]) != 0:
        # print_c1(f"Sada ovo: {matrix[k]}")
        for a in range(len(samo_plusevi)):
            for b in range(len(samo_plusevi[0])):
                if samo_plusevi[a][b] != 0:
                    if matrix[a][b] != samo_plusevi[a][b] and is_in_matrix(samo_plusevi[a][b], matrix):
                        # print('OVO JE NETACNO1::::', samo_plusevi[k][i])
                        return True
        # for j in range(len(samo_plusevi[k])):
        #     if samo_plusevi[k][j] != 0:
        #         print("samo_plusevi:",samo_plusevi[k][j])
        #         print("\nMatrica[k] = ", matrix[k])
        if (matrix[k][i] != samo_plusevi[k][i] and samo_plusevi[k][i] != 0):
            # print('OVO JE NETACNO::::', samo_plusevi[k][i])
            return True
    # Treba da pitas dal je <zuta> na mestu gde treba, ako nije preskoci.
    # Ako je zuta unutra, treba da bude na prvom mestu. Ako nije, false
    return False


def isprazni_fajl():
    with open("stablo.txt", "w") as file:
        file.write('')


def upisi_u_fajl(str, end='\n'):
    with open("stablo.txt", 'a') as file:
        file.write(str + end)


def upisivanje_u_stablo_fajl(root):
    isprazni_fajl()
    upisi_u_fajl("------ ISPIS STABLA ------")
    red = [root]
    br = 0
    br1 = 0
    kon = []
    loading_counter = 0
    limit = 30
    while len(red) > 0:
        for i in range(len(pojmovi)):
            for j in range(len(pojmovi[0])):
                for k in range(m):
                    x = Node()
                    x.info = prekopiraj_info(red[0])
                    if jeste_u_matrici(pojmovi[i][j], x.info):
                        continue
                    y = prekopiraj_info(x)
                    x.info[k] = replace_element_in_list(x.info[k], '_', i, j)
                    if x.info == y:
                        continue
                    if preklapa_se_sa_plusevima(x.info, k, i):
                        continue
                    red.append(x)

                    br += 1
                    print_matrix_file(x.info)
                    if x.info == tacni_pojmovi:
                        br1 += 1
                        upisi_u_fajl(f"Tacno rešenje.  ({br1}.)")
        kon.append(red[0])
        red.remove(red[0])
        loading_counter+=1
        if loading_counter >= limit:
            print_c2("█",end='')
            loading_counter = 0
            limit = limit*1.2
    upisi_u_fajl("Duzina stabla je ", str(len(kon)))


def upisivanje_u_stablo(root):
    print("-" * 30)
    red = [root]
    br = 0
    br1 = 0
    kon = []
    while len(red) > 0:
        for i in range(len(pojmovi)):
            for j in range(len(pojmovi[0])):
                for k in range(m):
                    x = Node()
                    x.info = prekopiraj_info(red[0])
                    if jeste_u_matrici(pojmovi[i][j], x.info):
                        continue
                    y = prekopiraj_info(x)
                    x.info[k] = replace_element_in_list(x.info[k], '_', i, j)
                    if x.info == y:
                        continue
                    if preklapa_se_sa_plusevima(x.info, k, i):
                        continue
                    red.append(x)

                    br += 1
                    print_matrix(x.info)
                    if x.info == tacni_pojmovi:
                        br1 += 1
                        print_c1(f"Tačno rešenje.  ({br1}.)")
        kon.append(red[0])
        red.remove(red[0])
    print("Duzina stabla je ", len(kon))


# [['plava', 'zuta', 'zelena'], ['telefon', 'racunar', 'sveska']]


def stvaranje_stabla():
    koren = Node()
    koren.add_child(3) \
        .add_next(2) \
        .add_child(8) \
        .add_next(1) \
        .add_next(0) \
        .add_child(4) \
        .add_next(5) \
        .add_next(6) \
        .add_next(7) \
        .add_child(1) \
        .add_next(2)
    print("\nPreorder:")
    preorder(koren)


# endregion

# region Stek
def push(node):
    stek.append(node)


def pop():
    if (not empty_stack()):
        x = stek[len(stek) - 1]
        stek.remove(stek[len(stek) - 1])
        return x


def empty_stack():
    return len(stek) == 0


# endregion


# region Bojenje
def print_rgb_bg(text, r, g, b, r1, g1, b1, end='\n'):
    print('\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + ';48;2;' + str(r1) + ';' + str(g1) + ';' + str(
        b1) + 'm' + text + '\033[0m', end=end)


def print_rgb(text, r, g, b, end='\n'):
    print('\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm' + text + '\033[0m', end=end)


def print_c1(text, end='\n'):
    print_rgb(text, 57, 250, 254, end=end)


def print_c2(text, end='\n'):
    print_rgb(text, 30, 200, 130, end=end)

def print_c3(text, end='\n'):
    print_rgb(text, 200, 100, 100, end=end)


# endregion

def ispis_stanja():
    print_c1("╭──═━┈┈┈━═──╮" * len(dict))
    for key in dict:
        print_c1(f"│{key.center(11)}│", end='')
    print()
    pomocna = korisnik
    pomocna = [[pomocna[j][i] for j in range(len(pomocna))] for i in range(len(pomocna[0]))]
    for i in range(len(pomocna)):
        for j in range(len(pomocna[0])):
            print_c1('│', end='')
            print_c1(f'{pomocna[i][j]}'.center(11), end='')
            print_c1('│', end='')
        print()
    print_c1("╰──═━┈┈┈━═──╯" * len(dict))

def potez():
    print_c1("╭──═━┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈━═──╮".center(40))
    print_c1("│                   Ispišite osobine                   │".center(40))
    print_c1("│                                                      │".center(40))
    print_c1("│       Ukoliko zelite da uparite pojam, napisite      │".center(40))
    print_c1("│       ime kolone u koju zelite da dodate pojam.      │".center(40))
    print_c1("│                                                      │".center(40))
    print_c1("│                     ime + osobina                    │".center(40))
    print_c1("│                                                      │".center(40))
    print_c1("│            Za povratak nazad, napišite '0'           │".center(40))
    print_c1("╰──═━┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈━═──╯".center(40))
    op = -1
    while(op != '0'):
        ispis_stanja()
        op = input().strip()
        if op =='0':
            break
        if '+' in op:
            op = op.split('+')
        else:
            continue
        vrsta = op[0].strip()
        found = False
        i = 0
        for key in dict:
            if key == vrsta:
                vrsta = i
                found = True
                break
            i+=1
        if not found:
            print_c3("Niste lepo uneli ime.")
            continue
        pojam = op[1].strip()
        kolona = -1
        for i in range(len(pojmovi)):
            if pojam in pojmovi[i]:
                kolona = i
                break
        if(kolona == -1):
            print_c3("Uneli ste nepostojeci pojam...")
            continue
        korisnik[vrsta][kolona] = pojam

def pomoc():
    if tacni_pojmovi == -1:
        print_c2("\n➤ Rešenje ne postoji, te nema razloga za pomoć!\n")
        return
    if korisnik == tacni_pojmovi:
        print_c2("\n➤ Već ste popunili ispravno!\n")
        return False
    flag = True
    for i in range(len(korisnik)):
        for j in range(len(korisnik[0])):
            if korisnik[i][j] == '_': continue

            if not korisnik[i][j] in tacni_pojmovi[i]:
                flag = False
    if flag is False:
        print_c3("➤ Neispravno popunjeni pojmovi. Pomoć nedostupna...")
        return False
    for i in range(len(korisnik)):
        for j in range(len(korisnik[0])):
            if korisnik[i][j] == '_':
                korisnik[i][j] = tacni_pojmovi[i][j]
                return True

def igraj():
    print_c1("\n")
    print_c1("╭──═━┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈━═──╮".center(40))
    print_c1("│   Dobrodošli u igru!   │".center(40))
    print_c1("╰──═━┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈━═──╯".center(40))
    option = -1
    while (option != '0'):
        if option not in ['3','4']:
            print_c1("╭──═━┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈━═──╮".center(40))
            print_c1("│   Interaktivni meni    │".center(40))
            print_c1("│                        │".center(40))
            print_c1("│   1. Odigrajte         │".center(40))
            print_c1("│   2. Ispis stabla      │".center(40))
            print_c1("│   3. Proveri tačnost   │".center(40))
            print_c1("│   4. Pomoć             │".center(40))
            print_c1("│   0. Izlaz             │".center(40))
            print_c1("╰──═━┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈━═──╯".center(40))
        print_c2("\n╭─➤Unesite neku od opcija iz menija: ")
        print_c2("╰┈➤ ", end='')
        option = input()
        if option == '0':
            print_c3("\n\n")
            print_c3("╭──────────══─────────╮".center(32))
            print_c3("│   Igra je zavrsena. │".center(32))
            print_c3("╰──────────══─────────╯".center(32))
            print_c1(" ╭──────────══─────────╮".center(30))
            print_c1("│ Vidimo se uskoro 😎 │".center(30))
            print_c1(" ╰──────────══─────────╯".center(30))
        elif option == '1':
            potez()
        elif option == '2':
            print_c2("\n➤ Kreiranje stabla...\n➤ Upisivanje u fajl: ",end='')
            upisivanje_u_stablo_fajl(root)
            print_c2(" 100% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴'.\n")
            print_c2("\n➤ Stablo je upisano u fajl 'stablo.txt'.\n")
        elif option == '3':
            if tacni_pojmovi == -1:
                print_c1("╭──══──╮".center(40))
                print_c1("│ 𝙽𝚘𝚗𝚎 │".center(40))
                print_c1("╰──══──╯".center(40))
            else:
                flag = True
                for i in range(len(korisnik)):
                    for j in range(len(korisnik[0])):
                        if korisnik[i][j] == '_': continue

                        if not korisnik[i][j] in tacni_pojmovi[i]:
                            flag = False
                if flag is True:
                    print_c1("╭──══──╮".center(40))
                    print_c1("│  👍🏻  │".center(40))
                    print_c1("╰──══──╯".center(40))
                else:
                    print_c3("╭──══──╮".center(40))
                    print_c3("│  👎🏻  │".center(40))
                    print_c3("╰──══──╯".center(40))
        elif option =='4':
            print(tacni_pojmovi)
            if pomoc():
                ispis_stanja()


stek = []
m = int(input())
n = int(input())
kon = []
prvi_red = input().split(',')
dict = {}
pojmovi = []
samo_plusevi = [[0 for j in range(n - 1)] for i in range(m)]
unos_pojmova()

sve_ok = obrada_uslova()
if sve_ok:
    tacni_pojmovi = vrati_tacne_pojmove()
else:
    tacni_pojmovi = -1
root = Node()

korisnik = [['_' for j in range(n - 1)] for i in range(m)]
igraj()
