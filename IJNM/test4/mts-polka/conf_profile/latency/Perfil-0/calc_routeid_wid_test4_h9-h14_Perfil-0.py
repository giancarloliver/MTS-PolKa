#!/usr/bin/env python3
from polka.tools import calculate_routeid, print_poly
DEBUG = False


def _main():
    print("Insering irred poly (node-ID)")
    s = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],  # s1_0
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],  # s2_0
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],  # s2_1
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],  # s2_2      
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],  # s2_3
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1],  # s2_4
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],  # s1_1
        #[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1],  # s8
        #[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1],  # s9
        #[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],  # s1_00
    ]
    print("From h7 to h12 ====")
    # defining the nodes from h7 to h6
    nodes = [
    s[0],
    #s[1],
    #s[2],
    s[3],
	#s[4],
	# s[5],
	s[6],	
    ]
    # defining the transmission state for each node from h7 to h12
    o = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],     # s1_0   
	#[1, 0],  # s2_0
    #[1, 0],  # s2_1
    [1, 0],  # s2_2
	#[1, 0],	# s2_3	
	# [1, 0],	#s2_4
	[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # s1_1
    ]
    print("routeid h7 to h12 ====")
    print_poly(calculate_routeid(nodes, o, debug=DEBUG))
    print("From h7 to h12 ====")
    # defining the nodes from h7 to h6
    nodes = [
    s[0],
    #s[1],
    #s[2],
    s[3],
	#s[4],
	# s[5],
	s[6],	
    ]
    # defining the transmission weight for each node from h7 to h12
    w = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # s1_0   
	#[0, 0],  # s2_0
    #[0, 0],  # s2_1
    [0, 0],  # s2_2
	#[0, 0],	# s2_3	
	# [0, 0],	#s2_4
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # s1_1
    ]
    print("wid h7 to h12 ====")
    print_poly(calculate_routeid(nodes, w, debug=DEBUG))

    print("From h7 to h12 ====")
    # defining the nodes from h12 to h7
    nodes = [
    s[6],
    #s[5],
    #s[4],
    s[3],
	#s[2],
	#s[1],
	s[0],
    ]
    # defining the transmission state for each node from h12 to h7
    o = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],     # s1_1
	# [0, 1],  # s2_4
    #[0, 1],  # s2_3
	[1, 0],	# s2_2	
	#[1, 0], # s2_1
	#[0, 1], # s2_0        
	[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # s1_0
    ]
    print("routeid h12 to h7 ====")
    print_poly(calculate_routeid(nodes, o, debug=DEBUG))

    print("From h7 to h12 ====")
    # defining the nodes from h7 to h12
    nodes = [
    s[6],
    #s[5],
    #s[4],
    s[3],
	#s[2],
	#s[1],
	s[0],
    ]
     # defining the transmission weight for each node from h12 to h7
    w = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # s1_1
	# [0, 0],  # s2_4
    # [0, 0],  # s2_3
	[0, 0],	# s2_2	
	#[0, 0], # s2_1
	#[0, 0], # s2_0        
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # s1_0
    ]    
    print("wid h12 to h7 ====")
    print_poly(calculate_routeid(nodes, w, debug=DEBUG)) 


if __name__ == '__main__':
    _main()
