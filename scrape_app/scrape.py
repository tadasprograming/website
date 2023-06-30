import requests
import bs4

#url = "https://rekvizitai.vz.lt/imone/maxima_lt_uab/"

def scrape(url):
    res = requests.get(url)
    return bs4.BeautifulSoup(res.text,'lxml')
    '''except:
        return '#ERROR: Nepavyko nuskaityti nuorodos!'''

def find_info(soup):
    try:
        company_name = soup.select('.fn')
        company_name = company_name[0].text
    except:
        company_name = 'Įmonės pavadinimas nerastas'
        
    try:
        company_code_tag = soup.find('td', text='Įmonės kodas')
        company_code = company_code_tag.find_next_sibling('td')
        company_code = company_code.text.strip()
    except:
        company_code = 'Įmonės kodas nerastas'

    try:
        company_address_elem = soup.find('td', {'itemprop': 'address'})
        company_address = company_address_elem.get_text(strip=True)
    except:
        company_address = 'Įmonės adresas nerastas'

    try:
        company_boss_tag = soup.find('td', text='Vadovas')
        company_boss = company_boss_tag.find_next_sibling('td')
        company_boss = company_boss.text.strip()
    except:
        company_boss = 'Informacija apie vadovą nerasta'

    return {'name':company_name,'code':company_code,\
            'address':company_address,'boss':company_boss}






