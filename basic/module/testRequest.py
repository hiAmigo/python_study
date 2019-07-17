import requests

# r = requests.get('http://www.douban.com/search', params={'q':'python', 'cat':'1001'})

# print(r.url)
# print(r.status_code)
# print(r.encoding)
# print(r.content)
# print(r.text)

r1 = requests.post('http://www.douban.com/serch', data={'q':'python'})
