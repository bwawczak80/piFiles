import requests as req

qry = {"q" : "sounding+the+seventh+trumpet"}
r = req.get("https://www.discogs.com/search/",params=qry)
hold_string = r.text

start_url = hold_string.find("https://img")
stop_url = hold_string.find(".jpeg.jpg" )
image_url = hold_string[start_url:stop_url + 9]
r = req.get(image_url)

if r.status_code == 200:
    print('Successful request!')
    download_file = open("new_image.jpg","wb" )
    for chunk in r.iter_content(chunk_size=256):
        if chunk:
            download_file.write(chunk)
        
    download_file.close()
    print("done")

else:
    print('An error has occurred.')





