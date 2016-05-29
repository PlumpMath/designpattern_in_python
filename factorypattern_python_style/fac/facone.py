from abstractfac import AbstractFac
from ..product.producta import ProductA
from ..product.productb import ProductB


class FacOne(AbstractFac):
    ProductA = ProductA
    ProductB = ProductB
