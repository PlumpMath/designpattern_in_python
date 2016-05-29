from abstractfac import AbstractFac
from ..product.producta import ProductA
from ..product.productb import ProductB


class FacOne(AbstractFac):

    def produce_a(self):
        return ProductA()

    def produce_b(self):
        return ProductB()
