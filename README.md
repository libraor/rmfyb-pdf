# README

每周四自动获取《人民法院报》第六版、第七版，并发送至指定邮箱。

main.py 主文件,目前设置为发送标题和链接，发送pdf版暂时屏蔽
catch.py 抓取pdf文件，抓取版面链接
mail.py 以邮件形式发送pdf文件
content.py 抓取文章标题并生成链接
test.py v3.0临时文件，功能在函数化后并入mail.py-->mail_title_link
