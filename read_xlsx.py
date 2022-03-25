from pandas import read_excel

def read(file):
     df = read_excel(file)
     d = {}
     
     for key in df.keys():
          d[key] = list(df[key])
          
     return d


if __name__ == "__main__":
     r = read_xlsx("usuarios.xlsx")
     print(r)
