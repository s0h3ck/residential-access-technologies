from urllib.request import urlopen
from urllib.error   import HTTPError

def check_url_internet_country(country):
    ## Testing URL
    wikipedia = 'https://en.wikipedia.org/wiki/'

    ## Internet_in_COUNTRY test
    try:
        url = wikipedia + 'Internet_in_' + country
        response = urlopen(url)
    except HTTPError:
        try:
            ## Telecommunications_in_COUNTRY test
            url = wikipedia + 'Telecommunications_in_' + country
            response = urlopen(url)
        except HTTPError:
            return 'none'

    return response.geturl();      

while True:
    country = input('Enter the country name : ')

    url = check_url_internet_country(country)
    if url != 'none':
        print('[' + country + '](residential-access-technologies.md#' + country + ')([wiki](' + url + '))')
        print('##' + country + '\n')
    else:
        print('Nothing match with ' + country + '\n')
