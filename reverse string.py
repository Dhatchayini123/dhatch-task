str='Hello I am computer'
res=' '.join(word[::-1] for word in str.split())
print(res)