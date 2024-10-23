# Flipcart Scrapper

scrap from website:

```
from myapp.scrap import Flipkart
scrapper = Flipkart()
scrapper.get('mobiles')
```

parse the scrapped html:

```
from myapp.parse import Parse
p = Parse()
p.run()
```