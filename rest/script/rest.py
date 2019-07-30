import requests
import  json
import os

AUTH_ENDPOINT="http://127.0.0.1:8000/api/auth/register/"
refresh_point="http://127.0.0.1:8000/api/auth/jwt/refresh/"
ENDPOINT ="http://127.0.0.1:8000/api/status/"


img_pth =os.path.join(os.getcwd(),"l.jpg")

post_headers={
    "content-Type":"application/json",
    "Authorization":"JWT"+"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5LCJ1c2VybmFtZSI6InMxMyIsImV4cCI6MTU2NDQ3NjQwNSwiZW1haWwiOiJzMTNAZ21haWwuY29tIiwib3JpZ19pYXQiOjE1NjQ0NzYxMDV9.5Wh9SwVseIN9J9pndK7W8Kjge9QVuW0_JHNuK-Ow9EQ"
}

data={
    "username":"s14",
    "email":"s14@gmail.com",
    "password":1234,
    "password2":1234,

}

r       =  requests.post(AUTH_ENDPOINT,data=json.dumps(data),headers=post_headers)
token   =  r.json()#['token']
print (token)

# refresh_data={
#     "token":token
# }
# new=requests.post(refresh_point,data=json.dumps(refresh_data),headers=post_headers)
    # new_token=new.json()
# print (new_token)

# headers={
#      # "content-type":"application/json",
#     "Authorization":"JWT "+token
# }
# with open(img_pth,'rb') as image:
#
#     file_data={
#                  'image':image
#              }
#     ddata={}
#     r =requests.post(ENDPOINT,data=ddata ,headers=headers,files=file_data)
#     print(r.text)

# post_response=requests.request('post',ENDPOINT,data=post_data,headers=post_headers)
# print (post_response.text)
# /def do_img(method="get",data={},is_json=True,img_pth=None):
#     headers={}
#     if is_json:
#         # headers['content-type']='application/json'
#         data=json.dumps(data)
#     if img_pth is not None:
#         with open(img_pth,'rb') as image:
#             file_data={
#                 'image':image
#             }
#             r =requests.request(method,ENDPOINT,data=data ,headers=headers,files=file_data)
#     else:
#         r = requests.request(method, ENDPOINT, data=data,headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r
#
# def do(method="get",data={},is_json=True):
#     headers={}
#     if is_json:
#         headers['content-type']='application/json'
#         data=json.dumps(data)
#     r =requests.request(method,ENDPOINT,data=data ,headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r
#
# # do(data={'id':3})
# do_img(method='put',data={"id":14,"user":1,"content":"dhdjdbhjdhd"} ,is_json=False,img_pth=img_pth)
# # do(method='put',data={"id":7,"content":"something new","user":1})
# # do(method='post',data={"content":"something ndsdkjsdjsdksajdew","user":1})