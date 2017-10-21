

import random 

def generateTestCase(case, width, height):
    #### writing the output to the output file 
    output_file  = open(case, 'w')
    
    header = []
    for col in range(0, width):
        header.append(col)

    output_array = [header]
    for row in range(0, height):
    	r = []
    	for col in range(0, width):
    		r.append(random.randint(1, 10 * height))
    
        output_array.append(r)

    print output_array


    #### writing the rows in the output array to the output file
    for row in output_array:
    	line =  '\t'.join([str(i) for i in row])    	
    	output_file.write(line+'\n')
    

for i in range(0, 10):
    generateTestCase('case%s.txt' %(i), random.randint(5, 25), random.randint(1000, 2000) )