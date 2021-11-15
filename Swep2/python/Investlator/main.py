""" The Investment object takes in three methods p = principle, i = interest, n = years.
    It calculate a particular investment over a certain period of time.
  """
  
class Investment(object):
      def __init__(self,p,i,n):
          self.p = p
          self.i = i
          self.n = n
          
      def checkInvestment(self):
          count = 0
          while(count<self.n):
              inv = self.i
              inv += 1
              print(inv)
              count += 1

          invest = self.p * inv
          print(invest)
          
      def printParams(self):
          print(f'Principal = ${self.p}, Interest = {self.i}, Rate = {self.n} ')