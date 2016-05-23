import urllib2
import os.path

def get_file(url, filename):
    attempts = 0
    savepath = "sov_maps/%s" % (filename)

    if os.path.isfile(savepath):
        print "%s already exists" % (savepath)
        return
    
    while attempts < 3:
        print "Attempt %d : %s" % (attempts, url)
        try:
            response = urllib2.urlopen(url, timeout = 2)
            content = response.read()
            f = open( savepath, 'w' )
            f.write( content )
            f.close()
            print "    Success"
            break
        except urllib2.URLError as e:
            attempts += 1
            print type(e)

for year in [2016]: #range(2016, 2016):
    for month in range(1,13):
        for day in range(1,32):
            filename = "%d%02d%02d.png" % (year, month, day)
            url = "http://go-dl1.eve-files.com/media/corp/verite/%s" % filename
            get_file(url, filename)

