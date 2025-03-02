# WebScraper
Библиотека WebScraper предназначена для простого и эффективного извлечения данных с веб-страниц. Она предоставляет набор функций для парсинга HTML-контента и извлечения различных элементов, таких как заголовки, ссылки, изображения и мета-теги.

Этот проект представляет собой набор функций для парсинга веб-страниц с использованием библиотек `requests` и `BeautifulSoup`.

## Установка

1. Убедитесь, что у вас установлен Python 3.7 или выше.
2. Установите необходимые зависимости:

```bash
pip install requests beautifulsoup4

для ручной устоновки поместите файл core в свой проект и импортируйте все функции с помощью
```python
from core import *

## документация:
Основные функции
parse_mode_block(url, tag, class_=None)
Парсит элементы по указанному тегу и классу.

Пример:

python
Copy
parse_mode_block('https://example.com', 'h1')
parse_mode_site(url)
Парсит всю страницу, извлекая текст, ссылки, заголовки, изображения, мета-теги и таблицы.

get_page_content(url)
Возвращает HTML-код страницы.

Дополнительные функции
extract_titles(soup, tag='h1'): Извлекает заголовки по указанному тегу.

extract_links(soup): Извлекает все ссылки.

extract_images(soup): Извлекает все изображения.

extract_meta_tags(soup): Извлекает мета-теги.

extract_tables(soup): Извлекает таблицы.

extract_paragraphs(soup): Извлекает параграфы.

extract_lists(soup): Извлекает списки.

extract_forms(soup): Извлекает формы.

extract_comments(soup): Извлекает HTML-комментарии.

extract_specific_elements(soup, tag, class_=None): Извлекает элементы по тегу и классу.

extract_scripts(soup): Извлекает внешние скрипты.

extract_styles(soup): Извлекает внешние стили.

extract_iframes(soup): Извлекает iframe.

extract_buttons(soup): Извлекает текст кнопок.

extract_inputs(soup): Извлекает input-элементы.

extract_anchors(soup): Извлекает текст ссылок.

extract_divs(soup, class_=None): Извлекает текст div-элементов.

extract_spans(soup, class_=None): Извлекает текст span-элементов.

Пример использования
python
Copy
from bs4 import BeautifulSoup
from parser import get_page_content, extract_titles, extract_links

url = 'https://example.com'
page_content = get_page_content(url)
if page_content:
    soup = BeautifulSoup(page_content, 'html.parser')
    titles = extract_titles(soup, 'h1')
    links = extract_links(soup)
    print("Заголовки:", titles)
    print("Ссылки:", links)
