# borrowed some code from official documentation
# just a prime number finder program to learn the basics of python

def prime_num(num, print_nonprimes):
	num += 1
	result = ''
	for n in range(2,num):
		for x in range(2,n):
			if n%x == 0:
				if print_nonprimes:
					result += (str(n) + ' equals ' + str(x) + ' * ' + str(n//x) + '\n')
				break
		else:
			result += (str(n) + ' is prime!\n')
	return result

nonprime = False

user_in = raw_input('do you want to see nonprimes in your search? ')
if user_in in ('y', 'Y', 'yes', 'Yes', 'YES', 'sure'):
	nonprime = True

user_input = int(input('what number do you want to search up to? '))
print(prime_num(user_input, nonprime))