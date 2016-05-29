from abstractfac import AbstractFac
from ..product.producta2 import ProductA2
from ..product.productb2 import ProductB2


class FacTwo(AbstractFac):

    ProductA = ProductA2
    ProductB = ProductB2
