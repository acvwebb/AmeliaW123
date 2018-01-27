import scraperwiki
import requests
import lxml.html
import re

#Copy and paste a column from excel within the ''' markers to create a variable
pastedfromexcel = '''-12q-GnQht/
-12tFMTYdK/
-13Fn9GKVp/
-13RgOA64B/
-19MBDA7Dg/
-19RsMt00h/
-19TPnti7H/
-19X5USe6p/
-19hj4lBzo/
-19ugoNHpx/
-19xGXtIEv/
-191HsqOet/
-19_l6ihPC/
-1-L7NPrtl/
-1-XpykkiC/
-2EroUtnfT/
-2EtBdG3ya/
-2EvHToOVn/
-2E6vxgvEa/
-2E9aWGGQP/
-2E9bwB210/
-2FM_uuLps/
-2FWzABqLp/
-2FazNuVro/
-2Fhx9Ki3I/
-2Fjf-Dxo8/
-2L0uNIq2t/
-2L2yKro6K/
-2L3Q-MioH/
-2L6ieFmEY/
-2L68QTFPA/
-2MCQDAYty/
-2MGppzFPS/
-2MJBQI3E6/
-2MMN7tRlY/
-2MRhesYRH/
-2MR71zFPo/
-2RlIUACfu/
-2Rqm8m-hw/
-2Rs7EBV5L/
-2RvPGDsvYHfC5ivcykUTmf4fbT-t3mQzcglE0/
-2Ry0TnnH3/
-2R5CfAPig/
-2R9QENkCq/
-2SiG2MaLF/
-2SmsvpgXe/
-2SuXUCUrV/
-2TDumgpgo/
-2XjRmmPoN/
-2Xq_Gk8O9/
-2YHsnEwCa/
-2YgWKR959/
-2YtHGOwbY/
-2Yu0SEwDZ/
-2YxC2Nzyn/
-2Y2HGGPqP/
-2Y2f1CAP5/
-2ZJsywczL/
-2ZgifO71w/
-2fgFMmPkX/
-2ftH9mPky/
-2f7fpLksH/
-2gE55QDmc/
-2gRHdKlB_/
-2gdmODSdY/
-2gfCcH2Rb/
-2gjRuH2Ri/
-2gk92n2Rn/
-2gmQsH2Rp/
-2go70uILv/
-2g_oTH2SH/
-2hCdMn2SK/
-2hDySn2SV/
-2hFz-n2SZ/
-2hJ7Xn2Sg/
-2h5OPk1gw/
-2iPz3QIHG/
-2kdhOJDAT/
-2kfjFMEqX/
-2kh-2EuQF/
-2mCaLkuSa/
-2rEtXKROv/
-2rwPEM6vM/
-2sAvMM6vi/
-2sroiiGB4/
-2t8GwNndF/
-2t_mCpEtP/
-2vIB5BxEC/
-2vO5evgJK/
-2xJCjgK-_/
-2yAeMgKwO/
-2yZL_Adpy/
-2yahtgKwt/
-21ZxFu4R4/
-21tExI7UZ/
-22Lu0EhSF/
-23A-Dkkrw/
-24wEZmfvI/
-25MBIkkuN/
-277zHF6KC/
-2_g_0qS7v/
-3AB2vuO4N/
-3AmzOxbkv/
-3Arb7vytK/
-3B4YKNhx6/
-3CFA9thyQ/
-3CJb7thyV/
-3CNqCNhyg/
-3CQvkthyk/
-3CXETrI_k/
-3C0aUsnHQ/
-3FcSTqlF_/
-3GK2ZHVoe/
-3GWiWnMgQ/
-3G-GlQ7iz/
-3HiFXLYv4/
-3Hy68nOFl/
-3IeOIGouw/
-3IqlFhCR0/
-3JJsZsmlp/
-3KEcwmuDG/
-3KSNLGuDT/
-3P23fgeZV/
-3P9VGgeZb/
-3QDXfAeZl/
-3QHGzE44e/
-3Qp1oCn_d/
-3QtmuA2JL/
-3Qx9RS5eD/
-3QzbmJfHa/
-3Q5M2Fn15/
-3Q6lvjMr3/
-3RMqgA56M/
-3Wia7hXbH/
-3WpF3ls-y/
-3W7Pmw7kz/
-3XBZEEQk2/
-3XNiGkqer/
-3XP1xhb4U/
-3XSYMFaUD/
-3XcLRlRoi/
-3XefIPgkO/
-3XoO3vhw4/
-3XyZ3mc0B/
-3dO1mIb_j/
-3dZzShdk1/
-3dbH_mWaG/
-3dtBaLp-R/
-3dzKHPgq8/
-3d9x9BngX/
-3eIgZkQa8/
-3eWzlHcUd/
-3eY6NPh6B/
-3elTuHdV3/
-3e5xPR09e/
-3kmDRuc7a/
-3kuu8pzqa/
-3kwOajAC6/
-3kzphm7EM/
-3k1bNt0eu/
-3lC8vx6iy/
-3lDGyDADm/
-3lYDIDs3u/
-3lnnWkxK-/
-3lpbWlS4w/
-3lwntm1DV/
-3rvMaPg59/
-3rz1ajCNu/
-3r5YouyEz/
-3r6OrihG1/
-3r80rJx1i/
-3sAjrrd1O/
-3zAoGP9xj/
-3zEbPTiIb/
-3zLNGFgbr/
-3zPIdCUjU/
-3zPdJGbCK/
-3zPlkgGNN/
-3zXMvDCMZ/
-3zZ6dKXDC/
-3zebck-Il/
-3zjnNH83A/
-3zqCDhkhN/
-35h5LKZkv/
-35k9NQ0Hx/
-36BPCtqyy/
-36EZAFzC7/
-36EulBgVf/
-36GChotpV/
-36MG0lzDI/
-36PGowV9S/
-36PlxxGi1/
-36P5RItpx/
-36fpCvucN/
-3_90ClSBE/
-4AJLxNuzP/
-4AJjdNLbH/
-4ALu1nB1R/
-4AdpMOrtY/'''

#This then splits that variable on each carriage return, to create a list of usernames
picurllist = pastedfromexcel.split('\n')
baseurl = 'https://www.instagram.com/p/'
url = 'https://www.instagram.com/bhameastside/'

#Here we define a function which uses the username as an argument
def grabfollows(picurl):
    #create the full URL by joining the username to the baseurl
    userurl = baseurl+picurl
    print "SCRAPING", userurl
    #scrape it into 'html'
    #THIS GENERATES AN ERROR IF THE URL HAS DISAPPEARED
    html = scraperwiki.scrape(userurl)
    #convert it to an lxml object
    root = lxml.html.fromstring(html)
    print root
    #grab anything in <script> tags
    headers = root.cssselect('script')
    #the 7th one (index 6) has what we need
    print headers[6].text
    profiledata = headers[6].text
    #split the contents of that tag in two, grab the second part, then split that part again and grab the first part
    locationdata = profiledata.split('"location":')[1].split('}')[0]
    #followers = profiledata.split('"followed_by":{"count":')[1].split('}')[0]
    print "LOCATIONDATA:", locationdata
    print len(locationdata.split('has_public_page":'))
    if len(locationdata.split('has_public_page":'))>1:
        has_public_page = locationdata.split('has_public_page":')[1].split(',')[0]
        name = locationdata.split('name":"')[1].split('"')[0]
        idref = locationdata.split('id":"')[1].split('"')[0]
        print has_public_page
    else:
        has_public_page = "NONE"
        name = "NONE"
        idref = "NONE"
    likes = profiledata.split('likes":{"count":')[1].split(',')[0]
    is_ad = profiledata.split('is_ad":')[1].split(',')[0]
    username = profiledata.split('"owner":{"username":"')[1].split('"')[0]
    full_name = profiledata.split('full_name":')[1].split(',')[0]
    caption = profiledata.split('caption":')[1].split(',')[0]
    print "LIKES:", int(likes)
    #create the fields in our dictionary, and assign variables to those
    record['has_public_page'] = has_public_page
    record['name'] = name 
    record['place_id'] = idref 
    record['place_url'] = 'https://www.instagram.com/explore/locations/'+idref
    record['url'] = 'https://www.instagram.com/p/'+picurl
    record['picid'] = picurl
    record['likes'] = int(likes)
    record['is_ad'] = is_ad
    record['username'] = username
    record['full_name'] = full_name
    record['caption'] = caption
    print record
    #save the whole thing, with username as the unique key
    scraperwiki.sql.save(['url'], record)

#create an empty record (this will be filled when the function runs above)
record = {}
#loop through our username list
for picurl in picurllist:
    #run the function defined above on each username
    grabfollows(picurl)

#picurl = '-0ICf6gPdN/'
#grabfollows(picurl)
#html = requests.get(picurl)
#print html.content

# Saving data:


