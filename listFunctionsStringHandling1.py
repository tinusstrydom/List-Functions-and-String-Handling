# List, Functions and StringHandling 1 
# Tinus Strydom
# Program translate dna amino acids to protein

#request user to input sequence
dna = input("Please enter DNA sequence: ").upper()

'''
define translate function taking the sequence from input that is stored to dna variable
created a dictoinary with all the value pairs of codon and protein related to it
created empty protein variable for string output
if statement checks the lenght of dna string(input) divided by 3 is equal to 0
nothing left over
then the for loops, loops through range starting from 0 up to lenght of dna string
in steps of 3
codon is equal to the dna indice from value of i to i+3
protein is equal to the value of the codon in the slc dictionary 
then return protein value
else part of the loop has same iteration way
if loop inside check if the left over part is either 1 or 2 codons ,that isn't
a sequence to have a protein ,output for them was added to protein and returned
'''
def translate(dna):
    slc = {"ATT" : "I", "ATC" : "I", "ATA" : "I",
       "CTT" : "L", "CTC" : "L", "CTA" : "L", "CTG" : "L", "TTA" : "L",
       "GTT" : "V", "GTC" : "V", "GTA" : "V", "GTG" : "V",
       "TTT" : "F", "TTC" : "F",
       "ATG" : "M"}
    protein = ""
    
    #return len(dna)
    if len(dna) % 3 == 0:
        for i in range(0, len(dna), 3):
            codon = dna[i:i+3]
            protein += slc[codon]
        return "Protein: "+ protein+" "
    else:
        for i in range(0,len(dna),3):
            codon = dna[i:i+3]
            if len(codon) == 1:
                aminoX = "aminoX" #dna[i:i+1]
                protein += "sequence need 2 more codons: "+aminoX
            elif len(codon) == 2:
                aminoX = "aminoX" #dna[i:i+2]
                protein += "sequence need 1 more codon: "+aminoX
            else:
                protein += slc[codon]+", and "
        return "Protein: "+protein

#call function with argument of dna
print(translate(dna))
