# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

base_folder="/Users/Arthur/Dropbox/project/spider/res/"
base_arch=base_folder+'arch/'

which_month='8'
chief_editor="水羽哲"
chief_editor_desc="水羽哲，InfoQ中文站内容运营编辑，喜欢宅着看火影、海贼，没事爱写代码！"
chief_editor_image="shuiyuzhe.jpg"

plant_name='蔷薇'
plant_desc='蔷薇（学名：Rosa multiflora），又称野蔷薇，蔷薇科植物，主要分布在北半球温带、亚热带及热带山区等地区。蔷薇花是一种蔓藤爬篱笆的小花，花盘环绕萼筒口部，有白色、黄色等多种颜色，叶互生，奇数羽状复叶，其耐寒，有野生的，可用压条或嫁接法繁殖等种植方法。蔷薇可以药用，由其制成的蔷薇花粥有良好的营养价值。其不同颜色有不同花语，如红蔷薇代表热恋； 粉蔷薇代表爱的誓言。全属约有200种，广泛分布亚、欧、北非、北美各洲寒温带至亚热带地区。我国产82种。生长习性蔷薇喜阳光，亦耐半阴，较耐寒，在中国北方大部分地区都能露地越冬。对土壤要求不严，耐干旱，耐瘠薄，但栽植在土层深厚、疏松、肥沃湿润而又排水通畅的土壤中则生长更好，也可在粘重土壤上正常生长。不耐水湿，忌积水。新株定植时要施入腐熟有机肥。霜植后头一二年可于每年深秋开沟施一次基肥，以利生长和开花。萌蘖性强，耐修剪，抗污染。花期一般为每年的4-9月，次序开放，可达半年之久，由于温室效应而导致全球变暖，某些地方的蔷薇提早在4月，甚至是3月份便开始开花。中国人在文学作品和日常生活中、口语中的蔷薇，一般指黄蔷薇和野蔷薇。严格的说来，蔷薇属除少数玫瑰及月季外都称作蔷薇，而每一种蔷薇前面都有形容词，如矮蔷薇、藏边蔷薇、多腺小叶蔷薇等。此属品种全世界约有200种，品种繁多，变异极大，有许多变种及园艺栽培种，多产北半球温带、亚热带及热带山区。'
plant_img='qiangwei.png'


recommand_editor_name='臧秀涛'
recommand_editor_img='zangxiutao.png'
recommand_editor_desc='''各位读者朋友，大家好。很荣幸受邀成为本期《架构师》的推荐编辑。和InfoQ网站结缘已久，因为对Java和架构的爱好，每每被该网站的高质量内容所吸引，第一手的热点新闻和业界报道也让我受益匪浅。
机缘巧合，在新浪微博上看到InfoQ中文站主编贾国清（@frankjiagq）发布的译者招募信息，我便跃跃欲试了。因为之前翻译过一些技术文章，也跟别人合作翻译了一本技术书籍，所以希望能在InfoQ中文站上为技术传播贡献一份自己的力量。
InfoQ中文站对翻译的质量要求比较严格，新人加入要经过试译，试译通过之后才专为译者。而译者提交的译稿也要经过老编辑审校通过之后才能发布。前辈们的审校让我在准确表达、遣词造句和流畅表达方面获益良多。
加入之后，才发现翻译新闻和文章远远不是英文转换成中文这么简单。作为技术翻译，原文上的各种资料链接、技术背景都要了解一下，这是准确传达的前提。此后还要考虑遣词造句和中文习惯等问题。在自己可控的范围内，尽量做到最好，所以一篇稿件前前后后可能要处理四五次。发布之后也是诚惶诚恐，一方面自己会再读一遍，发现问题马上反馈；另一方面期待读者的评论，尽量和读者互动。有时候发布之后要修改感觉不太舒服的地方，可给水羽哲等编辑添了不少麻烦。
谈到与读者的互动，这里补充几句。非常希望能跟读者进行高质量的互动，但是有时候看到“像机器翻译的一样”之类的留言，心里很不是滋味。当然，问题肯定在译者身上，存在理解不到位和表达不到位等问题，这时候就要再回过头来核对，甚至找其他编辑帮忙看看，借以改进质量。但是，如果读者能详细指出一些具体问题，那真是求之不得，万分感谢的。希望能和读者共同进步。
</p><p>InfoQ编辑团队非常务实，大家经常为一些翻译或技术细节探讨半天，群策群力，争取准确地传达信息，“促进软件开发领域知识和创新的传播”。跟大家的合作非常开心。我的新浪微博是@臧秀涛，希望有机会跟读者进行更多交流。如果您有意加入我们，做技术的传播者，请邮件联系editors@cn.infoq.com。
'''

foreword_title='取舍'
forword_content=''''''



topic_title='再谈REST'
topic_desc='''

<p>PC时代的软件以功能取胜，移动时代的软件以体验取胜。这是目前在做移动应用的很多开发者都感受到的一个现实。</p>

<p>6月百度技术沙龙的话题是前端开发，同时也是InfoQ编辑的聚会。我们在聚会上邀请了前人人网前端负责人闫强一起过来玩，聊到前端职业发展这个话题的时候，他感慨道：前端这个领域很少有科班出身的。他自己的经历很“狂野”：攒过机器，修过笔记本，开过黑车，做过面馆，后来到做设计、Flash开发，到写HTML、JS，完全是一路闯过来的。</p>

<p>在人人网，前端最早是属于产品部门的。在他看来，这是件羞于启齿的事情。后来，前端独立了出来。现在，前端能够给后端提意见，因为他们既懂设计，又懂产品，也懂技术。另一方面，百度的前端则提出了F.I.S.项目，项目负责人张云龙称其为“前端领域工业化”，提倡前端的自动化。不管从哪个角度来看，前端正在变成一个产业，这个产业涉及到设计、产品、技术，并越来越往工程化的方向前进。</p>

<p>归根结底，跟电脑相关的设计都可以追溯到一个学科：人机交互。没有人可以知道在五年之后，指尖上的世界会变成什么样。但可以肯定的是，好的体验不再可有可无，因为用户对它具有非常高的期望！</p>'''


org_urls={
    "人物 | People":
    [
        "http://www.infoq.com/cn/news/2013/07/oschina-on-tech-choice"
    ],
    
    "观点 | View":
    [
        "http://www.infoq.com/cn/news/2013/07/things-change-processes",
        "http://www.infoq.com/cn/news/2013/07/functional-programming"
    ],

    "本期专题：再谈REST | Topic":
    [
        "http://www.infoq.com/cn/articles/how-to-design-a-good-restful-api",
        "http://www.infoq.com/cn/news/2013/05/idempotent",
        "http://www.infoq.com/cn/news/2013/06/web-style"
    ],

    "推荐文章 | Article":
    [
        "http://www.infoq.com/cn/articles/Chris-Patterson",
        "http://www.infoq.com/cn/articles/block-storage-overview",
        "http://www.infoq.com/cn/articles/interoperability-is-the-key"
    ], 

    "特别专栏 | Column":
    [
        "http://www.infoq.com/cn/news/2013/07/bachi-on-kissy",
        "http://www.infoq.com/cn/news/2013/07/m-dmp-xucheng-interview",
        "http://www.infoq.com/cn/news/2013/07/believe-data-power"
    ],

    "避开那些坑 | Void":
    [
        "http://www.infoq.com/cn/news/2013/07/xupeng-mysql-mistake",
        "http://www.infoq.com/cn/news/2013/07/async-await-pitfalls",
    ],

    "新品推荐 | Product":
    [
        "http://www.infoq.com/cn/news/2013/07/el3",
        "http://www.infoq.com/cn/news/2013/07/vs2012_4RC1",
        "http://www.infoq.com/cn/news/2013/07/NET-Reflector-8-2",
        "http://www.infoq.com/cn/news/2013/07/essential-studio-for-javascript",
        "http://www.infoq.com/cn/news/2013/07/dart-polymer-web-ui",
        "http://www.infoq.com/cn/news/2013/07/gae-memcache-module",
        "http://www.infoq.com/cn/news/2013/07/rails4"
    ]

}

gen_list=['arch/cover','arch/foreword','ads/InfoQ','arch/toc',
'ads/QClub','arch/0','arch/1','arch/2',
'arch/topic',
'arch/3',
'arch/4',
'arch/5',
'arch/6',
'arch/7',
'arch/8',
'arch/9',
'arch/10',
'arch/11',
'arch/12',
'arch/13',
'arch/14',
'ads/book',
'ads/history',
'arch/editor',
'arch/plant',
'ads/1kg',
'arch/right']

