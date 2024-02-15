class Library:
  #Constructor
  def __init__(self, filename='books.txt'):
    #Simdi burada a+ ile olmasinin sebebi ekleme hem cikarma hem cekme.
    self.file = open(filename, 'a+')

  def __del__(self):
    # Obje kullanilmayi birakinca dokumani kapiyor.
    if self.file:
      self.file.close()

  def list_books(self):
    # Dokumanin basina aliyor cursor'u
    self.file.seek(0)
    #Satirlari tek tek boluyor ve books bir string listi veya arrayi haline geliyor.
    books = self.file.read().splitlines()
    #Burada tum kitaplari yapilarini vs boluyoruz.
    for book in books:
      book_info = book.split(',')
      print(f'Book: {book_info[0]}, Author: {book_info[1]}')

  def add_book(self):
    #Eklenmek istenen kitabin bilgilerini aliyoruz.
    title = input('Enter book title: ')
    author = input('Enter author name: ')
    release_year = input('Enter first release year: ')
    num_pages = input('Enter number of pages: ')
    #Dokumana yazdirilacak string'in kendisini hazirladik.
    book_info = f'{title},{author},{release_year},{num_pages}\n'
    #Kitap bilgisini database'e ekledik.
    self.file.write(book_info)

  def remove_book(self):
    title_to_remove = input('Enter the title of the book to remove: ')
    self.file.seek(0)
    books = self.file.read().splitlines()
    # Databaseden cikarilacak kitabi bulduk. 
    for book in books:
      book_info = book.split(',')
      if (book_info[0] == title_to_remove):
        books.remove(book)
        break
    # Elimizdeki yeni liste ile database'i yeniden yaptik. 
    self.file.truncate(0)
    for book in books:
      self.file.write(f'{book}\n')
      self.file.flush()


# Kutphane objesini olusturduk
lib = Library()

# Sonsuz dongumuzu ve menumuzu olusturduk. 
while True:
  print("*** MENU ***")
  print("1) List Books")
  print("2) Add Book")
  print("3) Remove Book")
  print("4) Exit")

  choice = input("Enter your choice: ")

  if choice == '1':
    lib.list_books()
  elif choice == '2':
    lib.add_book()
  elif choice == '3':
    lib.remove_book()
  elif choice == '4':
    break  # Exit the loop to end the program
  else:
    print("Invalid choice. Please choose again.")
