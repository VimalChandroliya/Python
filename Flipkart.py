from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as uReq

my_url = "https://www.flipkart.com/search?q=iphone&otracker=start&as-show=on&as=off"

uClient = uReq(my_url)
page_html=uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

# print(page_soup.html)
# print(page_soup.get_text('='))

# print(page_soup.head)
containers = page_soup.findAll("div", {"class": 'col _2-gKeQ'})
print(len(containers))

container = containers[0]
print(soup.prettify(containers[0]))
print(container.div.img['alt'])

#
# price = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
# print(price[0].text)
#
# Rating = container.findAll("div" , {"class": "niH0FQ"})
# print(Rating[0].text)

# filename = "products.csv"
# f=open(filename,'w')

# headers = 'Product_Name, Pricing, Rating\n'
# f.write(headers)
#
# for container in containers:
#     product_name = container.div.img['alt']
#
#     price_container = container.findAll("div", {"class": "col col-5-12 _2o7WAb"})
#     price = price_container[0].text.strip() #strip function eliminates unnecessary comman,space
#
#     rating_container = container.findAll("div", {"class": "niH0FQ"})
#     rating = rating_container[0].text
#
#
#     print('Product_name : ',  product_name)
#     print('Price : ',  price)
#     print('Rating : ',  rating)
#
#     trim_price = ''.join(price.split(','))
#     rm_rupee = trim_price.split('₹')
#     add_rs_price = "Rs."+ rm_rupee[1]
#     split_price = add_rs_price.split('E')
#     final_price = split_price[0]
#
#     split_rating = rating.split(" ")
#     final_rating = split_rating[0]
#
#     # print('Final Price : ',final_price)
#     # print('Trim Price : ',trim_price)
#     # print('rm_ruppe : ',rm_rupee)
#     # print('add_rs_price : ',add_rs_price)
#     # print('Split price : ',split_price)
#
# #    print(product_name.replace(",","|") + "," + final_price + ","+ final_rating + '\n') #replace , with |
# #    f.write(product_name.replace(",","|") + "," + final_price + ","+ final_rating + '\n')
#
# f.close()

