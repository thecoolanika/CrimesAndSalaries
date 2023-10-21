'''
I compared the Average Monthly Net Salary (After Tax) and the crime index in the cities in the United States. 
In this file, I created a txt file and added to that. 
'''
import requests

f = open("crimesAndSalaries.txt", "w")

url = "https://www.numbeo.com/api/"

fields = {"api_key" : "0jalvgng5h70u2"}

r = requests.get(url + "/cities", params = fields)

cities = r.json()
cities = cities["cities"]

cityIDs = []
for city in cities:
  if city ["country"] == "United States":
    cityIDs.append(city["city"])

for ids in cityIDs:
  fields = {"api_key": "0jalvgng5h70u2", "query": ids}
  r2 = requests.get(url + "/city_prices", params = fields)
  prices = r2.json()
  if "prices" in prices:
    prices = prices["prices"]
    for price in prices:
      if "item_name" in price:
        if "average_price" in price:
          if "Average Monthly Net Salary" in price["item_name"]:
            fields = {"api_key": "0jalvgng5h70u2", "query": ids}
            r3 = requests.get(url + "/city_crime", params = fields)
            cityCrime = r3.json()
            if "index_crime" in cityCrime:
              f.write(str(cityCrime["index_crime"])+ "," + str(prices["average_price"]) + "/n")
