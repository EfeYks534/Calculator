# Sözcük çözümleyicinin (Lexer) bize verdiği Token'leri anlamlandırmak
# ve üzerinde  işlem yapmak için  Parser kullanılıyor.


from Lexer import *


class Parser:
	def __init__(self, lexer):
		self.lexer = lexer
		self.variables = { "pi": 3.1415926 }

	def fetch(self):
		return self.lexer.lex()

	def putback(self, tok):
		self.lexer.restore(tok)

	def parse_atom(self): # En küçük birim
		tok = self.fetch()

		if tok.token == TK_MINUS:
			atom = self.parse_factor()
			return -atom
		elif tok.token == TK_PLUS:
			return self.parse_factor()
		elif tok.token == TK_NUMBER:
			return tok.val
		elif tok.token == TK_LPHAR:
			val = self.parse_expr()
			tok = self.fetch()

			if tok.token != TK_RPHAR:
				self.lexer.error(tok.pos, "Kapanmayan parantez (')' bekleniyordu)")

			return val
		elif tok.token == TK_IDENT:
			ntok = self.fetch()

			if ntok.token == TK_EQU:
				self.variables[tok.val] = self.parse_expr()
			else:
				self.putback(ntok)

			if tok.val not in self.variables:
				self.lexer.error(tok.pos, "'" + tok.val + "' adında bir değişken yok")
				return None

			return self.variables[tok.val]

		self.lexer.error(tok.pos, "Tanınmayan sözcük")
		return None

	def parse_factor(self):
		atom = self.parse_atom()

		tok = self.fetch()
		if tok.token == TK_EXCLAM:
			v = 1
			while atom > 1:
				v = v * atom
				atom = atom - 1

			return v
		elif tok.token == TK_CARET:
			atom2 = self.parse_atom()

			return pow(atom, atom2)

		self.putback(tok)

		return atom

	def parse_term(self): # Terim, çarpım ve bölme 
		f = self.parse_factor()

		tok = self.fetch()

		while tok.token == TK_STAR or tok.token == TK_SLASH:
			f2 = self.parse_factor()

			if tok.token == TK_STAR:
				f = f * f2
			else:
				f = f / f2

			tok = self.fetch()

		self.putback(tok)

		return f

	def parse_expr(self): # Toplama çıkarma
		f = self.parse_term()

		tok = self.fetch()

		while tok.token == TK_PLUS or tok.token == TK_MINUS:
			f2 = self.parse_term()

			if tok.token == TK_PLUS:
				f = f + f2
			else:
				f = f - f2

			tok = self.fetch()

		self.putback(tok)

		return f

	def parse(self):
		v = self.parse_expr()

		tok = self.fetch()
		while tok.token == TK_COMMA:
			v = self.parse_expr()
			tok = self.fetch()

		self.putback(tok)

		return v
