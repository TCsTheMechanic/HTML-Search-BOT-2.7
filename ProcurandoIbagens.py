import urllib2
import re

site = urllib2.urlopen("http://arcoplex.com.br/?lang=054")

conteudo = site.read()
conteudo = conteudo.replace("\n", "")

padrao = r'filme-single-list Cartaz(.*?)/>'
matcher = re.compile(padrao)
infos = matcher.findall(conteudo)
print "-- INFOS --"
print infos
print "-- INFOS --"

padrao = r'filme-img" src="(.*?)"'
matcher = re.compile(padrao)
ibagens = map(lambda x: matcher.findall(x)[0], infos)

for i in xrange(5):
    print ibagens[i]+"\n"
