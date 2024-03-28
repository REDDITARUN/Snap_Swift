## 🚀 SnapSwift: Supercharge Your Image Scraping Experience!
---

SnapSwift is your go-to Python library for effortlessly downloading bulk images from Bing.com. Leveraging asynchronous URL requests, SnapSwift ensures blazing-fast downloads, making image scraping a breeze.

This library builds upon the foundation of the renowned Bing Image Downloader by [Gurugaurav](https://github.com/gurugaurav/bing_image_downloader), offering enhanced functionalities and performance. Unlike its predecessors, SnapSwift focuses solely on fetching images in JPG format, perfect for constructing image datasets. 


### 😱 Features

1. **Multi-Class Downloading**: SnapSwift allows users to download images belonging to multiple classes or categories simultaneously. This feature enables users to scrape images for diverse topics or themes in a single operation, streamlining the process of gathering data for various projects.

2. **Exclusive JPG Format Downloading**: SnapSwift exclusively downloads images in JPG format. By focusing solely on JPG images, SnapSwift ensures that users obtain consistent file types, simplifying the management and processing of downloaded images for building datasets or other applications.


### 📝 Disclaimer

SnapSwift empowers you to download a plethora of images from Bing. However, it's crucial to respect copyright terms and permissions. Please refrain from downloading or using any image that violates its copyright terms.

### 💻 How to Use

To get started with SnapSwift, follow these simple steps:

```bash
git clone https://github.com/REDDITARUN/Snap_Swift.git
cd Snap_Swift
pip install .
```

### 🛠️ Usage

Customize your image scraping parameters in the `runner.py` file to suit your needs. Specify your desired queries, limit, output directory, and more to tailor the scraping process to your requirements.

#### Parameters:

- `query_string`: String to be searched.
- `limit`: (optional, default is 100) Number of images to download.
- `output_dir`: (optional, default is 'dataset') Name of the output directory.
- `adult_filter_off`: (optional, default is True) Enable or disable adult content filtration.
- `force_replace`: (optional, default is False) Delete the folder if present and start a fresh download.
- `timeout`: (optional, default is 60) Timeout for connection in seconds.
- `filter`: (optional, default is "") Specify the type of images to filter, choose from [line, photo, clipart, gif, transparent].
- `verbose`: (optional, default is True) Enable verbose output messages during the download process.

---

**References:**

- [SnapSwift Repository](https://github.com/REDDITARUN/Snap_Swift)
- [Bing Image Downloader by Gurugaurav](https://github.com/gurugaurav/bing_image_downloader/tree/master)
