import itertools
def remove_consecutive_duplicates(s1):
     return (''.join(i for i, _ in itertools.groupby(s1)))

s1= input()
print(remove_consecutive_duplicates(s1))