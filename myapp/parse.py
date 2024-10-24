from bs4 import BeautifulSoup

class BaseParser:
    def __init__(self, fname="myapp/mobiles.html",my_model=None,product_class="tUxRFH"):
        fp = open(fname)
        soup = BeautifulSoup(fp.read(), "html.parser")
        # self.products = soup.find_all("div", {"class": "_75nlfW"})
        self.products = soup.find_all("div", {"class": product_class})      
        self.my_model = my_model
        self.category = fname.split('_',1)[0]

    def get_ratings(self, product):
        for rating in product.find_all("div", {"class": "_5OesEi"}):
            self.result["star"] = rating.select_one(".XQDdHH").text
            self.result["ratings"] = rating.select_one(".Wphh3N").text

    def get_price_image(self, product):
        # self.result["image"] = product.select_one(".DByuf4")["src"]
        self.result["image"] = product.select_one(".DByuf4")["src"]
        try:
            self.result["price"] = product.select_one(".Nx9bqj").text
        except:
            print(f"error:{self.result['pid']}")

    def get_pid(self):
        self.result['pid'] = self.result['link'].rsplit('/',1)[1].split('?',1)[0]
        return self.result['pid']
    
    def save_img(self):
        import urllib.request
        from pathlib import Path
        fname = f"myapp/static/img/{self.result['pid']}.jpeg"
        file_path = Path(fname)
        if file_path.is_file():
            print(f"File {fname} exists!")
        else:            
            urllib.request.urlretrieve(self.result["image"], fname)

    def save(self):
        obj=self.my_model(**self.result)
        obj.save()
        self.save_img()
        print(f"saved: {self.result['pid']}")


class Parse(BaseParser):
    def get_specs(self, product):
        # keys = ["ram", "display", "camera", "battery", "processor", "warranty"]
        data = {}
        for i, spec in enumerate(product.find_all("li", {"class": "J+igdf"})):
            data[str(i)]=spec.text
        self.result['details']=data

    
    def run(self):
        for product in self.products:
            self.result = {'category':self.category}
            self.result["link"] = product.select_one(".CGtC98")["href"]
            pid=self.get_pid()
            if self.my_model.objects.filter(pid=pid):
                continue     
            self.result["title"] = product.select_one(".KzDlHZ").text
            
            self.get_ratings(product)
            self.get_specs(product)
            self.get_price_image( product)   
            self.save()

class Parse2(BaseParser):
    def __init__(self, fname,my_model):
        super().__init__(fname,my_model,"_75nlfW")
    def run(self):   
        for four_products in self.products:            
            for product in four_products.find_all("div", {"class": "slAVV4"}):
                self.result = {'category':f's_{self.category}'}
                a_tag = product.select_one(".wjcEIp")
                self.result['title'] = a_tag['title']
                self.result["link"] = a_tag['href']                
                
                self.result['details'] = {
                    '1':product.select_one(".NqpwHC").text if product.select_one(".NqpwHC") else ''
                }
                pid=self.get_pid()
                self.get_ratings(product)   
                self.get_price_image( product)         
                self.save()