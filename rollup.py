#!/usr/bin/python

import sys, getopt


#### this function takes a table and a row as an input and finds the matching row in the table 
   #  and sums most right values of row and matching row in the table and stores them back in the table.
def aggregateRowWithOutput(output, row):
    #find the output row width
    row_width = len(row)

    #find a simular set to accumilate with
    for x in range(0, len(output)):
        if row[:row_width-1] == output[x][:row_width-1]:
            output[x][row_width-1] += row[row_width-1]
            return output

    #if not found then add it, because it is a new set
    output.append(row)

    return output         

#### this function finds the possible sets of columns to aggregate by.
def generateColumnSets(columns):
    sets = []
    for i in range(len(columns), 0, -1): 
        sets.append(columns[:i])

    sets.append([])
    return sets
    
#### this function loops through all the table rows with all the possible sets of columns and apply the aggregation to the output     
def rollupTable(table, columns):
    output = []
    table_width = len(table[0])
    
    # generate the sets to be used for rolling up     
    sets = generateColumnSets(columns)
    

    for colset in sets: 
        print colset

        for row in table:
        	# unify the size of the rows to be aggregated 
            agg_row = [''] * (len(columns)+1)

            # set the aggregation fields 
            for x in colset:
                agg_row[colset.index(x)] = row[x]

            # set the value of the row
            print agg_row, row
            agg_row[len(agg_row)-1] =  row[table_width-1]
            
            # aggregate the row with the output 
            output = aggregateRowWithOutput(output, agg_row)

    return output
    



def main(argv):
	#### initialize the variables and read the user input 
    inputfile = ''
    outputfile = 'rollupoutputfile.txt'
    columns = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:c",[ "ifile=" , "ofile=" , "cols=" ])
    except getopt.GetoptError:
        print 'rollup.py -i <inputfile> -o <outputfile> -c <comma separated column names>'
        sys.exit(2)

    print opts   
    for opt, arg in opts:
        if opt == '-h':
            print 'rollup.py -i <inputfile> -o <outputfile> -c <comma separated column names>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-c", "--cols"):
            columns = arg         

    print "Input file is: ", inputfile
    print "Output file is:", outputfile   
    print "Columns:", columns.split(',')

    
    #### read the content of the input file and find the headers of the table
    with open(inputfile) as f:
        file_content = f.readlines()

    input_table = []
    headers = file_content[0].replace('\n','').split('\t')
    file_content.pop(0)

    for line in file_content:
        input_line = line.replace('\n','').split('\t')
        #print input_line, input_line[len(input_line)-1]
        input_line[len(input_line)-1] = int(input_line[len(input_line)-1])
        input_table.append(input_line)
        
   
    #### find the input column
    input_columns = []
    try:
        for col in columns.split(','):
            input_columns.append(headers.index(col))
    except:
        input_columns = []        

 
    #### run the rollup aggregation function on the input table and the input columns
    output = rollupTable(input_table, input_columns)


    #### writing the output to the output file 
    output_file  = open(outputfile, 'w')
    

    #### Preparing the table headers for the output file 
    output_headers_arr = columns.split(',')
    output_headers_arr.append(headers[len(headers)-1])
    output_header_line = '\t'.join(output_headers_arr) + '\n'
    output_file.write(output_header_line)

    #### writing the rows in the output array to the output file
    for row in output:
    	line =  '\t'.join([str(i) for i in row])    	
    	output_file.write(line+'\n')
    


if __name__ == "__main__":
    main(sys.argv[1:])











