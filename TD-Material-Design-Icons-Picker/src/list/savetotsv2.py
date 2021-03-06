import json

with open('icons.json') as json_data:
    data = json.load(json_data)

    tsv = 'name\tchr\ttag\n'
    tags = []
    cont = 0
    for element in data: 
        tag = ""
        try:
            tagL = element['tags'][0]
        except IndexError:
            tagL = "(No Tag " + str(int(cont/100)).zfill(2) + ")"
            cont += 1
            tag = tagL 
        
        tags.append(tagL)
        
        for i in range(len(element['tags'])):
            tag = element['tags'][i]+" , "+tag
            tags.append(element['tags'][i])

        newline = element['name']+"\t"+"0x"+element['codepoint']+"\t"+tag+"\n"
        #print(newline) 
        tsv = tsv+newline

print(tsv)
tags = set(tags)
tags = list(tags)
taglist = ""


for Tlist in tags:
    taglist = Tlist+"\n"+taglist

print(taglist)
print(tags)

with open('iconlist2.tsv','w') as outputf:
    outputf.write(tsv)
with open('tags2.tsv','w') as outputf:
    outputf.write(taglist)
with open('tags2.txt','w') as outputf:
    outputf.write(str(tags))