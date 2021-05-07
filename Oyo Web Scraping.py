import requests as reqs
from bs4 import BeautifulSoup as BS
import csv

oyo_url = "https://www.oyorooms.com/hotels-in-mumbai/?page="
page_num = 11

def OYO_CSV(inpList):
         with open("OYO_Info.csv","a+",newline = "") as oyoInfo:
            oyoWrite = csv.writer(oyoInfo)
            if oyoInfo.tell() == 0:
                oyoWrite.writerow(Head)
            oyoWrite.writerow(inpList)


for it in range(1,page_num):
    oyo_url +=str(it)
    req = reqs.get(oyo_url, headers ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} )
    cont = req.content
    bs = BS(cont,"html.parser")

    Head = ["Hotel Number","Hotel Name" , "Hotel Address" , "Hotel Rating" , "Hotel Amenities" , "Hotel Pricing"]
    All_Hotels = bs.find_all("div",{"class" : "hotelCardListing"})
    hotel_amenities = []
    wholeList=[]



    for i,hotel in enumerate(All_Hotels):
        hotel_name = hotel.find("h3", {"class" : "listingHotelDescriptionhotelName"}).text
        hotel_address = hotel.find("span",{"class":"u-line--clamp-2"}).text
        hotel_rating = hotel.find("span",{"class":"hotelRatingrating"}).text
        ph_a = hotel.find_all("div",{"class":"amenityWrapper"})
        try :
            hotel_pricing = hotel.find("span",{"class":"listingPrice__finalPrice"}).text
        except :
            hotel_pricing = "---"

        for amenity in ph_a:
            a = amenity.find("span",{"class":"d-body-sm d-textEllipsis"}).text
            hotel_amenities.append(a.strip())

        wholeList =[i+1 , hotel_name , hotel_address , hotel_rating , ",".join(hotel_amenities), hotel_pricing[1::]]
        OYO_CSV(wholeList)
        oyo_url = oyo_url.replace(str(it),"")
