# Image Mixer - Python Desktop Application

## Overview

**Image Mixer** is a desktop application developed in Python using PyQt5 that allows users to manipulate and mix components of up to four images. The application provides various features such as converting colored images to grayscale, resizing images to a uniform size, displaying specific components of an image (Magnitude, Phase, Real Part, Imaginary Part), and more.

![image](https://github.com/tahaaa22/Image-mixer/assets/66066832/e5f6dda2-45ee-48ff-9177-c127a7d2a33a)

![image](https://github.com/tahaaa22/Image-mixer/assets/66066832/727408ee-b02d-475d-ac64-3a2ce9a684c1)

![image](https://github.com/tahaaa22/Image-mixer/assets/66066832/21b87f33-0b2b-4843-8ff1-65c4ef79e62b)

## Features

1. **Converting to Grayscale**: Convert colored images to grayscale effortlessly.

2. **Uniform Resizing**: Resize all loaded images to a uniform size for consistency.

3. **Component Display**: Display and visualize specific components of an image, including Magnitude, Phase, Real Part, and Imaginary Part.

4. **Mixing Components (Mood 1)**: Mix any of the four components with another image's components at a chosen ratio. Users can control the percentage contribution of each image's component.

5. **Region Mixing (Mood 2)**: Mix a region from a component of one image with other images. Regions can be either inner or outer, corresponding to high frequencies.

6. **Multithreading**: The application is designed to execute two processes synchronously, improving performance and responsiveness.

7. **Logging Results**: All results, including processed images and user interactions, are logged into a `results.log` file for future reference and analysis.

8. **Brightness and Contrast Modification**: Easily modify the brightness and contrast of an image by clicking on the image and dragging the mouse in the vertical or horizontal direction.

## Dependencies

The application relies on the following Python libraries:

- `logging`: For logging results into a file.
- `PyQt5.QtCore`: Core functionality for the PyQt5 framework.
- `cv2`: OpenCV library for image processing.
- `numpy`: Fundamental package for scientific computing with Python.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/tahaaa22/Image-Mixer.git
   cd Image-Mixer
   ```

2. Install dependencies:

   ```bash
   pip install cv2 numpy
   ```

3. Run the application:

   ```bash
   python Application.py
   ```

## Contributing

Contributions are welcome! If you have any ideas, bug reports, or feature requests, please open an issue on the GitHub repository.


Feel free to explore, modify, and enhance the capabilities of Image Mixer. If you have any questions or encounter issues, don't hesitate to reach out!
