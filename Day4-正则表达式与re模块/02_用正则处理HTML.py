import re

f = open('top250.html','r',encoding='utf-8')
content = f.read()
f.close()
"""
获取排名，名称，导演，主演，评分，评价
"""

# obj = re.compile(r'<div class="item">.*?<em>(?P<rank>.*?)</em>.*?<span class="title">(?P<name>.*?)</span'
#                  r'>.*?导演: (?P<director>.*?)&nbsp;&nbsp;&nbsp;主演: (?P<actors>.*?)<br>.*?<span class="rating_num" prope'
#                  r'rty="v:average">(?P<score>.*?)</span>.*?<p class="quote">.*?<span>(?P<remark>.*?)</span>.*?</div>',re.S)
# r = obj.finditer(content)
# for item in r:
#     rank = item.group('rank')
#     name = item.group('name')
#     director = item.group('director')
#     actors = item.group('actors')
#     score = item.group('score')
#     remark = item.group('remark')
#     print(rank,name,director,actors,score,remark)

obj_li = re.compile(r'<li>(?P<li>.*?)</li>',re.S)
# 分解提取每一项
obj_rank = re.compile(r'<em>(?P<rank>.*?)</em>',re.S)
obj_name = re.compile(r'<span class="title">(?P<name>.*?)</span>',re.S)
obj_director = re.compile(r'导演: (?P<director>.*?)&nbsp;',re.S)
obj_actors = re.compile(r'主演: (?P<actors>.*?)<br>',re.S)
obj_score = re.compile(r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>',re.S)
obj_remark = re.compile(r'<p class="quote">.*?<span>(?P<remark>.*?)</span>',re.S)
li_list = obj_li.finditer(content)
for li in li_list:
    li_code = li.group('li')
    # print(li_code)
    # print("=================================")
    rank=obj_rank.search(li_code).group('rank')
    name=obj_name.search(li_code).group('name')
    director=obj_director.search(li_code).group('director')
    actors1=obj_actors.search(li_code)
    if actors1:
        actors=actors1.group('actors')
    else:
        actors="..."
    score=obj_score.search(li_code).group('score')
    remark1=obj_remark.search(li_code)
    if remark1:
        remark=remark1.group('remark')
    else:
        remark="..."
    print(rank,name,director,actors,score,remark)