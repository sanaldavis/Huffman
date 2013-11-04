string="malayalam";


//find the frequency of the characters in string
function frequency(string)
{
	freq={};
	for(count=0; count<string.length; count++)
	{
		if (string[count] in freq)
			freq[string[count]]+=1;
		else
			freq[string[count]]=1;
	}
	return freq;
}
freqs=frequency(string);
//freqs=frequency("aaabccdeeeeeffg");
//{'a': 3, 'c': 2, 'b': 1, 'e': 5, 'd': 1, 'g': 1, 'f': 2}



// frequency sorted and stored order of rank
function sortFreq(freqs)
{
	tuples=[];
	for(var key in freqs)
		//console.log(freqs[key],key);
		tuples.push([freqs[key],key]);	
	return tuples.sort();
}
tuples=sortFreq(freqs);
//[[1, 'b'], [1, 'd'], [1, 'g'], [2, 'c'], [2, 'f'], [3, 'a'], [5, 'e']] 



//build tree
function buildTree(tuples)
{
	while(tuples.length>1)
	{
	leastTwo=[tuples[0][1],tuples[1][1]]
	//console.log(leastTwo);
	theRest=tuples.slice(2,tuples.length);
	//console.log(theRest);
	combFreq=tuples[0][0]+tuples[1][0];
	//console.log(combFreq);
	tuples=theRest;
	end=[combFreq,leastTwo];
	tuples.push(end);
	//console.log(tuples);
	tuples.sort();
	//console.log(tuples);
	}
	return tuples[0][1];
}
tree=buildTree(tuples);	
//console.log(tree);
//[ 'a', [ 'm', [ 'y', 'l' ] ] ]


code={};
pat='';
//assiging codes to each letter
function assignCode(node,pat)
{
	if(typeof(node)==typeof(""))
		code[node]=pat;
	else
	{
		assignCode( node[0], pat+'0');
		assignCode( node[1], pat+'1');
	}
}
assignCode(tree,pat);
//console.log(code);
//{ a: '0', m: '10', y: '110', l: '111' }


//encoding given string
function encode(string)
{
	output='';
	for(s in string)
		output+=code[string[s]];
	return output;
}

encoded=encode(string);
console.log("Encoded as:",encoded);
//10011101100111010



//decoding that string
function decode(tree,encoded)
{
	output='';
	p=tree;
	for(bit in encoded)
	{
		if(encoded[bit]=='0')
			p=p[0];
		else
			p=p[1];
		if(typeof(p)==typeof(''))
		{
		output+=p;
		p=tree;
		}
	}
	return output;
}
decoded=decode(tree,encoded);
console.log("Decoded as:",decoded);
//malayalam
