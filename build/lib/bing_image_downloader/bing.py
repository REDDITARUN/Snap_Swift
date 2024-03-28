import imghdr
import posixpath
import urllib.parse
import urllib.request
from pathlib import Path
import re
class Bing:
    def __init__(self, query, limit, output_dir, adult, timeout, filter='', verbose=True):
        self.download_count = 0
        self.query = query
        self.output_dir = output_dir
        self.adult = adult
        self.filter = filter
        self.verbose = verbose
        self.seen = set()

        assert isinstance(limit, int), "limit must be integer"
        self.limit = limit
        assert isinstance(timeout, int), "timeout must be integer"
        self.timeout = timeout

        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                                       'AppleWebKit/537.11 (KHTML, like Gecko) '
                                       'Chrome/23.0.1271.64 Safari/537.11',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                        'Accept-Encoding': 'none',
                        'Accept-Language': 'en-US,en;q=0.8',
                        'Connection': 'keep-alive'}
        self.page_counter = 0

    def get_filter(self, shorthand):
        if shorthand == "line" or shorthand == "linedrawing":
            return "+filterui:photo-linedrawing"
        elif shorthand == "photo":
            return "+filterui:photo-photo"
        elif shorthand == "clipart":
            return "+filterui:photo-clipart"
        elif shorthand == "gif" or shorthand == "animatedgif":
            return "+filterui:photo-animatedgif"
        elif shorthand == "transparent":
            return "+filterui:photo-transparent"
        else:
            return ""

    def save_image(self, link, file_path):
        request = urllib.request.Request(link, None, self.headers)
        image = urllib.request.urlopen(request, timeout=self.timeout).read()
        if not imghdr.what(None, image):
            if self.verbose:
                print('[Error]Invalid image, not saving {}\n'.format(link))
            raise ValueError('Invalid image, not saving {}\n'.format(link))
        with open(file_path, 'wb') as f:
            f.write(image)

    def download_image(self, link):
        self.download_count += 1
        if self.verbose:
            print("[%] Downloading Image #{} from {}".format(self.download_count, link))
        # Always save images as JPEG
        file_path = self.output_dir / f"Image_{self.download_count}.jpg"
        try:
            self.save_image(link, file_path)
            if self.verbose:
                print("[%] File Downloaded as JPEG!\n")
        except Exception as e:
            self.download_count -= 1
            if self.verbose:
                print("[!] Issue getting: {}\n[!] Error:: {}".format(link, e))

    def run(self):
        while self.download_count < self.limit:
            if self.verbose:
                print('\n\n[!!]Indexing page: {}\n'.format(self.page_counter + 1))
            request_url = f'https://www.bing.com/images/async?q={urllib.parse.quote_plus(self.query)}' \
                          f'&first={self.page_counter}&count={self.limit}' \
                          f'&adlt={self.adult}&qft={self.get_filter(self.filter) if self.filter else ""}'
            request = urllib.request.Request(request_url, None, headers=self.headers)
            response = urllib.request.urlopen(request)
            html = response.read().decode('utf8')
            if not html:
                if self.verbose:
                    print("[%] No more images are available")
                break
            links = re.findall('murl&quot;:&quot;(.*?)&quot;', html)
            if self.verbose:
                print("[%] Indexed {} Images on Page {}.".format(len(links), self.page_counter + 1))
                print("\n===============================================\n")
            for link in links:
                if self.download_count < self.limit and link not in self.seen:
                    self.seen.add(link)
                    self.download_image(link)
            self.page_counter += 1
        if self.verbose:
            print("\n\n[%] Done. Downloaded {} images.".format(self.download_count))
