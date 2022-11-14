'''первый номер рк'''
def perimetr_func(adge1, adge2):
    '''функция для подсчёта периметра и площади'''
    if adge1 == adge2:
        print('Периметр: ', adge1*4, 'Площадь: ', adge1**2)
    else:
        print('Периметр: ', (adge1 + adge2)*2)
if __name__=='__main__':
    perimetr_func(int(input('Введите первое число ')), int(input('Введите второе число ')))
