# %%
import asyncio
from pyppeteer import launch
import nest_asyncio
nest_asyncio.apply()
from urllib.parse import urlparse
import time
import random

# %%
user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]

# %%
async def get_all_links(input_url):
    browserObj = await launch({"headless": False})
    url = await browserObj.newPage()
    await url.goto(input_url, timeout=0)
    link_elements = await url.querySelectorAll("a")
    links = []
    for link_element in link_elements:
        link_url = await url.evaluate('(element) => element.href', link_element)
        links.append(link_url)
    await browserObj.close()
    return links

async def main():
    url = 'https://tapaltea.com'  # Replace with your desired URL
    links = await get_all_links(url)
    for link in links:
        print(link)  
    return links 

link = asyncio.get_event_loop().run_until_complete(main())

# %%
link = list(set(link))
exclusion_list = ['unilever','twitter','facebook','instagram','youtube','.jpg','.png','tel','mailto']
links = [item for item in link if not any(exclude_word in item.lower() for exclude_word in exclusion_list)]
(links)

# %%

async def extract_text(url):
    browser = await launch({"headless": False})
    page = await browser.newPage()
    await page.setUserAgent(random.choice(user_agents_list))
    await page.goto(url, timeout=0)
    time.sleep(10)
    text = await page.evaluate('() => document.body.innerText')
    await browser.close()
    return text

for url in links[:-4]:
    text = await extract_text(url)
    parsed_url = urlparse(url)
    filename = url.replace("https://tapaltea.com/","").replace(".html","").replace("/","_") + ".txt"
    with open("C:\\Users\\Dell\\Desktop\\scrapper_tapal\\files" + filename, 'w') as f:
        f.write(text)

# %%



