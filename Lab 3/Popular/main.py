import sys
from collections import Counter

inputlist = sys.argv[1].lower()
inputlist = sorted(inputlist)

counterfunc = Counter(list(inputlist))

for top5list, item in enumerate(counterfunc.most_common(5)):
    formatted_str = '{}:{},'.format(item[0],item[1])
    print(formatted_str, end='',)