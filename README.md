# 得物App商户后台 sign破解 部分接口统计

>（本项目仅用于学习用途，使用本项目的一切后果自负，如果得物app看到本项目觉得需要删除请联系邮箱）。

## 说明
APP的破解接口sign详情可见[luo1994/du-app-sign](https://github.com/luo1994/du-app-sign)

本破解方式也适用于APP端和小程序端的接口

> 登录可使用模拟点击登录进入，获取Token
## 文档

 > 必带请求头
channel:pc
clientid:stark
content-type:application/json;charset=UTF-8
passporttoken: {mchToken}
syscode:DU_USER

> sign加密方式：<br/> 请求参数按ASCII码排序，拼接 字符串 + "048a9c4943398714b356a696503d2d36" <br/>如下

```
pageSize: 20
pageNo: 1

// 排序
pageNo: 1
pageSize: 20

// 拼接字符串
"pageNo1pageSize20" + "048a9c4943398714b356a696503d2d36" = "pageNo1pageSize20048a9c4943398714b356a696503d2d36"
```

### 商家信息

请求方式：get

https://stark.dewu.com/api/v1/h5/biz/home/merchantInfo?sign=fe26befc49444d362c8f17463630bdba
---
### 出价列表

请求方式：post

https://stark.dewu.com/api/v1/h5/biz/bidding/biddingList
请求参数：
```
biddingModel: 1
biddingType: "0"
pageNo: 1
pageSize: 20
sellerPriceType: 1 // 出价价格 （>当前渠道最低价）
sign: "897ccf162c15dc2900cc7a513a2b80ce"
```
---
### 待发货订单列表

请求方式：post

https://stark.dewu.com/api/v1/h5/biz/orders/list
请求参数
```
becomingDeliverTimeOut: false
bizType: "0"
endTime: "2021-01-04 23:59:59"
pageNo: 1
pageSize: 20
sign: "61f703c64ecb25eb0dcca204563f55b8"
startTime: "2020-11-30 00:00:00"
status: 1 // 待发货的订单状态
subTypeListString: "0,13"
```
---
### 商品出价查询

请求方式：post

https://stark.dewu.com/api/v1/h5/biz/search/newProductSearch
请求参数
```
articleNumberStr: "关键词" // 型号搜索内容
productNameStr: "关键词" // 商品搜索内容
biddingType: "0"
page: 1
pageSize: 20
sign: "94daf216b5b511d54c43ef980668c563"
```
---
### 商品出价规格查询

请求方式：GET

https://stark.dewu.com/api/v1/h5/biz/newBidding/queryPropsBySpuId
请求参数
```
spuId: 1204463
sign: 0638e9f893a1db3a155c25ec62b63713
```
### 商品详情

请求方式 GET

https://stark.dewu.com/api/v1/h5/biz/bidding/detail
请求参数：
```
spuId: 1204463
biddingType: 0
sign: b4194769ec14f37dc3f63a72d9a802c8
```
---
### 商品下架

请求方式：post

https://stark.dewu.com/api/v1/h5/biz/newBidding/addOrUpdateSingleBidding
请求参数：
```
oldQuantity: 1
price: 79999
quantity: 0 // 数量设置 0 （下架）
sellerBiddingNo: "101220031986420892"
sellerBiddingType: 0
sign: "b0f0c4ac58ef329f62790d3d0ba1337a"
skuId: 601410696
type: 1
```
---
### 商品上架或修改

请求方式：post

https://stark.dewu.com/api/v1/h5/biz/newBidding/addOrUpdateSingleBidding
请求参数：
```
// 新增
price: 5999900 // 价格
quantity: 1 // 数量（库存）
sellerBiddingType: 0
sign: "0a82a73de6c418fe4e8f2a95fc5790bb"
skuId: 601410696
type: 1

// 修改
oldQuantity: 1
price: 6999900
quantity: 1
sellerBiddingNo: "101220031986378182"
sellerBiddingType: 0
sign: "acf4988d88c789759fd705eabf692c3f"
skuId: 601410696
type: 1
```

>（本项目仅用于学习用途，使用本项目的一切后果自负，如果得物app看到本项目觉得需要删除请联系邮箱）。