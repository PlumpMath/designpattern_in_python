from abstractfac import AbstractFac
from ..product.producta2 import ProductA2
from ..product.productb2 import ProductB2


class FacTwo(AbstractFac):

    def produce_a(self):

        return ProductA2()

    def produce_b(self):

        return ProductB2()
