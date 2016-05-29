class AbstractFac(object):

    @classmethod
    def produce_a(cls):

        return cls.ProductA()

    @classmethod
    def produce_b(cls):

        return cls.ProductB()
