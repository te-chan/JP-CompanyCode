import os
import requests
import pandas as pd

kabu_excel = "https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls"

def get_company_list_from_csv():
    # donwload kabu xls
    res = requests.get(kabu_excel)
    with open('data.xls', 'wb') as f:
        f.write(res.content)
    
    df = pd.read_excel('data.xls', sheet_name='Sheet1', header=None)
    code_and_name = [[str(row[1]), row[2]] for row in df.values][1:]

    # save to csv
    df = pd.DataFrame(code_and_name, columns=['code', 'name'])
    df.to_csv('company_list.csv', index=False)

if __name__ == '__main__':
    get_company_list_from_csv()
    os.remove('data.xls')