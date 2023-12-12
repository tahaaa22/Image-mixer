import numpy as np
import cv2

class OurImage:
    def __init__(self, data):
        self.image_data = data
        self.magnitude = None
        self.phase = None
        self.real = None
        self.imaginary = None
        self.calculate_components()
        self.Components = [self.magnitude, self.phase, self.real, self.imaginary]

    def calculate_components(self):
    
        f_transform = np.fft.fft2(self.image_data)
        f_transform_shifted = np.fft.fftshift(f_transform)

        self.magnitude = cv2.normalize((20 * np.log(np.abs(f_transform_shifted))), None, 0, 255, cv2.NORM_MINMAX)
        self.phase = np.angle(f_transform_shifted)
        self.real = np.real(f_transform_shifted)
        self.imaginary = np.imag(f_transform_shifted)



