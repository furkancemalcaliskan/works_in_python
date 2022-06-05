

#class Matematik:
   
    #def topla(self,sayi1,sayi2):    #self classın ta kendisi, yazmak zorundayız.
        #return sayi1 + sayi2

    #def cikar(self,sayi1,sayi2):
        #return sayi1 - sayi2

    #def carp(self,sayi1,sayi2):
        #return sayi1 * sayi2
        
    #def bol(self,sayi1,sayi2):
        #return sayi1 / sayi2

class Matematik:
        
        def __init__(self,sayi1,sayi2):
            self.sayi1 = sayi1
            self.sayi2 = sayi2

        def topla(self):    #self classın ta kendisi, yazmak zorundayız.
            return self.sayi1 + self.sayi2

        def cikar(self):
            return self.sayi1 - self.sayi2

        def carp(self):
            return self.sayi1 * self.sayi2
        
        def bol(self):
            return self.sayi1 / self.sayi2

    
matematik = Matematik(2,78)
matematik2 = Matematik(3,76)
print("Toplam = " + str(matematik.topla()))