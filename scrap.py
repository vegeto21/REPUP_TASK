import requests
import os
from bs4 import BeautifulSoup
import pandas as pd


headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}


# list of all the hotels whose reviews we're collecting
urls = ['https://www.tripadvisor.in/Hotel_Review-g304551-d3507485-Reviews-Red_Fox_Hotel_Delhi_Airport-New_Delhi_National_Capital_Territory_of_Delhi.html',
'https://www.tripadvisor.in/Hotel_Review-g304555-d776155-Reviews-Hotel_Kalyan-Jaipur_Jaipur_District_Rajasthan.html',
'https://www.tripadvisor.in/Hotel_Review-g304551-d299120-Reviews-The_Lalit_New_Delhi-New_Delhi_National_Capital_Territory_of_Delhi.html',
'https://www.tripadvisor.in/Hotel_Review-g304551-d11561000-Reviews-Roseate_House_New_Delhi-New_Delhi_National_Capital_Territory_of_Delhi.html',
'https://www.tripadvisor.in/Hotel_Review-g8342248-d10390860-Reviews-Parakkat_Nature_Hotels_Resorts-Pallivasal_Munnar_Idukki_District_Kerala.html',
'https://www.tripadvisor.in/Hotel_Review-g304555-d304576-Reviews-Shahpura_House-Jaipur_Jaipur_District_Rajasthan.html',
'https://www.tripadvisor.in/Hotel_Review-g303890-d604848-Reviews-Villa_Retreat-Kodaikanal_Dindigul_District_Tamil_Nadu.html',
'https://www.tripadvisor.in/Hotel_Review-g297605-d651438-Reviews-Santana_Beach_Resort-Candolim_Bardez_North_Goa_District_Goa.html',
'https://www.tripadvisor.in/Hotel_Review-g297685-d609694-Reviews-Ganpati_Guest_House-Varanasi_Varanasi_District_Uttar_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g635749-d6376843-Reviews-Bella_Vista_Resort-Mahabaleshwar_Satara_District_Maharashtra.html',
'https://www.tripadvisor.in/Hotel_Review-g304554-d299124-Reviews-The_Lalit_Mumbai-Mumbai_Maharashtra.html',
'https://www.tripadvisor.in/Hotel_Review-g304551-d306957-Reviews-Radisson_Blu_Plaza_Delhi_Airport-New_Delhi_National_Capital_Territory_of_Delhi.html',
'https://www.tripadvisor.in/Hotel_Review-g297628-d735365-Reviews-The_Monarch_Luxur-Bengaluru_Bangalore_District_Karnataka.html',
'https://www.tripadvisor.in/Hotel_Review-g297587-d3748122-Reviews-Fortune_Select_Grand_Ridge-Tirupati_Chittoor_District_Andhra_Pradesh.html',
'https://www.tripadvisor.in/Hotel_Review-g816969-d1220372-Reviews-Om_Sai_Beach_Huts-Agonda_South_Goa_District_Goa.html',
'https://www.tripadvisor.in/Hotel_Review-g297675-d10184114-Reviews-Hotel_Kiscol_Grands-Coimbatore_Coimbatore_District_Tamil_Nadu.html',
'https://www.tripadvisor.in/Hotel_Review-g303894-d13139721-Reviews-Hotel_Rameswaram_Grand-Rameswaram_Ramanathapuram_District_Tamil_Nadu.html',
'https://www.tripadvisor.in/Hotel_Review-g297628-d1400046-Reviews-Hotel_City_Centaur-Bengaluru_Bangalore_District_Karnataka.html',
'https://www.tripadvisor.in/Hotel_Review-g297628-d1400042-Reviews-Hill_View_Resorts-Bengaluru_Bangalore_District_Karnataka.html',
'https://www.tripadvisor.in/Hotel_Review-g297628-d1144028-Reviews-OYO_10885_Hotel_Keerthana_International-Bengaluru_Bangalore_District_Karnataka.html',
'https://www.tripadvisor.in/Hotel_Review-g297628-d3666489-Reviews-Royal_Inn_Hotel_Apartments-Bengaluru_Bangalore_District_Karnataka.html',
'https://www.tripadvisor.in/Hotel_Review-g297628-d1144202-Reviews-Roxel_Inn_Diamond_District-Bengaluru_Bangalore_District_Karnataka.html',
'https://www.tripadvisor.in/Hotel_Review-g297628-d4045459-Reviews-The_Woodbridge_Hotel_Delux_Lodging-Bengaluru_Bangalore_District_Karnataka.html'
]


# scrapping the reviews from each url
for url in urls:

	source_code = requests.get(url, headers=headers, timeout=15)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text,"html.parser")
	# uncomment the line below to scrape positive reviews
	# h2s = soup.findAll('a', {'class':'hotels-hotel-review-community-content-review-list-parts-ReviewTitle__reviewTitleText--2VUye'})
	try:
		bubbles = soup.findAll('span', {'class':'ui_bubble_rating bubble_20'}) # the negative reviews
		for bubble in bubbles:
			value = bubble.parent.next_sibling
			print(value.text)
			temp2 = [item.text for item in value]
			extra = [0]*len(temp2)
			
			# create a dataframe to store the reviews along with their statuses(0/1)
			mapped = zip(temp2, extra)
			df = pd.DataFrame(list(mapped))
			with open('data_new.csv', 'a') as f:
				df.to_csv(f, header=False, index=False)
	except Exception as e:
		print(str(e))

	print('Scrapped a hotel')
	
