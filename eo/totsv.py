#!/usr/bin/env python

def transform(source,target):
    with open(source,"rUt") as fi:
        with open(target,"wt") as fo:
            try:
                while True:
                    word = next(fi).strip()
                    defn = next(fi).strip()
                    fo.write("{}\t{}\n".format(word,defn))
            except StopIteration:
                pass



if __name__=="__main__":
    import sys
    transform(*sys.argv[1:])


           
     	
