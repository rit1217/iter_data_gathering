import requests
import json
import os
from .config import FILEPATHS


def get_raw_data():
    language = 'EN'
    raw_data_file = open(FILEPATHS[f'raw_data_{language}'], 'w+')
    missing_detail_file = open(FILEPATHS[f'missing_detail_{language}'], 'w+')
    response = True
    pageNo = 1
    
    raw_data_file.write('[')
    missing_detail_file.write('[')

    try:
        while response:
            response = requests.get("https://tatapi.tourismthailand.org/tatapi/v5/places/search",
                            headers = {
                                "Accept": "*/*",
                                "Authorization": os.environ['TAT_API_KEY'],
                                "Accept-Language": language
                            },
                            params = {
                                'numberOfResult':100,
                                'pagenumber':pageNo
                            })
            pageNo += 1
            data = response.json()['result']
            for i in data:
                query = "https://tatapi.tourismthailand.org/tatapi/v5/" + i['category_code'].lower() + '/' + i['place_id'] 
                detail_response = requests.get(query,
                            headers = {
                                "Accept": "*/*",
                                "Authorization": os.environ['TAT_API_KEY'],
                                "Accept-Language": language
                            })
                if detail_response.status_code == 200:
                    detail = detail_response.json()['result']

                    # detail not containing category
                    detail['category_code'] = i['category_code']
                    detail['category_description'] = i['category_description']
                    raw_data_file.write(json.dumps(detail))
                    raw_data_file.write(',')
                    cnt += 1
                else:
                    missing_detail_file.write(json.dumps(i))
                    missing_detail_file.write(',')
                    mcnt += 1

    except Exception as e:    
        # no more response
        print(e, 'collected: ' cnt, ', missing detail: ', mcnt)
        raw_data_file.write(']')
        missing_detail_file.write(']')
