import cv2


class Cropper(object):
    WNAME = "Select the cropping region (r=reset, c=finish)"

    def __init__(self, image):
        self._image = image
        self._orig = image.copy()

        self._dragging = False
        self._coords = list()

    def _click_and_crop(self, event, x, y, _, __):
        if event == cv2.EVENT_LBUTTONDOWN:
            self._coords.clear()
            self._coords.append((x, y))
            self._dragging = True

        elif event == cv2.EVENT_LBUTTONUP and self._dragging:
            self._coords.append((x, y))

            cv2.rectangle(self._image, self._coords[0], self._coords[1], (0, 255, 0), 2)

    def crop(self):
        cv2.namedWindow(self.WNAME)
        cv2.setMouseCallback(self.WNAME, self._click_and_crop)

        while True:
            cv2.imshow(self.WNAME, self._image)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("r"):
                self.reset()

            elif key == ord("q"):
                break

            elif key == ord("c"):
                (x1, y1), (x2, y2) = self._coords
                #cropped = self._image[y1:y2, x1:x2]
                #self._image = cropped

                cv2.destroyAllWindows()
                break

    @property
    def image(self):
        return self._image.copy()

    def reset(self):
        self._image = self._orig.copy()
