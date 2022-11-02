import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(URL):

    '''A function that finds the html tags used as references for needed citations and returns their length.'''

    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations_needed = len(soup.find_all('a', text='citation needed'))
    return citations_needed


def get_citations_needed_report(URL):

    '''A function that finds the html tags a ref for required citations, saves its contents, 
    and returns the content with the required citations.'''

    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations_needed = soup.find_all('a', text='citation needed')
    entries = []
    for i in citations_needed:
        entries.append(i.find_parents('p')[0].text.strip())
    result = '\n\n'.join(entries)
    return result


URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
count = get_citations_needed_count(URL)
citations = get_citations_needed_report(URL)

print(f"{count} citations needed: \n\n")
print(citations)
