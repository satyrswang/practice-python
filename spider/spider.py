from urllib import urlopen
from link_finder import  LinkFinder
from genneral import *
import scrapy 

class Spider:

	project_name = ''
	base_rul = 	''
	domain_name = ''
	queue_file = ''
	crawled_file = ''
	queue = set()
	crawled = set()
	
	def _init_(self,params):
		#super()._init_()	
		Spider.project_name =params.get("project_name")
		Spider.base_rul = params.get("base_rul")
		Spider.domain_name = params.get("domain_name")
		Spider.queue_file = project_name+'/queue.txt'
		Spider.crawled_file = project_name+'/crawled.txt'
		self.boot()
		self.crawl_page('first spider',Spider.base_rul)

	@staticmethod
	def boot():
		create_project_dir(Spider.project_name)
		create_data_files(Spider.project_name,Spider.base_rul)
		Spider.queue = file_to_set(Spider.queue_file)
		Spider.crawled = file_to_set(Spider.crawled_file)
	
	@staticmethod
	def crawl_page(threadname,page_rul):
		if page_rul not in Spider.crawled:
			print(threadname + 'now crawling'+page_rul)
			print('queue' + str(len(Spider.queue)))
			Spider.add_links_to_queue(Spider.gather_link(page_rul))
			Spider.queue.remove(page_rul)
			Spider.crawled.add(page_rul)
			Spider.update_file()

	@staticmethod
	def gather_link(page_rul):
		html_string = ''
		try: 
			response =urlopen(page_url)
			if response.getheader('content-type'=='text/html'):
				html_bytes = response.read()
				html_string = html_bytes.decode("utf-8")
			finder = LinkFinder(Spider.base_rul,Spider.page_url)
			finder.feed(html_bytes)
		except:
			print("error")
			return set()

		return finder.page_links

	@staticmethod
	def add_links_to_queue(links):
		for url in links:
			if url in Spider.queue:
				continue
			if url in Spider.crawled:
				continue
			if Spider.domain_name not in url:
				continue
			Spider.queue.add(url)

	@staticmethod
	def update_file():
		set_to_file(Spider.queue,Spider.queue_file)
		set_to_file(Spider.crawled,Spider.crawled_file)

















