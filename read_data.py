import sys

with open(sys.argv[1]) as f:
	sents = []
	tagged = []
	pos = []
	count = -1
	sent = []
	tags = []
	for line in f.readlines():
		if(line[0] == '\n'):
			sents.append(sent)
			tagged.append(tags)
			tags = []
			sent = []
		if(line[0] == '#'):
			continue
		else:
			toks = line.split('\t')
			sent.append(toks[2])
			tags.append(toks[3])
