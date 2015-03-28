"""
>>> zip_ops_test(url='http://iana.org')
org,iana)/ 20140126200624 http://www.iana.org/ text/html 200 OSSAPWJ23L56IYVRW3GFEAR4MCJMGPTB - - 2258 334 iana.warc.gz
org,iana)/ 20140127171238 http://iana.org unk 302 3I42H3S6NNFQ2MSVX7XZKYAYSCX5QBYJ - - 343 1858 dupes.warc.gz
org,iana)/ 20140127171238 http://www.iana.org/ warc/revisit - OSSAPWJ23L56IYVRW3GFEAR4MCJMGPTB - - 536 2678 dupes.warc.gz

# test idx index (tabs replacad with 4 spaces)
>>> zip_ops_test(url='http://iana.org/domains/', matchType='prefix', showPagedIndex=True)
org,iana)/dnssec 20140126201307    zipnum    8511    373    35
org,iana)/domains/int 20140126201239    zipnum    8884    353    36
org,iana)/domains/root/servers 20140126201227    zipnum    9237    386    37

>>> zip_ops_test(url='http://iana.org/domains/*')
org,iana)/domains/arpa 20140126201248 http://www.iana.org/domains/arpa text/html 200 QOFZZRN6JIKAL2JRL6ZC2VVG42SPKGHT - - 2939 759039 iana.warc.gz
org,iana)/domains/example 20140128051539 http://www.iana.org/domains/example text/html 302 JZ622UA23G5ZU6Y3XAKH4LINONUEICEG - - 577 2907 example.warc.gz
org,iana)/domains/idn-tables 20140126201127 http://www.iana.org/domains/idn-tables text/html 200 HNCUFTJMOQOGAEY6T56KVC3T7TVLKGEW - - 8118 715878 iana.warc.gz
org,iana)/domains/int 20140126201239 http://www.iana.org/domains/int text/html 200 X32BBNNORV4SPEHTQF5KI5NFHSKTZK6Q - - 2482 746788 iana.warc.gz
org,iana)/domains/reserved 20140126201054 http://www.iana.org/domains/reserved text/html 200 R5AAEQX5XY5X5DG66B23ODN5DUBWRA27 - - 3573 701457 iana.warc.gz
org,iana)/domains/root 20140126200912 http://www.iana.org/domains/root text/html 200 YWA2R6UVWCYNHBZJKBTPYPZ5CJWKGGUX - - 2691 657746 iana.warc.gz
org,iana)/domains/root/db 20140126200927 http://www.iana.org/domains/root/db/ text/html 302 3I42H3S6NNFQ2MSVX7XZKYAYSCX5QBYJ - - 446 671278 iana.warc.gz
org,iana)/domains/root/db 20140126200928 http://www.iana.org/domains/root/db text/html 200 DHXA725IW5VJJFRTWBQT6BEZKRE7H57S - - 18365 672225 iana.warc.gz
org,iana)/domains/root/servers 20140126201227 http://www.iana.org/domains/root/servers text/html 200 AFW34N3S4NK2RJ6QWMVPB5E2AIUETAHU - - 3137 733840 iana.warc.gz

# Pages -- default page size
>>> zip_ops_test(url='http://iana.org/domains/example', matchType='exact', showNumPages=True)
{"blocks": 1, "pages": 1, "pageSize": 10}

>>> zip_ops_test(url='http://iana.org/domains/', matchType='domain', showNumPages=True)
{"blocks": 38, "pages": 4, "pageSize": 10}

# set page size
>>> zip_ops_test(url='http://iana.org/domains/', matchType='domain', pageSize=4, showNumPages=True)
{"blocks": 38, "pages": 10, "pageSize": 4}

# set page size -- alt domain query
>>> zip_ops_test(url='*.iana.org', pageSize='4', showNumPages=True)
{"blocks": 38, "pages": 10, "pageSize": 4}

# page size for non-existent, but secondary index match
>>> zip_ops_test(url='iana.org/domains/int/blah', pageSize=4, showNumPages=True)
{"blocks": 0, "pages": 0, "pageSize": 4}

# page size for non-existent, no secondary index match
>>> zip_ops_test(url='*.foo.bar', showNumPages=True)
{"blocks": 0, "pages": 0, "pageSize": 10}

# first page
>>> zip_ops_test(url='http://iana.org/domains/', matchType='domain', showPagedIndex=True, pageSize=4, page=0)
com,example)/ 20140127171200    zipnum    0    276    1
org,iana)/ 20140127171238    zipnum    276    328    2
org,iana)/_css/2013.1/fonts/inconsolata.otf 20140126201055    zipnum    604    312    3
org,iana)/_css/2013.1/fonts/opensans-bold.ttf 20140126200718    zipnum    916    235    4

# first page -- simplified query
>>> zip_ops_test(url='*.iana.org/path_part_ignored/', showPagedIndex=True, pageSize=4)
com,example)/ 20140127171200    zipnum    0    276    1
org,iana)/ 20140127171238    zipnum    276    328    2
org,iana)/_css/2013.1/fonts/inconsolata.otf 20140126201055    zipnum    604    312    3
org,iana)/_css/2013.1/fonts/opensans-bold.ttf 20140126200718    zipnum    916    235    4

# next page + json
>>> zip_ops_test(url='http://iana.org/domains/', matchType='domain', output='json', showPagedIndex=True, pageSize=4, page=1)
{"urlkey": "org,iana)/_css/2013.1/fonts/opensans-bold.ttf 20140126200912", "part": "zipnum", "offset": 1151, "length": 235, "lineno": 5}
{"urlkey": "org,iana)/_css/2013.1/fonts/opensans-bold.ttf 20140126201240", "part": "zipnum", "offset": 1386, "length": 306, "lineno": 6}
{"urlkey": "org,iana)/_css/2013.1/fonts/opensans-regular.ttf 20140126200654", "part": "zipnum", "offset": 1692, "length": 235, "lineno": 7}
{"urlkey": "org,iana)/_css/2013.1/fonts/opensans-regular.ttf 20140126200816", "part": "zipnum", "offset": 1927, "length": 231, "lineno": 8}

# last page
>>> zip_ops_test(url='http://iana.org/domains/', matchType='domain', showPagedIndex=True, pageSize=4, page=9)
org,iana)/domains/root/servers 20140126201227    zipnum    9237    386    37
org,iana)/time-zones 20140126200737    zipnum    9623    145    38

# last page cdx
>>> zip_ops_test(url='http://iana.org/domains/', matchType='domain', pageSize=4, page=9)
org,iana)/domains/root/servers 20140126201227 http://www.iana.org/domains/root/servers text/html 200 AFW34N3S4NK2RJ6QWMVPB5E2AIUETAHU - - 3137 733840 iana.warc.gz
org,iana)/numbers 20140126200651 http://www.iana.org/numbers text/html 200 HWT5UZKURYLW5QNWVZCWFCANGEMU7XWK - - 3498 321385 iana.warc.gz
org,iana)/performance/ietf-draft-status 20140126200815 http://www.iana.org/performance/ietf-draft-status text/html 200 T5IQTX6DWV5KABGH454CYEDWKRI5Y23E - - 2940 597667 iana.warc.gz
org,iana)/performance/ietf-statistics 20140126200804 http://www.iana.org/performance/ietf-statistics text/html 200 XOFML5WNBQMTSULLIIPLSP6U5MX33HN6 - - 3712 582987 iana.warc.gz
org,iana)/protocols 20140126200715 http://www.iana.org/protocols text/html 200 IRUJZEUAXOUUG224ZMI4VWTUPJX6XJTT - - 63663 496277 iana.warc.gz
org,iana)/time-zones 20140126200737 http://www.iana.org/time-zones text/html 200 4Z27MYWOSXY2XDRAJRW7WRMT56LXDD4R - - 2449 569675 iana.warc.gz


# last page reverse -- not yet supported
#>>> zip_ops_test(url='http://iana.org/domains/', matchType='domain', reverse=True, showPagedIndex=True, pageSize=4, page=9)
#org,iana)/time-zones 20140126200737    zipnum    9623    145    38
#org,iana)/domains/root/servers 20140126201227    zipnum    9237    386    37


# last page reverse CDX
>>> zip_ops_test(url='http://iana.org/domains/', matchType='domain', reverse=True, pageSize=4, page=9)
org,iana)/time-zones 20140126200737 http://www.iana.org/time-zones text/html 200 4Z27MYWOSXY2XDRAJRW7WRMT56LXDD4R - - 2449 569675 iana.warc.gz
org,iana)/protocols 20140126200715 http://www.iana.org/protocols text/html 200 IRUJZEUAXOUUG224ZMI4VWTUPJX6XJTT - - 63663 496277 iana.warc.gz
org,iana)/performance/ietf-statistics 20140126200804 http://www.iana.org/performance/ietf-statistics text/html 200 XOFML5WNBQMTSULLIIPLSP6U5MX33HN6 - - 3712 582987 iana.warc.gz
org,iana)/performance/ietf-draft-status 20140126200815 http://www.iana.org/performance/ietf-draft-status text/html 200 T5IQTX6DWV5KABGH454CYEDWKRI5Y23E - - 2940 597667 iana.warc.gz
org,iana)/numbers 20140126200651 http://www.iana.org/numbers text/html 200 HWT5UZKURYLW5QNWVZCWFCANGEMU7XWK - - 3498 321385 iana.warc.gz
org,iana)/domains/root/servers 20140126201227 http://www.iana.org/domains/root/servers text/html 200 AFW34N3S4NK2RJ6QWMVPB5E2AIUETAHU - - 3137 733840 iana.warc.gz


# invalid page
>>> zip_ops_test(url='http://iana.org/domains/', matchType='domain', showPagedIndex=True, pageSize=4, page=10)
Traceback (most recent call last):
CDXException: Page 10 invalid: First Page is 0, Last Page is 9


>>> zip_ops_test(url='http://aaa.aaa/', matchType='exact', showPagedIndex=True)
Traceback (most recent call last):
NotFoundException: No Captures found for: http://aaa.aaa/

>>> zip_ops_test(url='http://aaa.aaa/', matchType='domain', showPagedIndex=True)
Traceback (most recent call last):
NotFoundException: No Captures found for: http://aaa.aaa/ (domain query)

>>> zip_ops_test(url='http://aaa.zz/', matchType='domain', showPagedIndex=True)
Traceback (most recent call last):
NotFoundException: No Captures found for: http://aaa.zz/ (domain query)

"""

from test_cdxops import cdx_ops_test
from pywb import get_test_dir
from pywb.cdx.cdxserver import CDXServer


import shutil
import tempfile
import os
import json


test_zipnum = get_test_dir() + 'zipcdx/zipnum-sample.idx'

def zip_ops_test(url, **kwargs):
    sources = test_zipnum
    cdx_ops_test(url, sources, **kwargs)


def test_zip_prefix_load():

    tmpdir = tempfile.mkdtemp()
    try:
        shutil.copy(test_zipnum, tmpdir)
        shutil.copy(get_test_dir() + 'zipcdx/zipnum-sample.cdx.gz',
                    os.path.join(tmpdir, 'zipnum'))

        config={}
        config['shard_index_loc'] = dict(match='(.*)',
                                         replace=r'\1')
        server = CDXServer(os.path.join(tmpdir, 'zipnum-sample.idx'),
                           config=config)


        # Test Page Count
        results = server.load_cdx(url='iana.org/',
                                  matchType='domain',
                                  showNumPages=True)

        results = list(results)
        assert len(results) == 1, results
        assert json.loads(results[0]) == {"blocks": 38, "pages": 4, "pageSize": 10}


        # Test simple query
        results = server.load_cdx(url='iana.org/')
        results = list(results)
        assert len(results) ==3, results
        assert '20140126200624' in results[0]
        assert '20140127171238' in results[1]
        assert 'warc/revisit' in results[2]

    finally:
        shutil.rmtree(tmpdir)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
