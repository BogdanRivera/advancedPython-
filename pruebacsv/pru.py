import csv
def lee_csv(path):
  with open(path,'r') as file:
    reader = csv.reader(file,delimiter=',')
    header = next(reader)
    datos = []
    for row in reader:
      iterable = zip(header,row)
      country_dict = dict(iterable)
      datos.append(country_dict)
    return datos


if __name__=="__main__":
  datos = lee_csv("./pruebacsv/juegos.csv")
  print(datos[0],datos[1])
  
  