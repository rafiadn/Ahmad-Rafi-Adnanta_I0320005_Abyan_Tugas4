usia = float(input("Berapa usiamu kamu?: "))
x = str(input("Apakah Anda sudah lulus ujian kualifikasi? (Y/T): "))

if usia >= 21:
    if x == 'Y':
        print('Anda dapat mendaftar kursus.')
    elif x == 'T':
        print('Anda tidak dapat mendaftar kursus.')
    else:
        print('Anda tidak dapat mendaftar kursus.')
else :
    print('Anda tidak dapat mendaftar kursus.')