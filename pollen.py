import webscraper as ws

def getPollenCount():
    mylist = ws.chunkParser(ws.scrape('https://www.atlantaallergy.com/pollen_counts'),
                                      'class="pollen-num"').split(' ')
    for i in mylist:
        try:
            j = float(i)
            return j
        except:
            continue
    return float(9999)