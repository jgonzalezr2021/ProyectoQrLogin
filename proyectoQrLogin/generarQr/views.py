import qrcode
import barcode
from django.utils.encoding import smart_str
from django.shortcuts import render
from barcode.writer import ImageWriter
from django.http import HttpResponse

def generate_file(barcode_file):
    # output = HttpResponse(content_type="image/jpeg")
    output = HttpResponse(content_type="application/force-download")
    barcode_file.save(output, "JPEG")
    output['Content-Disposition'] = 'attachment; filename=%s' % smart_str('barcode.jpg')
    output['X-Sendfile'] = smart_str('barcode.jpg')
    return output