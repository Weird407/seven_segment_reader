import cv2
import numpy as np


class finder(object):
    WNAME = "Select segments (r=reset, q=quit, c=finish)"

    def __init__(self, image):
        self._image = image
        self._orig = image.copy()

        self._coords = list()

    def _click(self, event, x, y, _, __):
        if event == cv2.EVENT_LBUTTONDOWN:
            self._coords.append((x, y))
            #print(x,y) #to test if it works correctly
            cv2.circle(self._image, (x, y), 5 ,(0, 255, 0), 2)

    def find_segment(self):
        cv2.namedWindow(self.WNAME)
        cv2.setMouseCallback(self.WNAME, self._click)
        example = cv2.imread("seven_segment.png")

        # resize to fit next to each other
        h = np.size(self._image,0)
        w = int(0.5*np.size(self._image,1))
        set = cv2.resize(example,(w,h))

        while True:
            cv2.imshow(self.WNAME, np.hstack([self._image, set]))
            key = cv2.waitKey(1) & 0xFF

            if key == ord("r"):
                self.reset()

            elif key == ord("q"):
                break

            elif key == ord("c"):
                cv2.destroyAllWindows()
                break

    @property
    def image(self):
        return self._image.copy()

    def reset(self):
        self._image = self._orig.copy()
        self._coords.clear()
