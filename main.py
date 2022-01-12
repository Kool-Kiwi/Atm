class Cars(object):
    def __init__(self,yourname,color,price,model):
        self.color=color
        self.yourname=yourname
        self.price=price
        self.model=model
    def info(self):
        print(self.yourname," has selected a ",self.model," for ",self.price," in ",self.color," colour.")


person1=Cars("Kavya","blue","1,00,000","audi")
person1.info()
person2=Cars("Jeevitha","green","1,00,00","ferrai")
person2.info()