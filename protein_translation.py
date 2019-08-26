def proteins(strand):
    import re
    codonlist=re.findall(".{3}" ,strand)
    codondict={'AUG':'Methionine','UUU':'Phenylalanine','UUC':'Phenylalanine','UUA':'Leucine','UUG':'Leucine','UCU':'Serine','UCC':'Serine','UCA':'Serine','UCG':'Serine','UAU':'Tyrosine','UAC':'Tyrosine','UGU':'Cysteine','UGC':'Cysteine','UGG':'Tryptophan','UAA':'STOP','UAG':'STOP','UGA':'STOP'}
    proteinlist=[]
    for codon in codonlist:
        if codon=='UAA' or codon=='UAG' or codon=='UGA':
            break
        else:
            proteinlist.append(codondict[codon])
    return proteinlist

