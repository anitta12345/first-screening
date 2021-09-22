input=[4,5,3,2]
filter(lambda x: x%4==0, input)
list(filter(lambda x: x%4==0, input))
len(list(filter(lambda x: x%4==0, input)))
output={i:len(list(filter(lambda x: x%i==0, input))) for i in input}
print(output)
