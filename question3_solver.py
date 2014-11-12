import re

class Question3_Solver:
	def __init__(self, cpt):
		self.cpt = cpt;
	#####################################
	# ADD YOUR CODE HERE
	# Pr(x|y) = self.cpt.conditional_prob(x, y);
	# A word begins with "`" and ends with "`".
	# For example, the probability of word "ab":
	# Pr("ab") = \
	#    self.cpt.conditional_prob("a", "`") * \
	#    self.cpt.conditional_prob("b", "a") * \
	#    self.cpt.conditional_prob("`", "b");
	# 	query example:
	#  	  query: "qu--_--n";
	#    return "t";
	def solve(self, query):
		list_of_words = query.split('_')
		m = re.search('[-_]', query)
		dashword = query[m.start():]
		if re.search('[a-z]', dashword):
			n = re.search('[a-z]', dashword)
			dashword = dashword[0:n.start()]
		else:
			dashword = dashword[0:len(dashword)]
		preword = '`' + list_of_words[0]
		remword = list_of_words[1] + '`'
		l = len(preword)
		first = preword[len(preword)-1]
		last = remword[0]
		pr = 1
		if l > 1:
			for x in range(1, l):
				if preword[x] != '-':
					pr = pr * self.cpt.conditional_prob(preword[x], preword[x-1])
				else:
					first = preword[x-1]
					break
		tempword = preword.split('-')
		preword = tempword[0].split('_')[0]
		l = len(remword)
		if l > 1:
			for x in range(1, l):
				if remword[x-1] != '-':
					if last == '-':
						last = remword[x-1]
					pr = pr * self.cpt.conditional_prob(remword[x], remword[x-1])
				elif last == '-':
					last = remword[x]
		# Till now you have the start character before the first dash, end character after the last dash ---> first and last
		# Then you have the combination of dashs ---> dashword
		# You also have the probablities of the known character combinations
		# have to calculate the probablities of the hidden by summing up and the _ character
		alpha = 'abcdefghijklmnopqrstuvwxyz'
		best_prob = 0
		best_char = 'a'
		best_pair = ''
		best_new = 'a'
		l = 0
		while l < len(dashword):
			if l+1 == len(dashword):
				best_prob = 0
				for x in range(len(alpha)):
					temp = pr * self.cpt.conditional_prob(alpha[x], first) * self.cpt.conditional_prob(last, alpha[x])
					if temp > best_prob:
						best_prob = temp
						best_char = alpha[x]
				first = best_char
				best_pair += best_char
				pr = best_prob
				l+=1
			else:				
				for x in range(len(alpha)):
					temp = pr * self.cpt.conditional_prob(alpha[x],first)
					for y in range(len(alpha)):
						newtemp = temp * self.cpt.conditional_prob(alpha[y], alpha[x])
						if best_prob < newtemp:
							best_prob = newtemp
							best_char = alpha[x]
							best_new = alpha[y]
				first = best_char
				best_pair += best_new + best_char
				pr = best_prob
				l+=2
		m = re.search('_', dashword)
		print best_pair[m.start()]	
		result = best_pair[m.start()]
		return result

"""l = len(dashword)
precompute, postcompute, internal = [], [], []
if dashword[0] == '-':
precompute = [self.cpt.conditional_prob (x, first) for x in alpha]
if dashword[len(dashword)-1] == '-':
postcompute = [self.cpt.conditional_prob (last, x) for x in alpha]
for x in range(1,l):
if dashword[x-1] == dashword[x]:
internal = [self.cpt.conditional_prob(w, y)for w in alpha for y in alpha]
def calc_SUM(l, given, bp, pr):
if l == 0:
if bp < pr:
bp = pr
pr = calc_SUM(l-1)
for x in alpha:
newtemp += pr * self.cpt.conditional_prob(x, given)
"""
