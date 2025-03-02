import requests
from bs4 import BeautifulSoup, Comment


def parse_mode_block_header(url, tag):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headers = soup.find_all(tag)
        for header in headers:
            print(header.text)
    else:
        print(f"Ошибка: {response.status_code}")


def parse_mode_site_headers(url):
    tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for tag in tags:
            elements = soup.find_all(tag)
            print(f"Теги '{tag}':")
            for element in elements:
                print(element.text.strip())
            print()  # Пустая строка для разделения
    else:
        print(f"Ошибка: {response.status_code}")


def parse_mode_block(url, tag, class_=None):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        if class_:
            titles = soup.find_all(tag, class_=class_)
        else:
            titles = soup.find_all(tag)
        for title in titles:
            print(title.get_text(strip=True))
    else:
        print("(ERROR FRAEMWORK): BAD PARSE")
        print(f'Ошибка при получении страницы: {response.status_code}')


def parse_mode_site(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text(separator='\n', strip=True)
        links = [a['href'] for a in soup.find_all('a', href=True)]
        headers = [header.get_text(strip=True) for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
        images = [img['src'] for img in soup.find_all('img', src=True)]
        meta_tags = {meta.get('name', ''): meta.get('content', '') for meta in soup.find_all('meta')}
        tables = []
        for table in soup.find_all('table'):
            rows = []
            for row in table.find_all('tr'):
                cells = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
                rows.append(cells)
            tables.append(rows)
        print("Текст страницы:")
        print(page_text)
        print("\nСсылки:")
        for link in links:
            print(link)
        print("\nЗаголовки:")
        for header in headers:
            print(header)
        print("\nИзображения:")
        for img in images:
            print(img)
        print("\nМета-теги:")
        for name, content in meta_tags.items():
            print(f"{name}: {content}")
        print("\nТаблицы:")
        for i, table in enumerate(tables, 1):
            print(f"Таблица {i}:")
            for row in table:
                print(row)
    else:
        print(f'Ошибка при получении страницы: {response.status_code}')


def get_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Ошибка при получении страницы: {response.status_code}")
        return None


def extract_titles(soup, tag='h1'):
    return [title.get_text(strip=True) for title in soup.find_all(tag)]


def extract_links(soup):
    return [a['href'] for a in soup.find_all('a', href=True)]


def extract_images(soup):
    images = []
    for img in soup.find_all('img', src=True):
        images.append({
            'src': img['src'],
            'alt': img.get('alt', ''),
            'title': img.get('title', '')
        })
    return images


def extract_meta_tags(soup):
    return {meta.get('name', ''): meta.get('content', '') for meta in soup.find_all('meta')}


def extract_tables(soup):
    tables = []
    for table in soup.find_all('table'):
        rows = []
        for row in table.find_all('tr'):
            cells = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
            rows.append(cells)
        tables.append(rows)
    return tables


def extract_paragraphs(soup):
    return [p.get_text(strip=True) for p in soup.find_all('p')]


def extract_lists(soup):
    lists = []
    for list_tag in soup.find_all(['ul', 'ol']):
        items = [item.get_text(strip=True) for item in list_tag.find_all('li')]
        lists.append(items)
    return lists


def extract_forms(soup):
    forms = []
    for form in soup.find_all('form'):
        inputs = {input_tag.get('name', ''): input_tag.get('value', '') for input_tag in form.find_all('input')}
        forms.append(inputs)
    return forms


def extract_comments(soup):
    return [comment for comment in soup.find_all(string=lambda text: isinstance(text, Comment))]


def extract_specific_elements(soup, tag, class_=None):
    if class_:
        return [elem.get_text(strip=True) for elem in soup.find_all(tag, class_=class_)]
    else:
        return [elem.get_text(strip=True) for elem in soup.find_all(tag)]


def extract_scripts(soup):
    return [script['src'] for script in soup.find_all('script', src=True)]


def extract_styles(soup):
    return [style['href'] for style in soup.find_all('link', rel='stylesheet')]


def extract_iframes(soup):
    return [iframe['src'] for iframe in soup.find_all('iframe', src=True)]


def extract_buttons(soup):
    return [button.get_text(strip=True) for button in soup.find_all('button')]


def extract_inputs(soup):
    inputs = []
    for input_tag in soup.find_all('input'):
        inputs.append({
            'name': input_tag.get('name', ''),
            'type': input_tag.get('type', ''),
            'value': input_tag.get('value', '')
        })
    return inputs


def extract_anchors(soup):
    return [a.get_text(strip=True) for a in soup.find_all('a')]


def extract_divs(soup, class_=None):
    if class_:
        return [div.get_text(strip=True) for div in soup.find_all('div', class_=class_)]
    else:
        return [div.get_text(strip=True) for div in soup.find_all('div')]


def extract_spans(soup, class_=None):
    if class_:
        return [span.get_text(strip=True) for span in soup.find_all('span', class_=class_)]
    else:
        return [span.get_text(strip=True) for span in soup.find_all('span')]


def parse_images(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        images = extract_images(soup)
        for img in images:
            print(f"Image URL: {img['src']}")
            print(f"Alt Text: {img['alt']}")
            print(f"Title: {img['title']}")
            print()
    else:
        print(f'Ошибка при получении страницы: {response.status_code}')
