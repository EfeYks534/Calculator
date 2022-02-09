# Bir karakter dizisini (örnek: "3 / 2(2+1)") alıp parçalarına ayırmak
# için `Lexer` kullanılıyor. Lexer kararakter  dizisini alıp sayıları,
# sembolleri 'Token'lere dönüştürüyor yani sözcüklerine ayırıyor.
#  Örnek:
# "3 / 2" -> [(numara, 3), (slash), (numara, 2)]


TK_IDENT  =  0 # Kelime (a-z, A-Z, _)
TK_NUMBER =  1 # Numara
TK_STRING =  2 # Karakter dizisi
TK_PLUS   =  3 # +
TK_MINUS  =  4 # -
TK_STAR   =  5 # *
TK_SLASH  =  6 # /
TK_EQU    =  7 # =
TK_LPHAR  =  8 # (
TK_RPHAR  =  9 # )
TK_LBRACK = 10 # [
TK_RBRACK = 11 # ]
TK_LCURLY = 12 # {
TK_RCURLY = 13 # }
TK_EXCLAM = 14 # !
TK_COMMA  = 15 # ,
TK_CARET  = 16 # ^

TK_EOF    = -1 # Kaynak karakter dizisinin sonu
TK_ERROR  = -2 # Hatalı kaynak karakter dizisi

# Numerik Token'leri karakter dizisine dönüştürmek için liste
token_names = ["<ERROR>", "<EOF>", "IDENT", "NUMBER", "STRING", "PLUS", "MINUS", "STAR", "SLASH", "EQU", "LPHAR", "RPHAR", "LBRACK", "RBRACK", "LCURLY", "RCURLY", "EXCLAM"]

def token_name(tok):
	return token_names[tok + 2]


class Token:
	def __init__(self, pos, token, val):
		self.token = token
		self.val   = val
		self.pos   = pos

		# print("Token( ", pos, ", ", token, ", ", val, ")")

	def __str__(self):
		repr = "(" + token_name(self.token)

		if self.val is not None:
			repr = repr + ", " + str(self.val)

		repr = repr + ")"

		return repr

class Lexer:
	def __init__(self, src):
		self.src  = src # Kaynak karakter dizisi
		self.pos  = 0   # Kaynağın içindeki konum

	def error(self, pos, msg=None): # Hata fonksiyonu
		pos = self.pos if pos == None else pos

		if msg != None:
			print(pos, ": ", msg)
			exit()

		return Token(pos, TK_ERROR, None)

	def advance(self): # Bir karakter ilerlet
		if self.pos == len(self.src):
			return '\0'

		ch = self.src[self.pos]
		self.pos = self.pos + 1

		return ch

	def eof(self):
		return self.pos == len(self.src)

	def restore(self, token):
		self.pos = 0 if token == None else int(token.pos)

	def lex(self):
		if self.eof():
			return Token(self.pos, TK_EOF, None) # Kaynak karakter dizisinin sonu

		ch = self.advance()

		while ch.isspace():
			ch = self.advance()

		pos = self.pos - 1

		if ch.isdigit():
			num = 0
			j = 0 # Ondalık kısımdaki basamak sayısı
			is_float = False

			while True:
				if ch == '.':
					is_float = True # Reel sayı
					ch = self.advance()
					continue

				if ch.isalpha():
					return self.error(pos) # Sayıda beklenmeyen karakter

				if ch.isdigit() == False:
					if is_float:
						num = num * pow(10, -j) # Ondalık kısımı sağa kaydır

					self.pos = self.pos - 1
					return Token(pos, TK_NUMBER, num)

				num = num * 10 + int(ch[0])

				if is_float:
					j = j + 1

				ch = self.advance()

		if ch.isalpha() or ch == '_':
			identifier = ""
			while ch.isalpha() or ch.isdigit() or ch == '_':
				identifier = identifier + ch
				ch = self.advance()

			self.pos = self.pos - 1

			return Token(pos, TK_IDENT, identifier)

		if ch == '"':
			ch = self.advance()

			string = ch

			while ch != '"':
				ch = self.advance()

				if ch == '\0': # Karakter dizisinde beklenmeyen bitiş
					return self.error(pos)

				if ch != '"':
					string = string + ch

			return Token(pos, TK_STRING, string)

		if ch == '+':
			return Token(pos, TK_PLUS, None)
		elif ch == '-':
			return Token(pos, TK_MINUS, None)
		elif ch == '*':
			return Token(pos, TK_STAR, None)
		elif ch == '/':
			return Token(pos, TK_SLASH, None)
		elif ch == '=':
			return Token(pos, TK_EQU, None)
		elif ch == '(':
			return Token(pos, TK_LPHAR, None)
		elif ch == ')':
			return Token(pos, TK_RPHAR, None)
		elif ch == '[':
			return Token(pos, TK_LBRACK, None)
		elif ch == ']':
			return Token(pos, TK_RBRACK, None)
		elif ch == '{':
			return Token(pos, TK_LCURLY, None)
		elif ch == '}':
			return Token(pos, TK_RCURLY, None)
		elif ch == '!':
			return Token(pos, TK_EXCLAM, None)
		elif ch == ',':
			return Token(pos, TK_COMMA, None)
		elif ch == '^':
			return Token(pos, TK_CARET, None)

		return self.error(pos)
