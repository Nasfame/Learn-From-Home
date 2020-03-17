class Mine():

	stacks =[]
	mentor = []
	learner = []
	dict={}
	time={}
		


def addStacks(self,input):
    Mine.stacks.append(input)
    return
def setMentorOrLearner(self,input):
    if input in Mine.mentor:
        Mine.dict.update({input:"Mentor"})
    else:
        Mine.dict.update({input:"Learner"})
    return
def setAvailableTime(self,input,time):
    if input in Mine.mentor:
        Mine.dict.update({input:time})
    return
def getMentor(self,stacks,times):
    stack = Mine.stacks
    time=Mine.time.items
    available =[]
    for i in time:
        if i[1]<times:
            available.append(i[0])
    return available
    
    