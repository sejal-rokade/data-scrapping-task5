from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

if __name__=='__main__':
    with sync_playwright() as p:
      browser=p.chromium.launch(headless=False)
      page=browser.new_page()

      page.goto('https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY')
      page.wait_for_load_state('domcontentloaded')
      page.wait_for_load_state('networkidle')
      page.wait_for_timeout(500)

      page.screenshot(full_page=True,path='laptops.png')

      lapHtml=page.inner_html('body')
      laptopParse=HTMLParser(lapHtml)

      laptopData=laptopParse.css('div._75nLfW')

      lapDetails=[]

      for laptop in laptopData:
         Title=laptop.css('div.KzDlHZ')[0].text()
         Specification=laptop.css('ul.G4BRas')[0].text()
         Rating=laptop.css('div.XQDdHH')[0].text()
         Price=laptop.css('div.hl05eU')[0].text()
         Img=laptop.css('img.DByuf4')[0].attributes.get('src')

         laptop={
            'Title':Title,
             'Specification':Specification,
             'Rating':Rating,
             'Price':Price,
             'ImgUrl':Img
         }

         lapDetails.append(laptop)

         print(f'Title:{Title}')
         print(f'Specification:{Specification}')
         print(f'Rating:{Rating}')
         print(f'Price:{Price}')
         print(f'ImgUrl:{Img}')


      
    


      