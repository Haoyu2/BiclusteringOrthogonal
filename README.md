The program should perform regular clustering on the rows and columns
seperately, then use both clustering results to generate a bicluster.

Step 1: Given a matrix A, generate a distance matrix R between the rows
		(we will start with a binary matrix and using hamming distance).
		
Step 2: Perform regular clustering (k-means, or some other method) on R to
		get a set of rows with high values.  Save these results for later use.
		
Step 3: From the original matrix A, generate a distance matrix C between
		columns.
		
Step 4:  Perform clustering on C to get a set of columns with high values.

Step 5: Take the rows from step 2 and columns from step 4 to get a set of
		entries of A that should be grouped in a bicluster.
		


Example: A is a 5x5 matrix, step 2 yields a cluster {1,3,4} and step 4
		 yields a cluster {2,5}, then the final bicluster would consist of
		 the following entries of A: {(1,2); (1,5); (3,2); (3,5); (4,2); (4,5)} 
