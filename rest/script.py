import requests
import json

BASE_URL="http://127.0.0.1:8000/"

END_POINT="api/"

def get():
    r=requests.get(BASE_URL + END_POINT)
    data=r.json()
    return data


# data=get()
# print(data)


def create_update():
    data={
        'id':1,
        "content":"anotydwwwweer one"
    }
    r =requests.post(BASE_URL+END_POINT,data=json.dumps(data))
    print(r.headers)
    print (r.status_code)
    if r.status_code==requests.codes.ok:
        return r.json()



# x=create_update()
# print (x)


def do_obj_update():
    data = {
        'user': 111,
        "content": "anotyer oa.d,mdsdmsd ne"
    }
    r = requests.put(BASE_URL + END_POINT+"6/", data=json.dumps(data))
    print(r.headers)
    print (r.status_code)
    if r.status_code == requests.codes.ok:
        return r.json()
print (do_obj_update())