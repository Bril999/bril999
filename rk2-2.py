'''rk2 второй номер'''
if __name__=='__main__':
    with open ('stdin1.txt', 'r', encoding = 'utf-8') as file1, open ('stdin2.txt', 'r', encoding = 'utf-8') as file2:
        adge1, adge2 = ''.join(i for i in file1.read()), ''.join(i for i in file2.read())
    file1.close()
    file2.close()
    if int(adge1) == int(adge2):
        with open ('stdout.txt', 'w', encoding = 'utf-8') as file3:
            PERIMETR = (int(adge1) + int(adge2))*2
            SQUARE = int(adge1)*int(adge2)
            STRR1 = str(PERIMETR)
            STRR2 = str(SQUARE)
            file3.write(STRR1)
            file3.write(STRR2)
        file3.close()
    else:
        with open ('stdout.txt', 'w', encoding = 'utf-8') as file4:
            PERIMETR1 = (int(adge1) + int(adge2))*2
            STRR = str(PERIMETR1)
            file4.write(STRR)
        file4.close()
