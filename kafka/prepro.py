import json
from ast import literal_eval

input = b'{"BasicLog":{"UserIpAddress":"211.253.124.52","MemberNo":"17016875","RequestDateTime":"2020-06-17 15:45:36","AbsoluteUrl":"http://www.yes24.com/Product/Goods/80093472?pid=95609","ReferrerUrl":"http://www.yes24.com/Cooperate/Naver/welcomeNaver.aspx?pageNo=1&goodsNo=80093472","HttpStatusCode":"200","HttpMethod":"POST","UserAgent":"Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko","LogKindCode":"006_006","PageCode":"IAA","LanguageCode":"ko-KR","PCID":"15923757520291596799779","GUID":"847fa9ed-ed25-44fe-a497-9e3fa2e96b20","DeviceType":"P","CoordinateX":"1320","CoordinateY":"1320"},"UrlLog":{"HostName":"www.yes24.com","Path":"/Product/Goods/80093472","Protocol":"http"},"DeviceLog":{"OS":"Windows","Platform":"Win32","BrowserInfo":null,"Resolution":"1600x900","ColorDepth":"24"},"MemberLog":{"MemberGb":"01","MemberAge":"52","MemberCartNo":"17016875"}}'
result = input.decode("utf-8")

print('string type: {}'.format(type(result)))

# convert string to dictionary
result_json = json.loads(result)

print(result_json)
print(type(result_json))
print(result_json.get("BasicLog.PCID", '15923757520291596799779'))

