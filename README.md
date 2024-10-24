# Flipcart Scrapper

scrap from website:

```
# for refrigerator,monitors, television, ac, mobiles, laptop
$ mkdir htmlfiles
$ python
from scrap import Flipkart
scrapper = Flipkart() 
scrapper.get('mobiles')

# for trimmers, speakers, earphone,beds
$ mkdir htmlfiles2
$ python
from scrap import Flipkart
scrapper = Flipkart('htmlfiles2')
scrapper.get('trimmers')
```

parse the scrapped html(refrigerator,monitors, television, ac, mobiles, laptop):

```
./manange.py runserver
for parse got to -> http://localhost:8000/p/1/
```