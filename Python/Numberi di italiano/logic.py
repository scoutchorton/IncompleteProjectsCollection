from itnum import numbers
class Logic(object):
    def __init__(self, number):
        self.nu = number
        self.word = ""

    #One's place calculations
    def ones(self, n):
        return numbers.nums[n]

    #Ten's place calculations
    def tens(self, n):
        #If the number is in the teens or ten (special values for that)
        if n < 20:
            return numbers.nums[n]

        #If the number is 20 and more
        else:
            #Letter drop rule for 1 and 8
            if (int(str(n)[1]) == 1) or (int(str(n)[1]) == 8):
                return numbers.nums[int(str(n)[0])*10][:-1] + self.ones(int(str(n)[1]))
            #Doesn't align with the other rules
            else:
                return numbers.nums[int(str(n)[0])*10] + self.ones(int(str(n)[1]))


    #Hundred's place calculations
    def hunds(self,n):
        #If it is 100, answer is cento
        if int(str(n)[0]) == 1:
            return numbers.nums[100] + self.tens(int(str(n)[1:]))
        #Single number + cento + tens value
        else:
            return numbers.nums[int(str(n)[0])] + numbers.nums[100] + self.tens(int(str(n)[1:]))

    def run(self):
        #Ones place
        if len(str(self.nu)) == 1:
            self.word = self.word + self.ones(self.nu)

        #Tens place
        elif len(str(self.nu)) == 2:
            self.word = self.word + self.tens(self.nu)

        #Hundreds place
        elif len(str(self.nu)) == 3:
            self.word = self.word + self.hunds(self.nu)

        #Final return
        return self.word
