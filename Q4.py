__author__ = 'Alif'
import os
import urllib
from urlparse import urlparse
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    tup = [];
    new_list = list(tup)
    urlLink = ""

    def __init__(self, urlLink):
        HTMLParser.__init__(self)
        self.urlLink = urlLink
        self.make_dir()

    def handle_starttag(self, tag, attrs):
        domain = self.getdomain()
        if(tag=='img'):
            for name,value in attrs:
                if(name=='src'):
                    linkparsed = urlparse(value)
                    if str(linkparsed[1]) == "":
                        self.new_list.insert(-1,str(domain)+"/"+value)
                    else:
                        self.new_list.insert(-1,value)


    def download_pic(self,domain):
        for link in self.new_list:
            filename = link.split('/')[-1]
            linkparsed = urlparse(link.replace('\\','/'))
            if str(linkparsed[1]) == "":
                downloadLink = str(domain)+link.replace('\\','/')
                print "Download",filename
                urllib.urlretrieve(downloadLink, self.dir_name()+"/"+filename)
            else:
                print "Download",filename
                urllib.urlretrieve(link, self.dir_name()+"/"+filename)



    def make_dir(self):
        dir_name = self.dir_name()
        try:
            os.makedirs(dir_name)
            print "Create",dir_name,"directory"
        except Exception, e:
            print "Dir",dir_name,"existed"


    def dir_name(self):
        linkparsed = urlparse(urlLink)
        domainName = str(linkparsed[1]).replace('.','_')
        dir_name = domainName+'_images'
        return dir_name

    def writeFile(self):
        filename = str(self.dir_name()+"/"+self.getdomain()).replace('.','_')
        fo = open(filename+".txt", "w")
        for link in self.new_list:
            text = "LINK: "+link+"\n"
            fo.write(text)

        fo.close()

    def getdomain(self):
        linkparsed = urlparse(urlLink)
        return linkparsed[1]


urlLink = "https://www.twitter.com"
parser = MyHTMLParser(urlLink)
try:
    textStream = urllib.urlopen(urlLink).read()
    parser.feed(textStream)
    parser.download_pic(urlLink)
    parser.writeFile()
except Exception,e:
    print 'ERROR:',str(e)




