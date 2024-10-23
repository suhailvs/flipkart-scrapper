from bs4 import BeautifulSoup


class Parse:
    def __init__(self, fname= 'mobiles.html'):
        fp = open(fname)
        soup = BeautifulSoup(fp.read(), 'html.parser')
        self.products = soup.find_all("div", {"class": "tUxRFH"})
    
    def get_ratings(self,product):
        for rating in product.find_all("div", {"class": "_5OesEi"}):
            print('star:',rating.select_one(".XQDdHH").text)
            print(rating.select_one(".Wphh3N").text)
    
    def get_specs(self,product):
        for spec in product.find_all("li", {"class": "J+igdf"}):
            print(spec.text)
        
    def run(self):
        for product in self.products:
            print('='*100)
            self.get_ratings(product)
            print('-'*100)
            self.get_specs(product)
            print(product.select_one("._4b5DiR").text)

if __name__=='__main__':
    p = Parse()
    p.run()