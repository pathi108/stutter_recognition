def countAllSyllables(syllables):
    sum=0
    stttutered=0
    now=0
    last=0
    for syllable in syllables:
        now=len(syllable)
        sum=sum+now
        if now==1 and last ==1:
            stttutered=stttutered+1
        last=now
    return(sum,stttutered)


