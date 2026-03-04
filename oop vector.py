class twoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
      print(f"the vector is {self.i}i,{self.j}j")

class threeDvector(twoDvector):
   def __init__(self, i, j,k):
      super().__init__(i, j)
      self.k = k
   def showV(self):
       print(f"the three D vector is {self.i}i,{self.j}j,{self.k}k")


a = twoDvector(1,2)
a.show()
b = threeDvector(3,4,5)
b.showV()