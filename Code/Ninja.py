class Ninja(object):
	def __init__(self, v):
		if isinstance(v, str):
			self.value = int(v)
		else:
			self.value = v

	def _get_elements(self, x):
		return [i for i in range(1,x+1) if "8" not in str(i)]

	def __add__(self, other):
		y = self._get_elements(other.value)
		in_val = self.value
		c = 0
		while c != len(y):
			if "8" not in str(in_val + 1):
				c += 1
			in_val += 1
				
		return Ninja(in_val)

	def __sub__(self, other):
		y = self._get_elements(other.value)
		in_val = self.value
		c = 0
		while c != len(y):
			if "8" not in str(in_val - 1):
				c += 1
			in_val -= 1
		return Ninja(in_val)

	def __mul__(self, other):
		y = self._get_elements(other.value)
		new = self
		for i in range(1,len(y)):
			new = new + self
		return new

	def __div__(self, other):
		
		in_val = Ninja(1)
		rem = self - other
		while rem.value > 0:
			rem = rem - other
			if rem.value < 0:
				break
			in_val += Ninja(1)
		return in_val



	def __str__(self):
		return str(self.value)

N = int(input())
	
for i in range(N):
	num = input()
	if "+" in num:
		a,b = num.split("+")
		print(Ninja(a) + Ninja(b))
	elif "-" in num:
		a,b = num.split("-")
		print(Ninja(a) - Ninja(b))
	elif "*" in num:
		a,b = num.split("*")
		print(Ninja(a) * Ninja(b))
	elif "/" in num:
		a,b = num.split("/")
		print(Ninja(a) / Ninja(b))