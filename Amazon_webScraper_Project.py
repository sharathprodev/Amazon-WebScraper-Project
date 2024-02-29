def price_check():
	URL = ''
	headers = {
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
	
	page = requests.get(URL, headers=headers)
	soup1 = BeautifulSoup(page.content, "html.parser")
	soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    
    title = soup2.find(id = 'productTitle').get_text()
    
    price = soup2.find(id = 'priceblock_ourprice').get_text()
    
    price = price.strip()[1:]
    title = title.strip()
    
    import datetime
    
    today = datetime.date.today()
    
    import csv
    
    header = ['Title', 'Price', 'Date']
    date = [title, price, today]
    
    with open('AmzWebScraperDataset.csv', 'a+', newline='', encoding='UTFS') as f:
        writer = csv.writer(f)
        wriiter.writerow(data)
        
