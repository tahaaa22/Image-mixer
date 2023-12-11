import numpy as np

class OurImage:
    def __init__(self, data):
        self.image_data = data
        self.magnitude = None
        self.phase = None
        self.real = None
        self.imaginary = None
        self.calculate_components()
        self.Components = [self.magnitude,self.phase,self.real,self.imaginary]

    def calculate_components(self):
    
        f_transform = np.fft.fft(self.image_data)
        f_transform_shifted = np.fft.fftshift(f_transform)

        self.magnitude = np.abs(f_transform_shifted)
        self.phase = np.angle(f_transform_shifted)
        self.real = np.real(f_transform_shifted)
        self.imaginary = np.imag(f_transform_shifted)



