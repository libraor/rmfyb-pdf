# README

每周四自动获取《人民法院报》第六版、第七版，并发送至指定邮箱。

main.py 主文件
catch.py 抓取pdf文件，抓取版面链接
mail.py 以邮件形式发送pdf文件
content.py 抓取文章标题并生成链接
test.py 将文章标题和链接发送至邮箱，待函数化后并入mail.py
