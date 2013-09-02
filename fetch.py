# coding: utf-8
import requests
import re
from requests import *
import pyquery
from pyquery import PyQuery as pq
from lxml import etree
import urllib
import sys
import os


reload(sys)
sys.setdefaultencoding('utf8')

import config
from config import *

##########################################################################

_list_org_urls=["人物 | People","观点 | View",    "本期专题：再谈REST | Topic",
    "推荐文章 | Article", "特别专栏 | Column","避开那些坑 | Void","新品推荐 | Product"]

_urls={}
urls=[]
prod_urls=[]

for x in _list_org_urls:
    if x!='新品推荐 | Product':
        for y in org_urls[x]:
            _urls[y]=x
        urls+=org_urls[x]
    else:
        prod_urls=org_urls[x]



html_ = """
<html>
    <head>
        <link rel='stylesheet' href='../style/default.min.css'><script src='../style/highlight.pack.js'></script>
        <link rel="stylesheet" href="../style/print.css"/>
        <script>hljs.initHighlightingOnLoad();</script>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    </head>
    <body>
         <div class="page">
            <div class="head">
                <h1>{head}</h1>
            </div>
            <div class="title">
                <h1>{title}</h1>
            </div>
            <div class="author">
                {author}
            </div>
            {content}

            <div class="orglink">
                <p>
                    <strong>原文链接：<a href="{org}">{org}</a></strong>
                </p>
                <div>
                    {likes}
                </div>
            </div>
         </div>
    </body>
</html>"""


def get_rec(title, path, ids):
    data = requests.post(
        'http://www.infoq.com/api/recommendationlinks.action', {"topicIds": ids,
                                                                "title": title, "contentPath": path, "language": 'zh'
                                                                })
    import json
    _d = json.loads(data.content)
    return "".join('<li><a href="%s">%s</a></li>' % (x['url'], x['title']) for x in _d[1:] )


def get_article_content(url):
    data = requests.get(url)
    d = pq(data.content)
    pattern_pre = '{"topicIds": "(.*)", "title"'
    match_pre = re.findall(pattern_pre, data.content)
    title = d('title').text()
    print '    '+title
    author = d('.author_general').outerHtml().replace('href="/cn/author',
                                                      'href="http://infoq.com/cn/author').replace('<em>|</em>', '').replace('<em>/</em>', '')[:-72]
    content = d('.text_info_article').remove('.comments_like').remove('a[rel="permalink"]').remove('script').remove('.h1-r').remove('.related_sponsors').remove('.random_links').remove('.comment_here').remove('.comments').remove('.all_comments').remove(
        '#overlay_comments').remove('.related_sponsors').remove('#replyPopup').remove('#editCommentPopup').remove('#responseContent').remove('#messagePopup').remove('.related_sponsors').outerHtml().replace('src="/resource', 'src="http://www.infoq.com/resource').replace('<pre>','<pre><code>').replace('</pre>','</code></pre>')

    likes = ''
    try:
        likes = get_rec(title, url.replace(
            'http://infoq.com/cn', ''), match_pre[0])
        likes = ("<strong>相关内容</strong><ul>" + likes + "</ul>")
    except Exception, e:
        likes = ""
        print e

    return html_.format(head=_urls[url], title=title, author=author, content=content, likes=likes, org=url)


def get_news_content(url):
    data = requests.get(url)
    _data = data.content
    d = pq(_data)
    pattern_pre = '{"topicIds": "(.*)", "title"'
    _de_pattern = '发布于[\s\S]*<em>\|</em>'
    match_pre = re.findall(pattern_pre, _data)
    title = d('title').text()
    print '    '+title
    author = d('.author_general').outerHtml().replace('href="/cn/author',
                                                      'href="http://infoq.com/cn/author').replace('<em>|</em>', '').replace('<em>/</em>', '')[:-60]

    content = d('.text_info').remove('.comments_like').remove('a[rel="permalink"]').remove('script').remove('.h1-r').remove('.related_sponsors').remove('.random_links').remove('.comment_here').remove('.comments').remove('.all_comments').remove(
        '#overlay_comments').remove('.related_sponsors').remove('#replyPopup').remove('#editCommentPopup').remove('#responseContent').remove('#messagePopup').remove('.related_sponsors').outerHtml().replace('src="/resource', 'src="http://www.infoq.com/resource').replace('<pre>','<pre><code>').replace('</pre>','</code></pre>')
    likes = ''
    try:
        likes = get_rec(title, url.replace(
            'http://infoq.com/cn', ''), match_pre[0])
        likes = ("<strong>相关内容</strong><ul>" + likes + "</ul>")
    except Exception, e:
        print e
        likes = ""
    return html_.format(head=_urls[url], title=title, author=author, content=content, likes=likes, org=url)
def get_title(url):
    data = requests.get(url)
    _data = data.content
    d = pq(_data)
    title = d('title').text()
    print title
    return title
# 获取
def get_prod_content(url):
    html__='''
        <div class="title">
                <h2>{title}</h2>
            </div>
            <div class="author">
                {author}
            </div>
            {content}
            <div class="orglink">
                <p>
                    <strong>原文链接：<a href="{org}">{org}</a></strong>
                </p>

            </div>
    '''
    data = requests.get(url)
    d = pq(data.content)
    description = d('meta[name="description"]').attr('content')

    title = d('title').text()
    print '    '+title
    author = d('.author_general').outerHtml().replace('href="/cn/author',
                                                      'href="http://infoq.com/cn/author').replace('<em>|</em>', '').replace('<em>/</em>', '')[:-60]

    return html__.format( title=title, author=("<br6/>" + author), content=("<br/><p>" + description + "</p>"), org=url)

def gen_plant():
    html="""
    <html>
    <head>

        <link rel="stylesheet" href="../style/print.css"/>
        <link rel="stylesheet" href="../style/plant.css"/>

        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
      
    </head>
    <body>
         <div class="page">
            <div class="head">
                <h1>封面植物 </h1>
            </div>
            <div class="title">
                <h1>{plant_name}</h1>
            </div>
           
            <div class="text_info text_info_article">
                <p>
                <img style="max-width:200px;margin:5px;" src="../res/{plant_img}"/>{plant_desc}</p>                
                
            </div>
            </div>
            </body>
    """
    print '封面植物生成'
    with open(base_arch+'plant.html','w+') as f:
        f.write(html.format(plant_name=plant_name,plant_desc=plant_desc,plant_img=plant_img))
def gen_copy_right():
    html="""
<html>
    <head>

        <link rel="stylesheet" href="../style/print.css"/>
                <link rel="stylesheet" href="../style/copyright.css"/>

        <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.2.0/pure-min.css">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
       
    </head>
    <body>
         <div class="page">
            
                   <div class="pure-g">
    <div class="pure-u-3-8">
        <!--
        By default, grid units don't have any margin/padding.
        If you want to add these, put them in a child container.
        -->
        <img width="200px" src="http://www.infoq.com/resource/minibooks/architect-jun-10-2013/zh/cover/250.png"/>
    </div>

    <div class="pure-u-3-8">
        <h1>架构师 {which_month} 月刊</h1>
        <small>每月8日出刊</small>
        <br/>
        <p>本期主编：{chief_editor}<br/>
        美术/流程编辑：水羽哲<br/>
        总编辑：霍泰稳<br/>
        发行人：霍泰稳</p>
        <p>读者反馈：editors@cn.infoq.com<br/>
        投稿：editors@cn.infoq.com<br/>
        商务合作：sales@cn.infoq.com <br/>
        InfoQ 中文站：<a href="http://weibo.com/infoqchina">新浪微博</a></p>

    </div>
   
</div>
   <div class="pure-g" style="margin-top:70px;">
       <div class="pure-u">
        <table>
            <tr>
                <td width="10%">
                    
                </td>
                <td width="30px">
                     <img width="100px" src="../res/{chief_editor_image}"/> 
                </td>  <td width="10%">
                    
                </td>
                <td width="%"> 
                    <p style="font-size:13px;">{chief_editor_desc}</p>
                </td>
            </tr>
        </table>
       
</div>
  
   
</div>


   <div class="pure-g" style="margin-top:80px;margin-left:auto;margin-right:auto;">
    <div class="pure-u-1-5">
        <!--
        By default, grid units don't have any margin/padding.
        If you want to add these, put them in a child container.
        -->
        <img width="100px" src="http://cdn1.infoq.com/styles/i/logo_bigger.jpg"/>
    </div>

    <div class="pure-u-3-4">
        <p>《架构师》月刊由InfoQ 中文站出品。</p>
        
        <p>所有内容版权均属 C4Media Inc.所有，未经许可不得转载。</p>
    </div>
   
</div>
         
        </div>
    </body>
    """
    with open(base_arch+'right.html','w+') as f:
        f.write(html.format(chief_editor=chief_editor,chief_editor_desc=chief_editor_desc,
            which_month=which_month,chief_editor_image=chief_editor_image))
        print '版权页生成'
def gen_editor():
    html="""
    <html>
    <head>

        <link rel="stylesheet" href="../style/print.css"/>
        <link rel="stylesheet" href="../style/plant.css"/>

        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
      
    </head>
    <body>
         <div class="page">
            <div class="head">
                <h1>推荐编辑 | {recommand_editor_name} </h1>
            </div>
          
            <div class="text_info text_info_article">
                <p>
                <img style="max-width:200px;" src="../res/{recommand_editor_img}"/>{recommand_editor_desc}</p>                
                
            </div>
            </div>
            </body>
    """
    print '推荐编辑生成'
    with open(base_arch+'editor.html','w+') as f:
        f.write(html.format(recommand_editor_name=recommand_editor_name,recommand_editor_img=recommand_editor_img,recommand_editor_desc=recommand_editor_desc))



# 写入架构师的html文件

def gen_content():
    i = 0
    for x in urls:
        with open(base_arch+"%d.html" % i, 'w+') as f:
            if x.find('/news/') > 0:
                f.write(get_news_content(x))
            if x.find('/article') > 0:
                f.write(get_article_content(x))
            i += 1

# 写入架构师的新品推荐内容html文件
    with open(base_arch+"%d.html" % i, 'w+') as f:
        z = '''
        <html>
        <head>
    
            <link rel="stylesheet" href="../style/print.css"/>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        </head>
        <body>
             <div class="page">
                <div class="head">
                    <h1>新品推荐 | Product</h1>
                </div>
               '''
    
        for x in prod_urls:
            z += get_prod_content(x)
        f.write(z+           '''
             </div></body></html>''')
    i += 1
def gen_toc():
    with open(base_arch+'toc.html','w+') as f:
        html__='''
        <html>
        <head>
    
            <link rel="stylesheet" href="../style/print.css"/>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <style type="text/css">
                  img{
                    float: left;
                    margin-right: 8px;
                    margin-bottom: 5px；
                }
                           h1, h4{    color: rgb(24,103,45);                margin-bottom: 9px;                            -webkit-margin-before: 0.4em;

    }
    
                p{
    
                    margin: 0px;
                    line-height: 1.5;
                }
            </style>
        </head>
        <body>
             <div class="page">
                    <div class="toc" style="text-align: center;"><h1>目录</h1></div>'''
    
        for x in _list_org_urls:
            print x

            html__+=('<h4>'+x+'</h4>')
            for y in org_urls[x]:
                html__+=('<p>'+get_title(y)+'</p>')
        f.write(html__)
def gen_foreword():
    html="""
    <html>
    <head>

        <link rel="stylesheet" href="../style/print.css"/>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                   
    </head>
    <body>
         <div class="page" >
            <div class="head">
                <h1>卷首语 </h1>
            </div>
                <h1>{foreword_title}</h1>
           
            <div class="" style="-webkit-margin-before: 0em;">
               {forword_content}
            </div>
                
                        <div class="author">
                        本期主编：{chief_editor}
                    </div>
            </div>
            </body>
    """
    print '卷首语生成'
    with open(base_arch+'foreword.html','w+') as f:
        f.write(html.format(forword_content=forword_content,foreword_title=foreword_title,chief_editor=chief_editor))
def gen_topic():
    html="""
    <html>
    <head>

        <link rel="stylesheet" href="../style/print.css"/>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

    </head>
    <body>
         <div class="page" >
            <div class="head">
                <h1>推荐语 </h1>
            </div>
                <h1>{topic_title}</h1>
           
            <div class="" style="-webkit-margin-before: 0em;">
               {topic_desc}
            </div>
                
            </div>
            </body>
    """
    print '推荐语生成'
    with open(base_arch+'topic.html','w+') as f:
        f.write(html.format(topic_title=topic_title,topic_desc=topic_desc))

######################################################################
gen_foreword()
#gen_toc()
gen_topic()
gen_editor()
gen_copy_right()
gen_plant()
gen_editor()
gen_content()
