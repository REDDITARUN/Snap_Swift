import sys
from bing_image_downloader import downloader

# queries = [ "baking powder", 
#            "basil", "basmati_rice", "beans", "beets", "blackberries", "black_pepper", 
#            "bread", "bread_crumbs", "bread_flour", "brown_rice", "butter", "cabbage", 
#            "cardamom", "carrot", "cashews", "cauliflower", "cereal", "cheese", "chicken"]

queries = [
     "lambo"
]
for query in queries:
    if len(sys.argv) == 3:
        filter = sys.argv[2]
    else:
        filter = ""
        
    downloader.download(
        query,
        limit=50,
        output_dir="dataset_dem",
        adult_filter_off=True,
        force_replace=False,
        timeout=120,
        filter=filter,
        verbose=True,
    )
