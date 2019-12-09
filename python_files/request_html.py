import requests as req

# response = req.get("http://www.google.com")
# print(response.text)
# str.find(str, beg=0, end=len(string))
 
qry = {"q" : "sounding+the+seventh+trumpet"}
# qryResponse = req.get("https://www.google.com/search", params=qry)
# print(qryResponse.url)
# r = req.get("https://img.discogs.com/45LUqP2auQLS-DBhYDVhha6AeJc=/300x300/filters:strip_icc():format(jpeg):mode_rgb():quality(40)/discogs-images/R-1008180-1459499314-1961.jpeg.jpg" , stream = True)

r = req.get("https://www.discogs.com/search/",params=qry)
hold_string = r.text
# str.find(str, beg=0, end=len(string))
start_url = hold_string.find("https://img")
stop_url = hold_string.find(".jpeg.jpg" )
print(start_url)
print(stop_url)
image_url = hold_string[start_url:stop_url + 9]
r = req.get(image_url)
print(image_url)
# r = req.get ("https://www.discogs.com/Aerosmith-Pump/master/37145")
if r.status_code == 200:
    print('Successful request!')
    # print(r.text)
    
    # download_file = open("37145.jpg", "wb" )
    download_file = open("pump.jpg","wb" )
    for chunk in r.iter_content(chunk_size=256):
        if chunk:
            download_file.write(chunk)
        
    download_file.close()
    print("done")

else:
    print('An error has occurred.')





