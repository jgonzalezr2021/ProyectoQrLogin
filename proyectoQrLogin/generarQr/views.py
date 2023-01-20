import qrcode
import barcode
from django.utils.encoding import smart_str
from django.shortcuts import render
from barcode.writer import ImageWriter
from django.http import HttpResponse