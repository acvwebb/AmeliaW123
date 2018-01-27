# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
#lines 4 and 5 are the first two libraries that need to be imported 
import scraperwiki
import lxml.html
#
# # Read in a page
urllist = ["https://beta.companieshouse.gov.uk/search/companies?q=apple"]
#need to store the list of URLS as a variable (list) then you need to loop through
for url in urllist: 
  html = scraperwiki.scrape(url)
  root = lxml.html.fromstring(html)
  names = root.cssselect("li h3 a")
  addresses = root.cssselect("li p:nth-child(3)")
  
  for i in names:
    print "Name?", i.text_content()
  for i in addresses:
    print "Live?", i.text_content()    
 
  
  
#create a range, range(1,10); assign it to a variable, makes a list; eg pring "inserts url"+str(i) - 
html = scraperwiki.scrape("https://beta.companieshouse.gov.uk/search?q=Amelia+Webb+Legend" )

record = {}
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
names = root.cssselect("li h3 a")
for name in names: 
  print name.text
  print name.attrib['href']
  record['link'] = name.attrib['href'] 
  print record
  scraperwiki.sqlite.save(unique_keys=['link'], data=record)

#Line 18 is adding extra information to our dictionary 
# # Write out to the sqlite database using scraperwiki library
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
