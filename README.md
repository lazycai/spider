spider
======

InfoQ 的《架构师》生成脚本


=========

# 说明
1. 把res文件夹复制到某一个路径下
2. 修改config.py文件
3. 运行python fetch.py 和python gen.py


每一期制作架构师的时候首先把res文件夹拷贝到某个路径，这个路径就是base_folder，需要定义在config.py中定义了一些常量，如下是名词解释：

1. base_folder 基本的文件夹
2. base_arch 架构师生成的页面html文件夹
3. which_month 几月刊
4. chief_editor 主编
5. chief_editor_desc 主编介绍
6. chief_editor_image 主编头像，头像应该存储在res文件夹中
7. plant_name 封面植物的名称
8. plant_desc 封面植物的介绍
9. plant_img 封面植物
10. recommand_editor_name 推荐编辑
11. recommand_editor_img 推荐编辑图片
12. recommand_editor_desc 推荐编辑介绍
13. foreword_title 前言
14. forword_content 序言内容
15. topic_title 专题名称
16. topic_desc 专题推荐语
17. org_urls 内容列表，因为是自动生成，所有的内容都需要在CMS中获取，所以直接填写内容的URL，对于不需要显示在首页的内容建议发布的时候隐藏
18. gen_list 合成列表，这个列表的内容是合成的顺序，注意填写文件的名称，不用加后缀，因为arch是内容的单篇文件夹，ads是广告文件夹，所以需要写明是哪个文件夹的内容，在Mac下是/，在windows下是\\

**注意：**需要在windows下运行，否则生成的不是微软雅黑，不好看，在windows下把windows/print.css放到style的文件夹中。

然后运行`python fetch.py`，注意第一次是所有都运行，然后如果需要微调则可以编辑fetch.py最后的内容，把不需要的注释掉：

1. gen_foreword()  生成卷首语
2. gen_toc()  生成目录
3. gen_topic() 生成专题推荐语
4. gen_editor() 生成推荐编辑
5. gen_copy_right() 生成版权信息
6. gen_plant() 生成封面植物
7. gen_content() 生成所有的文章内容
