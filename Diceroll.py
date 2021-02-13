#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import json

# import our Random class from python/Random.py file
sys.path.append(".")
#from python.Random import Random
from Random import Random


# main function for our coin toss Python code
result = open("diceroll_result.txt","w")

if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 5555

    prob = 1/6

    # default number of Dice rolls (per experiment)
    Ntoss = 10

    # default number of experiments
    Nexp = 100

    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-prob' in sys.argv:
        p = sys.argv.index('-prob')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            prob = ptemp
    if '-Ntoss' in sys.argv:
        p = sys.argv.index('-Ntoss')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Ntoss = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    

    # class instance of our Random class using seed

    random = Random(seed)

    
    
    for e in range(0,Nexp):
            result_array=[]
            for t in range(0,Ntoss):
                #print(random.Bernoulli(prob), end=' ')
                result.write(str(random.Diceroll(prob))+"\n")
                



    result.close()
       
   
