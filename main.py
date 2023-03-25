import uproot
import sys

filename = sys.argv[1]
tuptype = sys.argv[2]

print(f'got {filename} filename')

with uproot.open(filename) as file:
    # Смотрим, какие структуры данных находятся в файле
    # file.keys()
    # Видим, что в данном случае есть TTree с названием "GammaLeak"
    # Достаём его оттуда
    ttree = file['Universal Ntuple']
    # Посмотрим на то, какие колонки имеются 
    # ttree.show()
    # xPos yPos zPos xDir yDir zDir len E
    # Распакуем его в совокупность массивов
    # Тут все зависит от того, какую имплементацию использовать, я хочу пандас
    data = ttree.arrays(["type", "xPos", "yPos", "zPos", "xDir", "yDir", "zDir", "len", "E"], library='pd')
    data.info()
    filtered = data.loc[data["type"] == int(tuptype)]
    filtered.info()

    # data.to_csv(filename[:-5] + '-' + tuptype + '.csv')
    #filtered = data.loc[data["type"] == 1]
    filtered.to_csv(filename[:-5] + '-' + tuptype + '.csv')

