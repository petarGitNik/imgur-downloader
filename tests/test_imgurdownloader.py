#!/usr/bin/python3


import pytest
from imgur.imgurdownloader import ImgurDownloader
from imgur.imgurdownloader import ImgurException


@pytest.fixture
def single_image_i():
    return ImgurDownloader('http://i.imgur.com/0s7mWKz.jpg')

@pytest.fixture
def single_image_without_extension_i():
    return ImgurDownloader('http://i.imgur.com/0s7mWKz')

@pytest.fixture
def single_image_without_extension():
    return ImgurDownloader('http://imgur.com/0s7mWKz')

@pytest.fixture
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

def test_invalid_link_almost_correct(self):
    """
    Test if the class raises exception for invalid link.
    """
    with pytest.raises(ImgurException):
        ImgurDownloader('http://.iimgur.com/0s7mWKz')

def test_is_it_image_with_extension(single_image_i):
    """
    Test if the provided URL leads to an image or album.
    """
    assert single_image_i.is_it_image() == True

def test_is_it_image_without_extension_i(single_image_without_extension_i):
    """
    Test if the provided URL leads to an image or album.
    """
    assert single_image_without_extension_i.is_it_image() == True

def test_is_it_image_without_extension(single_image_without_extension):
    """
    Test if the provided URL leads to an image or album.
    """
    assert single_image_without_extension.is_it_image() == True

def test_is_it_album_image_with_extension(single_image_i):
    """
    Test if the provided URL leads to an image or album.
    """
    assert single_image_i.is_it_album() == False

def test_is_it_album_image_without_extension_i(single_image_without_extension_i):
    """
    Test if the provided URL leads to an image or album.
    """
    assert single_image_without_extension_i.is_it_album() == False

def test_is_it_album_image_without_extension(single_image_without_extension):
    """
    Test if the provided URL leads to an image or album.
    """
    assert single_image_without_extension.is_it_album() == False

def test_is_it_image_album_a(album_a):
    """
    Test if the provided URL leads to an image or album.
    """
    assert album_a.is_it_image() == False

def test_is_it_image_album_gallery(album_gallery):
    """
    Test if the provided URL leads to an image or album.
    """
    assert album_gallery.is_it_image() == False

def test_is_it_album_image_without_extension_i(album_a):
    """
    Test if the provided URL leads to an image or album.
    """
    assert album_a.is_it_album() == True

def test_is_it_album_image_without_extension(album_gallery):
    """
    Test if the provided URL leads to an image or album.
    """
    assert album_gallery.is_it_album() == True