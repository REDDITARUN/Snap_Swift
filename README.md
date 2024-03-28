
## SnapSwift: Accelerating Your Image Scraping Experience!
<hr>

Python library to download bulk of images form Bing.com. This package uses async url, which makes it very fast while downloading.<br/>

This SnapSwift is an extension of Bing Image Downloader by https://github.com/gurugaurav/bing_image_downloader/tree/master, you can access form this link here.


### Disclaimer<br />

This program lets you download tons of images from Bing.
Please do not download or use any image that violates its copyright terms. 

### How to Use <br />

```bash
git clone https://github.com/REDDITARUN/Snap_Swift.git
cd Snap_Swift
pip install .
```



### Usage <br />

Go to the test.py file and make your modifications, like which photoes you want put the tags in query, and limit and etc etc. for images on single topic you can put in `queries = ["lambo"]` if you need multiple quiries to be searched then you can keep `queries = ["iphone", "Samsung"]`. 

`query_string` : String to be searched.<br />
`limit` : (optional, default is 100) Number of images to download.<br />
`output_dir` : (optional, default is 'dataset') Name of output dir.<br />
`adult_filter_off` : (optional, default is True) Enable of disable adult filteration.<br />
`force_replace` : (optional, default is False) Delete folder if present and start a fresh download.<br />
`timeout` : (optional, default is 60) timeout for connection in seconds.<br />
`filter` : (optional, default is "") filter, choose from [line, photo, clipart, gif, transparent]<br />
`verbose` : (optional, default is True) Enable downloaded message.<br />





