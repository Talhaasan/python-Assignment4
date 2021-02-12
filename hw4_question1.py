import numpy as np
import cv2

class ImageFilt:
    def _init_(self):    
        self.image_array = []
        self.width = 0
        self.height = 0
    
    def load_im(self):        
        self.image = cv2.imread('C:\\Users\\pc\\.spyder-py3\\openCV\\lena.png')
        
        if self.image.all == None:
             print("not finding image ")
             return False
        else:
             self.height, self.width, _ = self.image.shape
             self.image_array = np.asarray(self.image)
             
             return True
   
    def filter_im(self, f):
         if f == 0:
              self.kernel = np.ones((3, 3), np.float32) / 9
              
         elif f == 1:
              self.kernel = np.array([[-1,-1,-1], 
                                      [-1, 9,-1],
                                      [-1,-1,-1]])
        
         self.filtered_image = cv2.filter2D(self.image, -1, self.kernel)
    
    def plot_im(self):
    
        print(cv2.imshow("blur image",self.image), cv2.imshow("filter image",self.filtered_image))  
              

image = ImageFilt()  
image.load_im()

image.filter_im(0)
image.plot_im()

image.filter_im(1)
image.plot_im()