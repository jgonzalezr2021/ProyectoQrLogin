from django.shortcuts import render
import os
import time
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse, StreamingHttpResponse
from PIL import Image
from pyzbar.pyzbar import decode
from utils.camera_streaming_widget import CameraStreamingWidget

# alimentacion de la camara
def camera_feed(request):
    stream = CameraStreamingWidget()
    frames = stream.get_frames()

    #