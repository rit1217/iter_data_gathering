import requests
import json
import os


def get_raw_detail():
    places_f = open('../temp/places.json', 'w')
    places_f.write('[')
    places_file = open('../temp/places2.json', 'r')
    places = json.load(places_file)
    response = True
    pageNo = 1
    cnt = 0


    for i in places['data']:
        try:
            response = requests.get("https://tatapi.tourismthailand.org/tatapi/v5/" + i['category_code'].lower() + '/' + i['place_id'] ,
                            headers = {
                                "Accept": "*/*",
                                "Authorization": os.environ['TAT_API_KEY'],
                                "Accept-Language": "EN"
                            })
            pageNo += 1
            data = response.json()['result']
            for j in data.keys():
                i[j] = data[j]
            places_f.write(json.dumps(i))
            places_f.write(',')
            cnt += 1
        except:
                print(i['category_code'], i['place_id'])

    print(cnt)
    places_f.write(']')    