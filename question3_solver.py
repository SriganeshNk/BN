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
		print preword
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
		max_prob = []
		index = []
		for x in range(1,27):
			max_cpt = max(self.cpt.cpt[x])
			if self.cpt.cpt[x].index(max_cpt) == 0:
				max_cpt = max(self.cpt.cpt[x][1:])
				max_prob.append(max_cpt)
				index.append(self.cpt.cpt[x].index(max_cpt)-1)
			else:
				max_prob.append(max_cpt)
				index.append(self.cpt.cpt[x].index(max_cpt)-1)
		nextchar = ''
		l = len(dashword)
		precompute = preword
		print dashword
		for x in range(1,l):
			print x-1, dashword[x-1], x, dashword[x]
			if dashword[x-1] == '-' and x-1 == 0:
				if first == '`':
					pr = pr * max(self.cpt.cpt[0])
					nextchar = alpha[self.cpt.cpt[0].index(max(self.cpt.cpt[0]))-1]
					precompute += nextchar
				else:
					pr = pr * max_prob[ord(first)-97]
					nextchar = alpha[index[ord(first)-97]]
					precompute += nextchar
			if dashword[x] == '-' and dashword[x-1] == '-' and len(nextchar) > 0:
				pr = pr * max_prob[ord(nextchar)-97]
				nextchar = alpha[index[ord(nextchar)-97]]
				precompute += nextchar
			else:
				nextchar = ''
		if len(nextchar) == 0:
			nextchar = precompute[len(precompute)-1]
		for x in range(len(alpha)):
			temp = pr * self.cpt.conditional_prob(alpha[x], nextchar)
			
		return 'e'

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
