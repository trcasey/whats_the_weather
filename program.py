import requests
import bs4

def main():
    print_the_header()

    code = input('What zipcode do you want the weather for (10023)? ')

    html = get_html_from_web(code)

    #parse teh html
    get_weather_from_html(html)

    #display for the forecast


def print_the_header():
    print('----------------------------------')
    print('            WEATHER APP           ')
    print('----------------------------------')
    print()


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    #print(url)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])

    return response.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()
    print(condition, temp, scale)

if __name__ == '__main__':
    main()