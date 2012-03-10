#!/usr/bin/env python
import urllib,urllib2,string,random,cookielib,time

def random_string():
	size = random.randint(4,12) 
	chars = string.ascii_lowercase + string.digits
	return ''.join(random.choice(chars) for x in range(size))

if __name__ == '__main__':
	sleep = 0
	count = 1;
	while(1):
		email = random_string() + ''.join(random.sample(['@hotmail.com','@gmail.com','@facebook.com','@windowslive.com'], 1))
		password = random_string()
		post_data = urllib.urlencode({'0<text>' : email, '1<text>' : password})
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.FileCookieJar("cookies")))
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		opener.open('http://thaijakfreemce.yolasite.com', post_data)
		time.sleep(sleep)
		print email,password,count
		count = count + 1