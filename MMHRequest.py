import unirest

response = unirest.post(
"http://makemehost.com/gamestart.php", 

headers={ 
"Host": "makemehost.com",
"Connection":"keep-alive",
"Content-Length":"81",
"Cache-Control":"max-age=0",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Origin":"http://makemehost.com",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
"Content-Type":"application/x-www-form-urlencoded",
"Referer":"http://makemehost.com",
"Accept-Encoding":"gzip,deflate",
"Accept-Language":"it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4,es;q=0.2"}, 

params={ 
"map": "Parasite%202%20[v1.14B].w3x", 
"pp": "Public", 
"gn":"PARASITE+2", 
"owner":"Freyon",
"location":"ALL"}

)
print 'If the response code is 200, then the packet was fine'
print 'Response code:',response.code # The HTTP status code
#print response.headers # The HTTP headers
#print response.body # The parsed response
#print response.raw_body # The unparsed response
raw_input('Press enter to continue')