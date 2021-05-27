# List of books

"""
Code by:Vijayesh M T



Date:13/05/21
"""
list = ['Adventures of Tom Sawyer: Mark Twain',
        'Time Machine: H.G. Wells'
	, 'A passage to India: E.M.Forster'
	, 'Das Kapital : Karl Marx'
	, 'Chitra: R.N.Tagore'
	, 'My Experiments with Truth: Mahatma Gandhi']


class vijayesh_library:
	lst_of_books = list.copy()
	lst_of_books1 = list.copy()
	lst_of_books2 = list.copy()
	issued_books = []

	def __init__(self, list_of_books, library_name):
		self.list_of_books = list_of_books
		self.library_name = library_name

	print('\n')

	@classmethod
	def display(cls):
		print('\n')
		print('The list of books in the library : ', '\n')
		for i, j in enumerate(cls.lst_of_books2):
			print(i + 1, '-', j)
		print('\n')
		print('The availabe books in the library : ', '\n')
		for i, j in enumerate(vijayesh_library.lst_of_books):
			print(i + 1, '-', j)
		print('\n')
		return ' '

	@classmethod
	def issued_books1(cls):
		print('Issued books : ', '\n')
		if len(cls.issued_books) != 0:
			for i, j in enumerate(cls.issued_books):
				print(i + 1, '-', j)
		else:
			print('No books are issued')
		return ' '

	@classmethod
	def lend(cls):
		name = input('Enter your Name : ')
		lst = int(input('Select a book you want to lend : '))
		string = f'{cls.lst_of_books[lst - 1]} - This book is issued to MR/MRS.{name}'
		cls.issued_books.append(string)
		cls.lst_of_books.remove(cls.lst_of_books[lst - 1])
		return ' '

	@classmethod
	def return_(cls):
		name = input('Enter your Name :')
		lst = int(input('Enter the book number you want to return : '))
		cls.lst_of_books.insert(lst - 1, cls.lst_of_books1[lst - 1])
		string = f'{cls.lst_of_books1[lst - 1]} - This book is issued to MR/MRS.{name}'
		cls.issued_books.remove(string)
		return ' '

	@classmethod
	def donate(cls):
		donar = input('enter the name of the book : ')
		cls.lst_of_books.append(donar)
		cls.lst_of_books2.append(donar)
		cls.lst_of_books1.append( ( donar ) )
		return ' '



def main():
	book = vijayesh_library(list, 'Vijayesh''s''library')
	print("Welcome to Vijayesh's Library\n")
	while True:
		print(
			"Press\n1.To display books\n2.To lend book\n3.To return book\n4.To donate book\n5.To view lend details(Authorised Personal Only)\n6.To quit")
		n = input('Select an option from the above : ')

		if n == '1':
			print(book.display())
		elif n == '2':
			print(book.lend())
		elif n == '3':
			print(book.return_())
		elif n == '4':
			print(book.donate())
		elif n == '5':
			a = input("Enter User ID : ")
			b = input("Enter the Password : ")
			if a == '67584' and b == 'vijayesh@674':
				print(book.issued_books1())
			else:
				print('Invalid ID or Password')
				print('\n')
		elif n == '6':
			break
		else:
			print('Invalid input')
	exit(0)


if __name__ == "__main__":
	main()

