#-*- coding:utf-8 -*-

#- 工作经历

gj = ["应届毕业生","3年及以下","3-5年", "5-10年","10年以上","不要求"]

#- 学历

xl = [ "大专","本科","硕士","博士","不要求"]

#- 融资阶段

jd = ["未融资","天使轮","A轮", "B轮", "C轮","D轮及以上","上市公司","不需要融资"]

#- 行业领域

hy = ["移动互联网","电子商务","金融","企业服务","教育","文化娱乐","游戏","O2O","硬件","社交网络","旅游","医疗健康","生活服务","信息安全","数据服务","广告营销","分类信息","招聘","其他"]

#- 排序
px= ["new"]

#- 工作性质

gx = ["全职","兼职","实习"]

#- 月薪

yx = ["2k以下","2k-5k","5k-10k","10k-15k","15k-25k","25k-50k","50k以上"]


#- 工作性质

gx = ["全职","兼职","实习"]

#- 城市

city = ["北京","上海","深圳","广州","杭州","成都","南京","武汉","西安","厦门","长沙","苏州","天津","重庆","郑州","青岛","合肥","福州","济南","大连","珠海","无锡","佛山","东莞","宁波","常州","沈阳","石家庄","昆明","南昌","南宁","哈尔滨","海口","中山","惠州","贵阳","长春","太原","嘉兴","泰安","昆山","烟台","兰州","泉州","河源","淮南","镇江","三明","抚州","丽江", "漯河","宜春","丽水","池州","景德镇","佳木斯","恩施","莆田","日照","百色","马鞍山","莱芜","和田","滁州","东营","赣州","三亚","自贡","拉萨","凉山彝族自治州","保定","锦州","襄阳","邢台","大同","澳门特别行政区","濮阳","肇庆","滨州","抚顺","延边","乐山","绍兴","阳泉","荆州","巴中","宁德","鹤壁","邯郸","台州","潮州","黔南","信阳","九江","秦皇岛","茂名","沧州","塔城","德阳","梅州","南通","南阳","聊城","克拉玛依","淄博","徐州","芜湖","南平","鄂州","运城","香港特别行政区","营口","漳州","泸州","潍坊","淮安","湖州","吉林","阳江","毕节","乌鲁木齐","菏泽","淮北","蚌埠","玉林","盐城","泰州","新乡","孝感","葫芦岛","乌兰察布","云浮","西宁","株洲","黄冈","怀化","焦作","许昌","包头","宿州","鞍山","湛江","大理","牡丹江","永州","宜昌","雅安","呼和浩特","绵阳","扬州","桂林","榆林","宝鸡","十堰","广安","舟山"," 绥化","齐齐哈尔","银川","鄂尔多斯","玉溪","衢州","海东","六安","钦州","济宁","湘潭","晋中","江门","连云港","伊犁","内江","铁岭","临沂","温州","平顶山","承德","咸阳","柳州","晋城","白银","大庆","洛阳","通辽","阿克苏","周口","铜仁","岳阳","揭阳","南充","宿迁" ,"汕尾","上饶","遵义","萍乡","威海","安阳","台北","开封","河池" ,"衡阳","廊坊","汕头"," 德州","唐山","遂宁","安庆","娄底","清远","台中","辽阳","宜宾","金华","渭南","韶关","龙岩"]

city_dict = {"city":city}
hy_dict = {"hy":hy}
jd_dict = {"jd":jd}
xl_dict = {"xl":xl}
gj_dict = {"gj":gj}
yx_dict = {"yx":yx}
gx_dict = {"gx":gx}

filterbox = [city_dict,hy_dict,jd_dict,xl_dict,gj_dict,yx_dict,gx_dict]



agents = [
    "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
]