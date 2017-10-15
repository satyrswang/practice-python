import HTMLParser
import parse


class LinkFinder(HTMLParser):

	def __init__(self,dic):
		self.links = set()
		self.update(dic)
	
	def update(self,dic):
		self.base_url = dic.get("base_url")
		self.page_url = dic.get("page_url")

	def error(self,message):
		pass
	def handle_starttag(self,tag,attrs):
		if tag == 'a':
			for (attribute,value) in attrs:
				if attribute == 'href':
					url = parse.urljoin(self.base_rul,value)
					self.links.add(url)

	def page_links(self):
		return self.links


#finder = LinkFinder()
