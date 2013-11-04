codes={}

#dictionary of words with frequency
def frequency(string):
	freq={}
	for word in string:
		freq[word]=freq.get(word,0)+1
	return freq

#print frequency("aaabccdeeeeeffg")   
#{'a': 3, 'c': 2, 'b': 1, 'e': 5, 'd': 1, 'g': 1, 'f': 2}


#sort the words in the order of ranking and stored in tuples
def sortFreq(freq):
	words=freq.keys()
	tuples=[]
	for wd in words:
		tuples.append((freq[wd],wd))
	tuples.sort()
	return tuples
	 
#print sortFreq(frequency("aaabccdeeeeeffg")) 
#[(1, 'b'), (1, 'd'), (1, 'g'), (2, 'c'), (2, 'f'), (3, 'a'), (5, 'e')]


#make a tree
def buildTree(tuples) :
	while len(tuples) > 1 :
		leastTwo = tuple(tuples[0:2])
		#print leastTwo
		theRest = tuples[2:]
		#print theRest
		combFreq = leastTwo[0][0] + leastTwo[1][0]
		#print combFreq
		tuples= theRest + [(combFreq,leastTwo)]
		#print tuples
		tuples.sort()
		#print len(tuples)
	return tuples[0]
#print buildTree(sortFreq(frequency("aaabccdeeeeeffg")))
#(15, ((6, ((3, 'a'), (3, ((1, 'g'), (2, 'c'))))), (9, ((4, ((2, 'f'), (2, ((1, 'b'), (1, 'd'))))), (5, 'e')))))


#trim left,right and combine
def trimTree(tree):
	p=tree[1]
	#print 'p',p
	if type(p)==type(''): 
		return p
	else:
		#print 'p[01]',p[0],p[1]
		return (trimTree(p[0]),trimTree(p[1]))

#print trimTree(buildTree(sortFreq(frequency("aaabccdeeeeeffg")))) 
#(('a', ('g', 'c')), (('f', ('b', 'd')), 'e'))


#assigning codes to all nodes
def assignCodes(nodes, pat=''):
	global codes
	#print nodes,pat
	if type(nodes)==type(''):
		codes[nodes]=pat
	else:
		assignCodes(nodes[0], pat+'0')
		assignCodes(nodes[1], pat+'1')
tree=trimTree(buildTree(sortFreq(frequency("aaabccdeeeeeffg"))))
assignCodes(tree)
print codes 
#{'a': '00', 'c': '011', 'b': '1010', 'e': '11', 'd': '1011', 'g': '010', 'f': '100'}



#original string encoded with the data
def encode( string):
	global codes
	output=''
	for ch in string:
		output+=codes[ch]
	return output
print encode("aaabccdeeeeeffg")
#000000101001101110111111111111100100010


#decode the data and create tree
def decode(tree, s):
	output=''
	p=tree
	for b in s:
		if b=='0':
			p=p[0]
		else:
			p=p[1]
		#print b,p
		if type(p)==type(''):
			output+=p
			p=tree
	return output
print decode(tree,'000000101001101110111111111111100100010')	
