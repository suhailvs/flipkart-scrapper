from bs4 import BeautifulSoup


class Parse:
    def __init__(self, fname="myapp/mobiles.html",my_model=None):
        fp = open(fname)
        soup = BeautifulSoup(fp.read(), "html.parser")
        self.products = soup.find_all("div", {"class": "tUxRFH"})
        self.result = {}
        self.my_model = my_model

    def get_ratings(self, product):
        for rating in product.find_all("div", {"class": "_5OesEi"}):
            self.result["star"] = rating.select_one(".XQDdHH").text
            self.result["ratings"] = rating.select_one(".Wphh3N").text
            

    def get_specs(self, product):
        keys = ["ram", "display", "camera", "battery", "processor", "warranty"]
        for i, spec in enumerate(product.find_all("li", {"class": "J+igdf"})):
            self.result[keys[i]] = spec.text

    def run(self):
        for product in self.products:
            self.result["title"] = product.select_one(".KzDlHZ").text
            self.get_ratings(product)
            self.get_specs(product)
            self.result["link"] = product.select_one(".CGtC98")["href"]
            self.result["image"] = product.select_one(".DByuf4")["src"]
            print('='*100)
            import pprint
            pprint.pprint(self.result, compact=True)
            if self.my_model:
                obj=self.my_model(**self.result)
                obj.save()

        
if __name__ == "__main__":
    p = Parse()
    p.run()
