from Lexer import *
from Parser import *



# Program başlangıç noktası
def main():
	while True:
		lexer = Lexer(input("$ "))
		parser = Parser(lexer)

		print(parser.parse())


if __name__ == "__main__":
	main()
