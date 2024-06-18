'''input:hello programmers how are you'''
'''output:count how many spaces'''
sentence="Hello World how r u"
space_count=0
for character in sentence:
    if character==' ':
        space_count+=1
print("number of spaces:",space_count)