#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, threading
import time
import articles

ARTICLE1 = {
  'link' : 'http://www.ynet.co.il/articles/0,7340,L-4713571,00.html',
  'img' : 'https://images1.ynet.co.il/PicServer4/2014/08/05/5506384/52203970100690640360no.jpg',
  'title' : 'החוש הדומיננטי שיעזור לכם בלימודים',
  'content' : 'החוש הדומיננטי שיעזור לכם￼￼￼ בלימודים. אילו טיפים של שימוש בחושים יעזרו לכם?',
}
ARTICLE2 = {
  'link' : 'http://www.ynet.co.il/articles/0,7340,L-4713571,00.html',
  'img' : 'https://images1.ynet.co.il/PicServer5/2017/11/23/8172884/817287001000100980704no.jpg',
  'title' : '"כ"ט בנובמבר: "שמחה שנמשכה ימים ולילות,￼ הייתה אופוריה"',
  'content' : 'ב-1947 הם היו ילדים או צעירים￼￼￼￼￼￼ בתחילת דרכם, אבל את היום הגורלי ב-29 בנובמבר הם לא\
              שוכחים עד היום. "כולם היו צמודים לרדיו. אני זוכרת את התפרצות השמחה, ריקודים\
              והתחבקויות".',
}
ARTICLE3 = {
  'link' : 'https://www.calcalist.co.il/world/articles/0,7340,L-3726321,00.html',
  'img' : 'https://images1.calcalist.co.il/PicServer3/2017/11/30/775736/2_l.jpg',
  'title' : 'רוצים נייר טואלט? הזדהו: כך משפרים הסינים￼ את מצב השירותים הציבוריים',
  'content' : 'שבוע קרא נשיא סין שי ג‘ינפינג￼￼￼￼￼￼ להמשיך את מהפכת השירותים הציבוריים עליה הכריז ב-2015.ֿֿ\
                עד כה שופצו ונבנו 68 אלף מתקנים',
}
ARTICLE4 = {
  'link' : 'http://www.nrg.co.il/online/13/ART2/902/962.html',
  'img' : 'http://www.nrg.co.il/images/archive/465x349/1/646/416.jpg',
  'title' : 'מחקו לכם הודעה בווטסאפ? עדיין תוכלו לקרוא אותה',
  'content' : 'פליקציה בשם Noti cation History מאפשרת למשתמשי  אנדרואיד לקרוא את הנתונים הזמניים הנשמרים ביומן הפעילות של הסמארטפון, כולל הודעות מחוקות.'
}
ARTICLE5 = {
  'link' : 'http://www.nrg.co.il/online/55/ART2/904/542.html',
  'img' : 'http://www.nrg.co.il/images/archive/465x349/1/795/429.jpg',
  'title' : 'גם בחורף: זה בדיוק הזמן לקפוץ לאילת',
  'content' : 'העיר הדרומית נעימה לנופש גם￼￼￼￼￼ בחודשי החורף. כעת מוצעים מחירים אטרקטיביים במיוחד בחבילות שכוללות מגוון אטרקציות, לינה וטיסות'
}
ARTICLE6 = {
  'link' : 'https://food.walla.co.il/item/3113079',
  'img' : 'https://img.wcdn.co.il/f_auto,w_700/2/5/1/3/2513314-46.jpg',
  'title' : '12 בתי קפה שמתאימים לעבודה עם לפטופ',
  'content' : 'בין אם אתם סטודנטים או￼￼￼ עצמאיים, זה תמיד סיפור למצוא בית קפה נעים וטעים לרבוץ בו. קיבצנו עבורכם 12 מקומות אהובים בדיוק למטרה זו, בארבע הערים הגדולות'
}
ARTICLE7 = {
  'link' : 'https://news.walla.co.il/item/3114145',
  'img' : 'https://img.wcdn.co.il/f_auto,w_700/2/4/9/5/2495334-46.jpg',
  'title' : 'שותק על אזריה, נלחם באהוד ברק: בנט מנסה להיבנות כימין ממלכתי',
  'content' : 'כשרגב נלחמת ברעש בתאטרון￼￼￼ יפו, בנט משנה בשקט את נהלי סל התרבות כך שהחומרים "השמאלנים" ייפלטו. כשהקשת הפוליטית מתרעמת על דיווחי ה"דיל" של טראמפ עם הפלסטינים, בנט שותק עד שהרשות תסרב.'
}
ARTICLE8 = {
  'link' : 'https://news.walla.co.il/item/3114283',
  'img' : 'https://img.wcdn.co.il/f_auto,w_700/2/5/1/4/2514588-46.jpg',
  'title' : 'רצח בכל שלושה ימים: צרפת יוצאת למאבק￼￼ באלימות נגד נשים',
  'content' : 'אחרי ש-126 נשים נרצחו בידי בני￼￼￼ זוגן בשנה שעברה, הציג מקרון צעדים חדשים למלחמה בתופעה. "זאת בושה לצרפת", אמר הנשיא שאחת מהבטחות הבחירות שלו הייתה להשיג שוויון מגדרי.'
}
ARTICLES = [ARTICLE1, ARTICLE2, ARTICLE3, ARTICLE4, ARTICLE5, ARTICLE6, ARTICLE7, ARTICLE8]

def add_article_to_html(package_general_article,i):
    article = ARTICLES[int(i)]
    title_index = package_general_article.index('<a href="link">Title</a>')
    new_package_article = package_general_article[:title_index]+\
                          '<a href='+article['link']+'>'+article['title']+'</a>'+\
                          package_general_article[title_index+24:]
    image_index = new_package_article.index('<img src="" />')
    new_package_article = new_package_article[:image_index] + \
                          '<img src="' + article['img'] + '" />' + \
                          new_package_article[image_index + 14:]
    content_index = new_package_article.index('<h3>Content</h3>')
    new_package_article = new_package_article[:content_index] + \
                          '<h3>' + article['content'] + '</h3>' + \
                          new_package_article[content_index + 16:]
    return new_package_article

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '0.0.0.0'
server_port = 80
server.bind((server_ip, server_port))
server.listen(5)
GenericOkHeader = """HTTP/1.1 200 OK
Last-Modified:"""+time.asctime( time.localtime(time.time()) )+"""\n\nConnection: Close
Content-Length:
"""
okHeader = """HTTP/1.1 200 OK
Content-Type: text/html
Connection: Close
Content-Length:
"""
okHeaderImage = """HTTP/1.1 200 OK
Content-Type: image/*
Connection: Close
Content-Length: """
notFound = """HTTP/1.1 404 Not Found
Date: Sun, 18 Oct 2012 10:36:20 GMT
Server: Apache/2.2.14 (Win32)
Content-Length: 230
Connection: Closed
Content-Type: text/html
\n\n
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html>
<head>
   <title>404 Not Found</title>
</head>
<body>
   <h1>Not Found</h1>
   <p>The requested URL /t.html was not found on this server.</p>
</body>
</html>"""
notFoundHeader = """HTTP/1.1 404 Not Found
Content-Length: 0
Connection: Close
Content-Type: image/jpg"""
not_modified_header = """HTTP/1.1 304 Not Modified
Content-Length: 0
Connection: Close"""
while True:
    client_socket, client_address = server.accept()
    print 'Connection from: ', client_address
    data = client_socket.recv(1024)
    ifat=1
    while ifat:
        print 'Received: ', data
        if "If-Modified-Since:" in data:
            package = not_modified_header
        else:
            if(data.split('/')[1].startswith("homepage")):
                num_of_articles = data[data.index("?id=")+4]
                num_of_articles = int(num_of_articles)
                print "22222222222222222222222"
                location = "Files/template.html"
                f = open(location, 'r')
                package = f.read()
                f.close()
                start_of_article = package.index('<div class="row">')
                end_of_article = package.index('</div><!--/.row-->')+18
                print "end:"+package[end_of_article-18:end_of_article]
                package_start = package[:start_of_article-1]
                package_general_article =package[start_of_article:end_of_article]
                package_end = package[end_of_article+1:]
                package = package_start
                if(num_of_articles!=0):
                    for i in range(1,num_of_articles+1):
                        package_article = add_article_to_html(package_general_article,i-1)
                        package = package+package_article
                package = package+package_end
                package = okHeader + (str(len(package))) + "\n\n" + package
            else:
                location = data.split()[1][1:]
                try:
                    print "location: "+location
                    if not(location.startswith("Files/")):
                        location = "Files/"+location
                    if location.endswith("html"):
                        print "html"
                        f = open(location, 'r')
                        package = f.read()
                        package = okHeader+(str(len(package)))+"\n\n"+package
                    elif location.endswith("jpg") or location.endswith("png"):
                        print "jpg or png"
                        f = open(location, 'rb')
                        package = f.read()
                        package = okHeaderImage +(str(len(package)))+"\n\n"+ package
                    else:
                        print "else"
                        f = open(location, 'r')
                        package = f.read()
                        package = GenericOkHeader + (str(len(package))) + "\n\n" + package
                    #print package
                    f.close()
                except IOError:
                    print "111111111111111111111111111111\n"
                    package = notFoundHeader
        client_socket.send(package)
        print package
        #data = client_socket.recv(1024)
        print 'Client disconnected'
        client_socket.close()
        ifat=0
