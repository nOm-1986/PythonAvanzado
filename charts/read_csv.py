import csv
import matplotlib.pyplot as plt

FILE_URL = "d:/Development/Python/PythonIntermedio/InterNico/FilesExcel/world_population.csv"

def read_csv(path)->dict:
    data = []
    with open(path, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        for row in csv_reader:
            iterable = zip(header, row)
            country_dict = {k:v for k,v in iterable}
            data.append(country_dict)
    return data

def generate_chart(labels, data, name):
    fig, ax = plt.subplots()
    ax.pie(data, labels=labels)
    ax.axis('equal')
    file_name= name +'.png'
    plt.savefig(file_name)
    plt.show()

def run():
    data = read_csv(FILE_URL)
    select_country = input('Ingresa un continente: \n')
    try:
        filtro = list(filter(lambda x: x['Continent'] == select_country, data))
    except Exception as e:
        print(e)
    lab = list(map(lambda x: x['Country/Territory'], filtro))
    per = list(map(lambda x: x['World Population Percentage'], filtro))
    generate_chart(lab, per, select_country)

if __name__ == '__main__':
    run()

