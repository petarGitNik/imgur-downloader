#!/usr/bin/python3


"""
Download images from imgur. Use this in combination with Imgur class. Example:

```python3
from imgur.imgurdownloader Import Imgur

imgur = Imgur('http(s)://imgur.com/[album_hash]')
imgur.prepare_images()
imgur.numerate_images()

downloader = Downloader(imgur.images, '/home/user/Download')
downloader.download()
```
"""


import os
from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError
from shutil import copyfileobj
from time import sleep


__author__ = 'petarGitNik'
__copyright__ = 'Copyright (c) 2017 petarGitNik petargitnik@gmail.com'
__license__ = 'MIT'
__version__ = 'v0.2.0'
__email__ = 'petargitnik@gmail.com'
__status__ = 'Production'


class DownloaderException(Exception):
    """
    Raise this exception if there is something wrong with supplied path or with
    downloading process.
    """
    pass


class Downloader(object):
    """
    This class downloads files from provided source.
    """

    def __init__(self, images, destination, verbose=False):
        """
        Initiate Downloader object, with information about current and destination
        directory.
        """
        self.images = images
        self.destination = self.is_valid_path(destination)
        self.verbose = verbose
        self.current_directory = os.getcwd()

    def download(self):
        """
        Download the images.
        """
        os.chdir(self.destination)

        currently_at = 1
        total = len(self.images)
        while self.images:
            image = self.images.popleft()

            if self.verbose: self.display_status(image['url'], currently_at, total)

            try:
                self.write_file_to_filesystem(image['url'], image['filename'])
            except HTTPError as e:
                if self.verbose:
                    print('Could not download, error status:', e.code)
            except URLError as e:
                if self.verbose:
                    print('Something went wrong:', e.reason)

            currently_at += 1
            sleep(2)

        os.chdir(self.current_directory)

    def is_valid_path(self, path):
        """
        Check if the given path to download directory exists. If not, raise
        exception.
        """
        if os.path.exists(path):
            return path
        raise DownloaderException('Destination directory does not exist.')

    def display_status(self, url, currently_at, total):
        """
        Display the link of the image which is being downloaded, and download
        progress.
        """
        print(
            'Progress: {}/{}. Downloading: {}'.format(
                currently_at, total, url
            )
        )

    def write_file_to_filesystem(self, url, filename):
        """
        Download and write a file to a file system.
        """
        with urlopen(url) as r, open(filename, 'wb') as f:
            copyfileobj(r, f)
