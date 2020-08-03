from hashlib import sha1
def cachecheck(fun):
	def mod(*args,**kwargs):
		cname = sha1((str(args)+str(kwargs)).encode()).hexdigest()+".cache"
		try:
			text = open(cname,encoding='utf-8').read()
		except Exception:
			text = fun(*args,**kwargs)
			open(cname,"w",encoding='utf-8').write(text)
		return text
	return mod