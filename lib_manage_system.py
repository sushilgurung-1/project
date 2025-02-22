## Library Management System:

class Member:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def __repr__(self):
    return f"{self.name} : {self.age}"
  
# book class 
class book:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def __repr__(self):
    return f"{self.name} : {self.price}"
  
class Library:
  """ 
  1. Library class to add, remove and display books
  2. Member class to add, remove and display members
  """
  def __init__(self):
    self.dic_book = {}
    self.dic_member = {}
    self.borrow_record = {}
    
  def add_book(self, book):
    """
    Add book to the library
    """
    if book.name in self.dic_book:
      print("Book already exist!")
    else:
      # self.dic_book[book] = price
      self.dic_book[book.name] = book
      print("book added succesfully!")

  def remove_book(self):
    """
    Remove book from the library
    """
    print("Books available")
    self.display_books()
    book = input("Book name you want to remove: ").strip().capitalize()
    if book in self.dic_book:
      self.dic_book.pop(book)
      print("book remove done!")
    else:
      print("Book isn't available as you mentioned")

  def display_books(self):
    """
    Display books available in the library
    """
    print("\nBooks available")
    for book,price in self.dic_book.items():
      print(book,":", price)

  def add_memnber(self, member):
    """
    Add member to the library
    """
    if member.name in self.dic_member:
      print("Member already exist!")
    else:
      self.dic_member[member.name] = member
      print("Member added succesfully!")
    self.display_member()

  def display_member(self):
    """
    Display members available in the library
    """
    print("\nMembers available")
    for member in self.dic_member:
      print(member)

  def remove_member(self):
    """
    Remove member from the library
    """
    print("Members available")
    self.display_member()
    member = input("Member name you want to remove: ").strip().capitalize()
    if member in self.dic_member:
      self.dic_member.pop(member)
      print("Member remove done!")
    else:
      print("Member isn't available as you mentioned")
  
  def take_borrow(self, member, book):
    """
    Take borrow of the book
    """
    if member.name not in self.dic_member:
      # if book.name in self.dic_book:
        self.borrow_record[member.name] = book
        del self.dic_book[book.name]
        print("Borrow done!")
    else:
      print("Member is available as you mentioned")
    
  def borrow_details(self):
    """
    Display borrow details
    """
    print("\nBorrow details")
    for member, book in self.borrow_record.items():
      print(member,":", book)


def main():
  """
  Main function to test the library management system
  """
  book1 = book("Python", 100)
  book2 = book("Java", 200)
  book3 = book("C++", 300)
  book4 = book("C", 400)

  member1 = Member("John", 25)
  member2 = Member("Doe", 30)
  member3 = Member("Smith", 35)

  # test library class
  library = Library()
  
  # book add,remove, display
  library.add_book(book1)
  library.add_book(book2)
  library.add_book(book3)
  library.display_books()
  library.remove_book()

  # add,remove, display member
  library.add_memnber(member1)
  library.add_memnber(member2)
  library.remove_member()

  # add borrow
  library.take_borrow(member1, book1)
  library.borrow_details()

if __name__ == "__main__":
  main()

