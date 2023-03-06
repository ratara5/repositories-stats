import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        header = next(reader) #Obtener la primera fila de forma manual, la cual contiene los encabezados de las columnas del CSV
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
    return data

if __name__ == '__main__':
    data = read_csv('./my_app/data.csv')
    print(data)