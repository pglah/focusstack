import os
import cv2


class ImageReader():
    def __init__(self, image_files):
        self.image_files = image_files

    def read(self):
        focus_images = []
        for image in self.image_files:
            print(f"Reading in file {image}")
            image_type = image.split('.')[-1].lower()
            if image_type in ['png', 'jpg', 'jpeg']:
                image = self._read_with_open_cv(image)
            elif image_type == 'raw':
                image = self._read_as_matrice(image)
            else:
                raise Exception('Image Type not supported')

            focus_images.append(image)

        return focus_images

    def _read_with_open_cv(self, image):
        return cv2.imread(f'input/{image}')

    def _read_as_matrice(self, image):
        pass
