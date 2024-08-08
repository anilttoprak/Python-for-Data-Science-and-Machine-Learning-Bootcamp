import numpy as np

# EXERCİSES

#### Create an array of 10 zeros 

arr=np.zeros(10)

#### Create an array of 10 ones

np.ones(10)

#### Create an array of 10 fives

arr=np.linspace(5,5,10)
# OR
np.ones(10) * 5

#### Create an array of the integers from 10 to 50

arr=list(np.arange(10,51))

#### Create an array of all the even integers from 10 to 50

arr=list(np.arange(10,51,2))

#### Create a 3x3 matrix with values ranging from 0 to 8

arr=np.arange(0,9).reshape(3,3)

#### Create a 3x3 identity matrix

arr=np.eye(3)

#### Use NumPy to generate a random number between 0 and 1

arr=np.random.rand(1)

#### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

arr=np.random.randn(25)

#### Create the following matrix:

arr=np.arange(1,101).reshape(10,10) / 100

#### Create an array of 20 linearly spaced points between 0 and 1:

arr=np.linspace(0,1,20)

## Numpy Indexing and Selection

# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

mat = np.arange(1,26).reshape(5,5)

arr=mat[2:,1:]

arr=mat[3,-1]

arr=mat[:3,1:2] # **  

arr=mat[4]

arr=mat[3:]

#### Get the sum of all the values in mat

arr=mat.sum()

#### Get the standard deviation of the values in mat

arr=mat.std()

#### Get the sum of all the columns in mat

arr=mat.sum(axis=0)