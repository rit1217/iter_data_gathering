import requests
import json
import os


def get_raw_data():
    places_f = open('../temp/places2_TH.json', 'w')
    # places = pd.read_csv('place_new.csv.gz', usecols=['place_id']).astype(str)
    response = True
    # places = places['place_id'].to_list()
    pageNo = 1
    cnt = 0
    common = 0
    places_f.write('[')
    try:
        while response:
            response = requests.get("https://tatapi.tourismthailand.org/tatapi/v5/places/search",
                            headers = {
                                "Accept": "*/*",
                                "Authorization": os.environ['TAT_API_KEY'],
                                "Accept-Language": "EN"
                            },
                            params = {
                                'numberOfResult':100,
                                'pagenumber':pageNo
                            })
            pageNo += 1
            data = response.json()['result']
            for i in data:
                places_f.write(json.dumps(i))
                places_f.write(',')
                cnt += 1
                # if i['place_id'] in places:
                #     common += 1
    except Exception:    
        print(cnt)
        # print('common:', common)
        places_f.write(']')