import skimage.io as io
import skimage.transform as skt
import numpy as np
from PIL import Image, ImageOps
from src.models.class_patcher import patcher
from src.utils.imgproc import *


class patcher(patcher):
    def __init__(self, body, **options):
        super().__init__('京狐', './body/body_kyoko.png', pantie_position=[719, 1464], **options)

    def convert(self, image):
        # image = Image.open('./dream/0101.png')
        # @@@ Resize pantie image
        image = image.resize((int(image.width * 0.7), int(image.height * 0.7)), resample=Image.BICUBIC)
        # @@@ Convert pantie image to array
        pantie = np.array(image)
        #patch = np.copy(pantie[-140:-5, 546:, :])
        #pantie[-140:, 546:, :] = 0
        #patch = skt.resize(patch[::-1, ::-1, :], (160, 70), anti_aliasing=True, mode='reflect')
        #[pr, pc, d] = patch.shape
        #pantie[115:115 + pr, :pc, :] = np.uint8(patch * 255)

        #arrx = np.zeros(25)
        #arry = np.sin(np.linspace(0, np.pi, 25)) * 120 - 20
        #arry[3:11] -= np.sin(np.linspace(0, np.pi, 8)) * 100
        #pantie = affine_transform_by_arr(pantie, arrx, arry, smoothy=True, mvy=2)
        #pantie = np.uint8(pantie[:280, 18:-60] * 255)
        # @@@ Convert array to image
        return Image.fromarray(pantie)
