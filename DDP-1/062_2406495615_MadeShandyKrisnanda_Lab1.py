print(">>==========================<<")
print("||                     	   ||")
print("|| Welcome to Interrogation||")
print("||                     	   ||")
print(">>==========================<<")
print()

# membuat jawaban dalam variable
no_answer = ('n', 'N', 'no', 'No', 'NO')
yes_answer = ('y', 'Y', 'yes', 'Yes', 'YES')
all_answer = ('y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no', 'No', 'NO')

# meminta input untuk memulai interogasi 
has_ineterrogation = input("Mulai Interogasi(Y/N)?")
while has_ineterrogation not in all_answer:
    print('\ninput tidak valid')
    jawaban_interogasi = input("Mulai Interogasi(Y/N)?")
if has_ineterrogation in no_answer:
    print('Interogasi telah selesai\n')
    print('>>==========================<<')
    print('||                     	    ||')
    print('|| Ending the Interrogation ||')
    print('||                     	    ||')
    print('>>==========================<<')
while has_ineterrogation in yes_answer:
    print('Mari kita mulai interogasi\n')
    print()
    is_stop = False
    while is_stop == False:
        nama = input("Siapa namamu?")
        npm = input("Berapa nomor NPM mu?")
        digit_npm = 0 # menghitung jumlah digit pada npm
        for i in npm:
            digit_npm+=1
        if npm.isdigit()!= True: # memeriksa bentuk dari NPM
            print("NPM harus berupa angka!")
            print('------------------------------\n')
            continue
        elif int(digit_npm) != 10:
            print("NPM harus sepanjang 10 digits!")
            print('------------------------------\n')
            continue
        elif npm.isdigit() and int(digit_npm) == 10:
            has_motive = False
            has_alibi = False
            ask_motive = input("Apakah kamu punya motif (Y/N)?") # menanyakan kepunyaan motif
            if ask_motive in yes_answer:
                has_motive = True
                type_motive = input('motifnya apa?')
            elif ask_motive not in no_answer:
                print('seseorang bla bla')
                print('------------------------------\n')
                continue
            ask_alibi = input('Apakah punya alibi?') # menanyakan kepunyaan alibi
            if ask_alibi in yes_answer:
                has_alibi = True
                type_alibi = input('alibinya apa?')
            elif ask_alibi not in no_answer:
                print('seseorang bla bla')
                print('------------------------------\n')
                continue
            print()
            print(f"{nama} dengan NPM {npm}{' tidak' if has_motive == False else ''} memiliki motif {type_motive if has_motive == True else ''}{'tidak' if has_alibi == False else ''} 
                  memiliki alibi {type_alibi if has_alibi == True else ''}")
            if (has_motive and has_alibi) or (has_motive == False and has_alibi == False) :
                print(f'{nama} lumayan mencurigakan nih...')
            elif has_motive == False and has_alibi:
                print(f'{nama} tidak terlalu mencurigakan sih')
            elif has_motive and has_alibi == False:
                print(f'wah, {nama} mencurigakan nih >:(')
            print('------------------------------\n')
            lanjut_interogasi = input("Lanjut interogasi (Y/N))?") # meminta input user untuk melanjutkan interogasi
            while lanjut_interogasi not in all_answer:
                print()
                print('input tidak valid')
                lanjut_interogasi = input("Lanjut interogasi (Y/N))?")
            if lanjut_interogasi in (yes_answer):
                print('------------------------------\n')
                continue
            elif lanjut_interogasi in no_answer:
                print('Interogasi telah selesai\n')
                print('>>==========================<<')
                print('||                     	    ||')
                print('|| Ending the Interrogation ||')
                print('||                     	    ||')
                print('>>==========================<<')
                jawaban_interogasi = 'N'
                break
            while lanjut_interogasi not in (no_answer, yes_answer):
                print('\ninput tidak valid')
                lanjut_interogasi = input("Lanjut interogasi (Y/N))?")