import numpy as np

transition=np.matrix([[0,0,0,0,.5,0,.5,0,0,0],
	[0,0,0,0,0,0,.5,0,.5,0],
	[0,0,0,0,0,0,0,.5,0,.5],
	[0,0,0,0,.5,0,0,0,.5,0],
	[.333,0,0,.333,0,0,0,0,0,.333],
	[0,0,0,0,0,0,0,0,0,0],
	[.333,.333,0,0,0,0,0,.333,0,0],
	[0,0,.5,0,0,0,.5,0,0,0],
	[0,.5,0,.5,0,0,0,0,0,0],
	[0,0,.5,0,.5,0,0,0,0,0]])

values = [0,1,2,3,4,5,6,7,8,9]
state = np.matrix([[1,0,0,0,0,0,0,0,0,0]])

one= np.matmul(state,transition)
x= np.matmul(one,transition)
print np.matmul(x,values)

def expected_sum(time):
	# set initial state
	state = np.matrix([[1,0,0,0,0,0,0,0,0,0]])
	# this holds expected value of values for each state distribution 
	tobe_summed=[]
	# move forward through time
	for i in range(time):
		# apply transition matrix to current state
		state=np.matmul(state,transition)
		# multiple values matrix * distribution of probs of current states to find ev of that time
		ev = np.matmul(state,values)
		# append
		tobe_summed.append(ev[0,0])
	s= sum(tobe_summed)
	return s 

# print mod 10, as stated in problem
print expected_sum(200)%10