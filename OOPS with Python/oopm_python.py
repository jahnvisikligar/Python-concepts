#lets learn about the OOPM with python
from abc import ABC, abstractmethod
class Book(ABC):
  def __init__(self,title,author,price) -> None:
    self.title=title
    self.author=author
    self.__price=price
    self.__discount=None
  def set_discount(self,discount):
    self.__discount=discount
  def get_Price(self):
    if self.__discount:
      return (self.__price*(1-self.__discount))
    return self.__price
  @abstractmethod
  def __repr__(self):
    return f"""Book:{self.title},Author:{self.author},Price:{self.get_Price()}"""
#inheritance and polymorphism
class Novel(Book):
  def __init__(self, title, author, price,genre) -> None:
    super().__init__(title, author, price)
    self.genre=genre
  def __repr__(self):
    return f"""Novel:{self.title},Author:{self.author},Price:{self.get_Price()},Genre:{self.genre}"""

#book1=Book('ABC','DEF',100)
#book1.set_discount(0.20)
#print(book1)
novel1=Novel('GHI','JKL',120,'Fiction')
novel1.set_discount(0.20)
print(novel1)		







































