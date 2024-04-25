from  webscrapping import getNewsData
import csv

news_data = getNewsData()

with open("news_data.csv", "w", newline="") as csv_file:
    fieldnames = ["link", "title", "snippet", "date", "source"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(news_data)
  
print("Data saved to news_data.csv")