class Question1_Solver:
    def __init__(self, cpt):
        self.cpt = cpt;
        return;

    #####################################
    # ADD YOUR CODE HERE
    # Pr(x|y) = self.cpt.conditional_prob(x, y);
    # A word begins with "`" and ends with "`".
    # For example, the probability of word "ab":
    # Pr("ab") = \
    #    self.cpt.conditional_prob("a", "`") * \
    #    self.cpt.conditional_prob("b", "a") * \
    #    self.cpt.conditional_prob("`", "b");
    # query example:
    #    query: "ques_ion";
    #    return "t";
    def solve(self, query):
	# All possible alphabets in English
	alph='abcdefghijklmnopqrstuvwxyz'
	missing_index = query.index('_')

	# Get all possible combinations
	possible_words = ['`'+query.replace('_',c,1)+'`' for c in alph]
	
	pr_list = []
	for st in possible_words:
		pr = 1
		len_st = len(st)-1
		i = 0
		for c in st:
			if i < len_st:
					pr = pr*self.cpt.conditional_prob(st[i+1], c)
					if(pr == 0):
						break
					i = i + 1
		pr_list.append(pr)

	# Get the maximum prbability 
	pr = max(pr_list)

	# Find the word with maximum probability
	ind = pr_list.index(pr)
	final_string = possible_words[ind]

	#print query," ",final_string," ",final_string[missing_index+1]

	# Return the missing letter	
        return final_string[missing_index+1];


