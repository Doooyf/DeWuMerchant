import hashlib
import requests

# 请求头
headers = {
            "channel": "pc",
            "clientid": "stark",
            "content-type": "application/json;charset=UTF-8",
            "passporttoken": "{Token}", # 用户登陆后的token
            "syscode": "DU_USER"
        }

def getSign(data=None):
    """
    获取签名

    加密说明：
        通过ASCII排序，进行拼接字符串，再由md5加密得到sign，例如："pageNo1pageSize20" + "048a9c4943398714b356a696503d2d36" = "pageNo1pageSize20048a9c4943398714b356a696503d2d36"

    :param data: 请求参数
    :return: md5加密字符串
    """
    if data is None:
        data = dict()

    requestStr = ""

    if (len(data) > 0):
        # 数组排序
        data = sorted(data.items())
        
        # 生成字符串
        i = 0
        while i < len(data):
            requestStr += str(data[i][0]) + str(data[i][1])
            i += 1

    requestStr += "048a9c4943398714b356a696503d2d36"
    # md5原始sign的字符串
    m = hashlib.md5()
    m.update(requestStr.encode("utf8"))
    sign = m.hexdigest()
    return sign

def request(params):
    """
    请求参数处理
    :param params: 请求参数
    :return: params
    """
    if len(params) > 0:
        params["sign"] = getSign(params)
    else:
        params = dict()
        params["sign"] = getSign()
    return params
def headers():
    """
    docstring
    """
    pass

def get(url, params):
    params = request(params)
    res = requests.get(url, params=params, headers=headers)
    return res

res = get("{url}", [])
if res.status_code == 200:
    print("请求成功")