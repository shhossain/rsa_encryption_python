from math import gcd
import random
from prime_numbers import prime_numbers as p
import numpy as np


def cf(num1:int,num2:int)->int:
    n = []
    g = gcd(num1, num2)
    for i in range(1, g+1): 
        if g%i==0: 
            n.append(i)
    return n

def fi(p,q)->int:
	return (p-1)*(q-1)


class RSA:
	def __init__(self):
		self.generate_key()

	def generate_key(self):
		self.p ,self.q = random.choice(p),random.choice(p)
		self.n = self.p*self.q
		self.phi = fi(self.p,self.q)
		self.e = self.get_e()
		self.d = self.get_d()

		self.public_key = (self.e,self.n)
		self.private_key = (self.d,self.n)

		r = {'public':self.public_key,'private':self.private_key}

		return r

	def get_e(self)->int:
		for i in range(2,self.phi):
			if len(cf(self.n,i)) == 1 and len(cf(self.phi,i))==1:
				return i

	def get_d(self)->int:
		d_table = {'row1':[self.phi,self.e],'row2':[self.phi,1]}

		while True:
			row1 = d_table['row1']
			row2 = d_table['row2']

			result = row1[0]//row1[1]

			r1 = result * row1[1]

			r2 = result * row2[1]

			new_r1_c1 = row1[0] - r1
			new_r2_c1 = row2[0] - r2

			if new_r2_c1 < 0 :
				new_r2_c1 = new_r2_c1%self.phi

			if new_r1_c1 == 1:
				# print('d',new_r2_c1)
				return new_r2_c1
				# break


			d_table['row1'][0] = row1[1]
			d_table['row2'][0] = row2[1]

			d_table['row1'][1] = new_r1_c1
			d_table['row2'][1] = new_r2_c1


	# @staticmethod
	def toBinary(self,text):
	  return [int(ord(i)) for i in text]

	def toString(self,binary_string_list):
	  return "".join([chr(i) for i in binary_string_list])

	def encrypt(self,text:str,public_key:tuple=None)->int:

		if public_key == None:
			public_key = self.public_key

		e,n = public_key

		text_to_bin_list = self.toBinary(text)
		text_to_bin_list_np = np.array(text_to_bin_list,dtype='object')
		# print(text_to_bin_list_np,text_to_bin_list_np.dtype)

		encrypted_text_list = np.mod(np.power(text_to_bin_list_np,e),n)


		# print("ET",encrypted_text_list)

		return encrypted_text_list
		

	def decrypt(self,msg:int,private_key:tuple=None)->str:

		if private_key==None:
			private_key = self.private_key

		d,n = private_key

		msg_np = msg

		decrypted_text_np = np.mod(np.power(msg_np,d),n)
		# print("DT",decrypted_text_np)

		decrypted_text = self.toString(decrypted_text_np)

		return decrypted_text


