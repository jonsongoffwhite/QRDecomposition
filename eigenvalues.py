import random, copy, numpy as np
import sys

#Number of iterations used for the algorithm
#The larger the number, the more accurate the
#Eigen values will be
ITERATIONS = 100

#Generates a random symmetrical matrix
#of dimensions dim x dim, with values
#between -1000 and 1000
def generate_symmetrical_matrix(dim):
	output = np.zeros((dim,dim))
	for i in range(0, dim):
		for j in range(0, i+1):
			x = random.random()*1000*random.choice([-1,1])
			output[i,j] = x
			if (not i == j):
				output[j,i] = x
	if (np.linalg.det(output) != 0):
		return output
	else:
		return generate_symmetrical_matrix(dim)

#Returns a random matrix size between 1 - 10 inclusive
def random_size ():
	return random.randint (1, 10)

#Performs the qr decomposition of a symmetrical matrix u
#Returns a tuple of the decomposed constituents q and r
def qr(u):
	m = len(u[0])
	q = np.zeros((m, m))
	r = np.zeros((m, m))

	for i in range (m):
		q[:,i] = copy.copy(u[:,i])
		for j in range (i):
			r[j,i] = np.dot(q[:,j], q[:,i])
			q[:,i] = q[:,i] - (r[j,i] * q[:,j])

		r[i,i] = np.linalg.norm(q[:,i])
		q[:,i] = q[:,i]/r[i,i]
	return (q, r)

#Calculates eigenvalues and eigenvectors using the
#qr decomposition iteratively on the original matrix
def calculate_eigenvalues_and_vectors ():
	#print(matrix)
	e_v_in_matrix = eigenvalues_and_vectors_in_matrix(matrix, ITERATIONS)
	e = eigenvalues (e_v_in_matrix[0])
	v = e_v_in_matrix[1]
	return (e,v)

#Returns a tuple consisting of the eigen values as a matrix,
#and a matrix consisting of the eigenvectors for these values
def eigenvalues_and_vectors_in_matrix (u, m):

	h = np.identity(len(u))
	for i in range (m):
		q, r = qr(u)
		h = h.dot(q)
		u = np.dot(r, q)

	return (u,h)

#Returns a list of eigenvalues extracted from the matrix form
#of the eigenvalues
def eigenvalues (m):
	out = np.zeros (len(m))
	for i in range(len(m)):
		out[i] = m[i,i]
	return out

#Writes the matrix, the eigenvalues and the corresponding
#eigenvectors to a file called 'output'
def write (ans):
	f = open('output', 'w')
	f.write('Matrix: \n\n')
	f.write(str(matrix))
	f.write('\n\n\n')
	f.write('Eigenvalues: \n\n')
	for i in range(len(ans[0])):
		f.write(str(ans[0][i]) + '\n')
	f.write('\n\n')
	f.write('Eigenvectors: \n\n')
	#f.write(str(ans[1]))
	for i in range(len(ans[1])):
		f.write(str(ans[1][:,i]) + '\n')

if (len(sys.argv) > 1):
	matrix = np.loadtxt(sys.argv[1])
else:
	#matrix to be used in calculations
	matrix = generate_symmetrical_matrix (random_size())
assert(np.linalg.det(matrix) != 0), "Determinant is equal to 0, and must not be"
#write the output to the file
write (calculate_eigenvalues_and_vectors())


