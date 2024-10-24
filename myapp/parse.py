from bs4 import BeautifulSoup

class Parse:
    def __init__(self, fname="myapp/mobiles.html",my_model=None):
        fp = open(fname)
        soup = BeautifulSoup(fp.read(), "html.parser")
        self.products = soup.find_all("div", {"class": "tUxRFH"})
        self.result = {}
        self.my_model = my_model
        self.result['category'] = fname.split('_',1)[0]
    def get_ratings(self, product):
        for rating in product.find_all("div", {"class": "_5OesEi"}):
            self.result["star"] = rating.select_one(".XQDdHH").text
            self.result["ratings"] = rating.select_one(".Wphh3N").text
            

    def get_specs(self, product):
        # keys = ["ram", "display", "camera", "battery", "processor", "warranty"]
        data = {}
        for i, spec in enumerate(product.find_all("li", {"class": "J+igdf"})):
            data[str(i)]=spec.text
        self.result['details']=data

    def save_img(self):
        import urllib.request
        from pathlib import Path
        fname = f"myapp/static/img/{self.result['pid']}.jpeg"
        file_path = Path(fname)
        if file_path.is_file():
            print(f"File {fname} exists!")
        else:
            
            urllib.request.urlretrieve(self.result["image"], fname)

    def run(self):
        for product in self.products:
            self.result["link"] = product.select_one(".CGtC98")["href"]
            self.result['pid']=self.result['link'].rsplit('/',1)[1].split('?',1)[0]
            if self.my_model.objects.filter(pid=self.result['pid']):
                # print(':exists',self.result['pid'],self.result["price"],self.result["title"])
                continue
            print(self.result['pid'])
            
            self.result["title"] = product.select_one(".KzDlHZ").text
            try:
                self.result["price"] = product.select_one(".Nx9bqj").text
            except:
                print(self.result['pid'])
                print('-'*100)
            self.get_ratings(product)
            self.get_specs(product)
            self.result["link"] = product.select_one(".CGtC98")["href"]
            self.result["image"] = product.select_one(".DByuf4")["src"]
            
            # print('='*100)
            # import pprint
            # pprint.pprint(self.result, compact=True)
            if self.my_model:
                obj=self.my_model(**self.result)
                obj.save()
                self.save_img()
