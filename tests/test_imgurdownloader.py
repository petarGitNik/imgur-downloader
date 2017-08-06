#!/usr/bin/python3


import pytest
from imgur.imgurdownloader import ImgurDownloader
from imgur.imgurdownloader import ImgurException


class TestImgurDownloader(object):
    """
    Class that tests imgur downloader class from the main package.
    """

    @pytest.fixture
    def single_image_i():
        return ImgurDownloader('http://i.imgur.com/0s7mWKz.jpg')

    @pytest.fixture
    def single_image_without_extension_i():
        return ImgurDownloader('http://i.imgur.com/0s7mWKz')

    @pytest.fixture
    def single_image_without_extension():
        return ImgurDownloader('http://imgur.com/0s7mWKz')

    @pytest.fixutre
    def album_a():
        return ImgurDownloader('http://imgur.com/a/vTTHZ')

    @pytest.fixture
    def album_gallery():
        return ImgurDownloader('http://imgur.com/gallery/vTTHZ')

    def test_invalid_link(self):
        """
        Test if the class raises exception for invalid link.
        """
        with pytest.raises(ImgurException):
            ImgurDownloader('https://www.reddit.com')

    def test_invalid_link_with_variation(self):
        """
        Test if the class raises exception for invalid link.
        """
        with pytest.raises(ImgurException):
            ImgurDownloader('https://www.reddit.com/imgur.com')
