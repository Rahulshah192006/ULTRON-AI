
from covid import *
covid = Covid()
query = str(input())

def Covid():
    print(covid.get_status_by_country_name('india'))

if "Covid Cases" in query:
    Covid()