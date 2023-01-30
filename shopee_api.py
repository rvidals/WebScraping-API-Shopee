import requests
import json
from datetime import datetime
from tqdm import tqdm
import pandas as pd


carl = 'regata nba masculina'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}


def get_url():

    api_urls = []

    for i in range(0, 18):
        #O url verificar se a url existe e é compativel com a api_url
        # url = f'https://shopee.com.br/search?keyword=regata%20nba%20masculina&page={i}'
        api_url = f'https://shopee.com.br/api/v4/search/search_items?by=relevancy&keyword=regata%20nba%20masculina&limit=60&newest={i * 60}&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2&view_session_id=cc3a916a-a3ef-4c3d-afa2-f923d7c8a6af'
        api_urls.append(api_url) 

    return api_urls
    # print(url)
    # print(api_url)
    # print('======================')

def scrape(url):

    req = requests.get(url, headers=headers).json()

    linhas = req['items']

    data = []

    for i in range(0, len(linhas)):
        name  = req['items'][i]['item_basic']['name']
        price  = float(req['items'][i]['item_basic']['price'] / 100000)
        price_before_discount = float(req['items'][i]['item_basic']['price_before_discount'] / 100000)
        price_min  = float(req['items'][i]['item_basic']['price_min'] / 100000)
        price_min_before_discount = float(req['items'][i]['item_basic']['price_min_before_discount'] / 100000)
        price_max  = float(req['items'][i]['item_basic']['price_max'] / 100000)
        price_max_before_discount = float(req['items'][i]['item_basic']['price_max_before_discount'] / 100000)
        discount = req['items'][i]['item_basic']['discount']
        shop_location  = req['items'][i]['item_basic']['shop_location']
        shopid  = req['items'][i]['item_basic']['shopid']
        itemid = req['items'][i]['item_basic']['itemid']
        historical_sold  = req['items'][i]['item_basic']['historical_sold']
        stock = req['items'][i]['item_basic']['stock']
        link = f"https://shopee.com.br/{name.replace(' ','-')}-i.{shopid}.{itemid}"
        rating_star  = req['items'][i]['item_basic']['item_rating']['rating_star']
        rating_0  = req['items'][i]['item_basic']['item_rating']['rating_count'][0]
        rating_1  = req['items'][i]['item_basic']['item_rating']['rating_count'][1]
        rating_2  = req['items'][i]['item_basic']['item_rating']['rating_count'][2]
        rating_3  = req['items'][i]['item_basic']['item_rating']['rating_count'][3]
        rating_4  = req['items'][i]['item_basic']['item_rating']['rating_count'][4]
        rating_5  = req['items'][i]['item_basic']['item_rating']['rating_count'][5]

        data.append(
                    (name, price, price_before_discount, price_min,
                     price_min_before_discount, price_max, price_max_before_discount, 
                     discount, shop_location,  shopid, itemid, historical_sold, stock, rating_star, 
                     link, rating_0, rating_1, rating_2, rating_3, rating_4, rating_5)
                    )

    return data 

def data_frame(data):
    df = pd.DataFrame(data, 
                         columns=['name', 'price', 'price_before_discount', 'price_min', 
                         'price_min_before_discount','price_max','price_max_before_discount',
                         'discount','shop_location',  'shopid', 'itemid', 'historical_sold', 'stock','rating_star', 
                         'link', 'rating_0', 'rating_1', 'rating_2', 'rating_3', 'rating_4', 'rating_5']
                     )
    return df
    
def save_to_excel(df, nome_excel, pesquisa):
    date = datetime.now().strftime("%Y%m%d-%H-%M-%S")
    df.to_excel(nome_excel + '_' + date + '.xlsx', 
                sheet_name=pesquisa,
                index=False)
    print('Pesquisa Salva em Excel')

    
# def save_to_excel(df):
#     df.to_excel('Camisas da NBA - Shopee.xlsx', 
#                 index=False)
#     print('Pesquisa Salva em Excel')

if __name__ == '__main__':
    urls = get_url()

    dt_all = []
    for i in tqdm(range(0, len(urls))):
        url = urls[i]
        # print(url)
        scrapes = scrape(url)
        # print(scrape)
        dt_all.extend(scrapes)

    df = data_frame(dt_all)
    # print(df['link'])
    # save_to_excel(df)
    save_to_excel(df, 
                'Camisas da NBA - Shopee',
                'Pesquisa_01')


