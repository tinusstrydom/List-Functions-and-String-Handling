# List, Functions and StringHandling 2
# Tinus Strydom
# Program translate dna amino acids to protein (mutate)

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
    slc ={ 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
    } 
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
                protein += slc[codon]+" "
        return "Protein: "+protein

'''
define Mutate function
open the DNA text file to read from the sequence of dna
open the normalDNA text file to write to
for loop through each line in text file
used the replace function to check for "a" replace with the "A"
then write to the normFile the sequence with the a change to A
then close files
Used same way for the mutatedDNA text file ,only difference is changing "a" to "T"   
'''
def mutate():
    DNAfile = open("DNA.txt", "r", encoding="utf-8")
    normFile = open("normalDNA.txt", "w", encoding="utf-8")
    repA = DNAfile.read().replace("a","A")
    normFile.write(repA)
    DNAfile.close()
    normFile.close()
    
    DNAfile = open("DNA.txt", "r", encoding="utf-8")
    mutFile = open("mutatedDNA.txt", "w", encoding="utf-8")
    repT = DNAfile.read().replace("a","T")
    mutFile.write(repT)
    DNAfile.close()
    mutFile.close()

'''
define function txtTranslate
Open files mutatedDNA and normalDNA text files
assign to dna variable the value of mutFile, used the read method to
read everything from file, replaced the \n(newline) and \r(carriage return)
with empty string for the sequence from the fill to be one long string
then assigned the value from calling the translate function with the dna string
as argument
did the same for normalDNA
then closed the files
return to the user the output of x and y
***will notice that 24 protein will be different due to A and T changes from the
***mutated function (W, R)
***had to get all the proteins ,and the _ ones in the sequence is for stop codons
'''
def txtTranslate():
    mutFile = open("mutatedDNA.txt", "r", encoding="utf-8")
    normFile = open("normalDNA.txt", "r", encoding="utf-8")

    dna = mutFile.read().replace("\n", "").replace("\r", "")
    x = translate(dna)
    
    dna = normFile.read().replace("\n", "").replace("\r", "")
    y = translate(dna)
    
    mutFile.close()
    normFile.close()
    
    return "Sequence for mutatedDNA file is : "+x+"\n"+"Sequence for normalDNA file is : "+y+"\n"

'''
call functions
mutate to write string to the required files
then return to the user the output from txtTranslate function
'''
mutate()   
print(txtTranslate())
     
    




    























