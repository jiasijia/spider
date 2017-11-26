#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import re

from bs4 import BeautifulSoup as bs

def request(url,page):
	headers = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
		'Cache-Control': 'no-cache',
		'Connection': 'keep-alive',
		# 'Cookie': 'SINAGLOBAL=861300807960.2014.1511586070389; YF-Page-G0=59104684d5296c124160a1b451efa4ac; _s_tentry=-; Apache=2145845182243.3088.1511682644760; ULV=1511682644776:2:2:1:2145845182243.3088.1511682644760:1511586070532; YF-V5-G0=f59276155f879836eb028d7dcd01d03c; login_sid_t=6aa4324b7a5d4def54eb81b93be0d53f; YF-Ugrow-G0=ad06784f6deda07eea88e095402e4243; WBtopGlobal_register_version=573631b425a602e8; wb_cusLike_3897001513=N; SCF=AnuMXxNMHvt0yMIzAx6sUd-Yke6jVO_YhH-cykVzu0g4DqcK-lPnJlX5UOWG7eIgVHplFkQau28LvXU3TTtQrw4.; SUHB=03o1rFUGevqvNB; un=13920648010; SUB=_2AkMtRhoGdcPxrABZkf8VzGrnbY5H-jyek3PwAn7uJhMyAxgv7l0fqSVutBF-XHqisd2TQoqsV8kn7DcYS_V7RHsB; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9Whc9wvAy.LE2bHrlZeb5eQ_5JpV2hMXSKncShece2WpMC4odcXt; cross_origin_proto=SSL; WBStorage=82ca67f06fa80da0|undefined; UOR=,,login.sina.com.cn; wb_cusLike_undefined=N',
		'Cookie':'SINAGLOBAL=861300807960.2014.1511586070389; YF-Page-G0=59104684d5296c124160a1b451efa4ac; _s_tentry=-; Apache=2145845182243.3088.1511682644760; ULV=1511682644776:2:2:1:2145845182243.3088.1511682644760:1511586070532; YF-V5-G0=f59276155f879836eb028d7dcd01d03c; login_sid_t=6aa4324b7a5d4def54eb81b93be0d53f; YF-Ugrow-G0=ad06784f6deda07eea88e095402e4243; cross_origin_proto=SSL; UOR=,,login.sina.com.cn; wb_cusLike_undefined=N; WBtopGlobal_register_version=573631b425a602e8; SCF=AnuMXxNMHvt0yMIzAx6sUd-Yke6jVO_YhH-cykVzu0g4j63-IVqmj4kYCgOwpJVjK9AYce8ofnQIMpp14idNLf0.; SUB=_2A253Ht8eDeRhGeVG4lUR8C_Jyj-IHXVUbbfWrDV8PUNbmtBeLRDukW9NHetkTy4ichMA9D4oYZXlmw2Iky5_aUbD; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whc9wvAy.LE2bHrlZeb5eQ_5JpX5K2hUgL.FoeR1KM7eh2feKe2dJLoI0MLxKBLBonL12BLxK-L1K5L1heLxKnL1hzL1h.LxKML1-2L1hBLxK-LBo5L1K2LxK-LBo.LBoxg; SUHB=0xny8Kcihq3Oaj; ALF=1512303053; SSOLoginState=1511698254; un=13920648010',
		'Host': 'weibo.com',
		'Pragma': 'no-cache',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
	}

	r = requests.get(url, headers = headers)
	r.encoding = 'utf-8'

	soup = bs(r.text, 'lxml')
	
	scripts = soup.find_all('script')
	pattern = re.compile(r'FM.view\((.*)\)')

	homeSoup = {}
	weiboList = None
	
	uid = re.compile(r"\[\'oid\'\]\=\'(.*)\'").search(r.text).group(1)

	for script in scripts:
		m = pattern.search(script.string)
		if m is None:
			continue

		# if  'PCD_header' in script.string:
		# 	homeSoup['header'] = bs(json.loads(m.group(1)).get('html'), 'lxml')
		# elif 'PCD_counter' in script.string:
		# 	homeSoup['card'] = bs(json.loads(m.group(1)).get('html'), 'lxml')
		# elif 'PCD_person_info' in script.string:
		# 	homeSoup['info'] = bs(json.loads(m.group(1)).get('html'), 'lxml')
		# elif 'WB_feed ' in script.string:
		# 	weiboList = bs(json.loads(m.group(1)).get('html'), 'lxml')
		# else:
		# 	pass
	
		if 'WB_feed ' in script.string:
			
			weiboList = bs(json.loads(m.group(1)).get('html'), 'lxml')

	# username = homeSoup['header'].find('h1', class_='username').string
	# attentionCount = homeSoup['card'].find_all('strong', class_='W_f12')[0].string
	# fansCount = homeSoup['card'].find_all('strong', class_='W_f12')[1].string
	# weiboCount = homeSoup['card'].find_all('strong', class_='W_f12')[2].string
	# birthday = homeSoup['info'].find('ul', class_='ul_detail').find_all('span', 'item_text')[4].string.strip()
	# level = homeSoup['info'].find('a', class_='W_icon_level').span.string

	if weiboList is None:
		 return
	print(type(weiboList))
	with open('log.txt', 'a') as f:
		# f.write('姓名:%s\n关注:%s\n粉丝:%s\n微博:%s\n生日:%s\n等级:%s\n\n' % (
		# 	username, 
		# 	attentionCount, 
		# 	fansCount, 
		# 	weiboCount, 
		# 	birthday,
		# 	level[3:]))

		for item in weiboList.find_all('div', attrs={'action-type': 'feed_list_item'}):
			date = item.find('div', class_='WB_from').a.string
			content = item.find('div', class_='WB_text').text
			media = item.find('div', class_='WB_media_wrap')
			# feed = item.find('div', class_='WB_handle').ul.find_all('li')
			# transfer = feed[1].find('em', class_='W_ficon').next_sibling.string
			# comment = feed[2].find('em', class_='W_ficon').next_sibling.string
			# like = feed[3].find('em', class_='W_ficon').next_sibling.string
			transfer = item.find('span', attrs={"node-type": 'forward_btn_text'}).text
			comment = item.find('span', attrs={"node-type": 'comment_btn_text'}).text
			like = item.find('span', attrs={"node-type": 'like_status'}).text

			f.write('日期:%s\n内容:%s\n是否有图片:%s\n转发:%s\n评论:%s\n点赞:%s\n\n' % (
				date,
				content.strip(),
				'无' if media is None else '有',
				transfer,
				comment,
				like
			))
	next_page = page + 1

	request(url + '&page=' + str(next_page), next_page)

url = 'https://weibo.com/u/1730726637?is_all=1'
request(url,1)
