import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1200,720)
    camera.start_preview()
    camera.exposure_compensation = 2
    #camera.exposure_mode = 'spotlight'
    #camera_meter_mode = 'matrix'
    camera.image_effect = 'gpen'
    
    time.sleep(20)
    camera.exif_tags['IFD0.Arist'] = 'Kim'
    camera.exif_tags['IFD0.Copyright'] = 'CopyleftKim'

    camera.capture('foo.jpg')
    camera.stop_preview()