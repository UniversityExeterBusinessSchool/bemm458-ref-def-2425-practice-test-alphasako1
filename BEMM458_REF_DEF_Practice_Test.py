

#######################################################################################################################################################
# 
# Name: Alpha John Sako
# SID: 710036549
# Exam Date: 
# Module: BEMM458-Test2
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/bemm458-ref-def-2425-practice-test-alphasako1.git 
#
########################################################################################################################################################
# Instruction 1. Carefully read each question before attempting the solution. Complete all tasks in the script provided.

# Instruction 2. Only ethical and minimal use of AI tools is allowed. This includes help in syntax, documentation look-up, or debugging only.
#                You must not use AI to generate the core logic or full solutions.
#                Clearly indicate where and how AI support was used.

# Instruction 3. Paste the output of each code section directly beneath it as a comment (e.g., # OUTPUT: (34, 90))

# Instruction 4. Add sufficient code comments to demonstrate your understanding of each solution.

# Instruction 5. Save your file, commit it to GitHub, and upload to ELE. GitHub commit must be done before the end of the exam session.

########################################################################################################################################################
# Question 1 - List Comprehension and String Manipulation
# You are analysing customer reviews collected from a post-service survey.
# Your SID will determine the two allocated keywords from the dictionary below. Use the **second** and **second-to-last** digits of your SID.
# For each selected keyword, identify all positions (start and end) where the word occurs in the customer_review string.
# Store each occurrence as a tuple in a list called `location_list`.

customer_review = """Thank you for giving me the opportunity to share my honest opinion. I found the packaging impressive and delivery punctual. 
However, there are several key aspects that require improvement. The installation process was somewhat confusing, and I had to refer to external 
tutorials. That said, the design aesthetics are great, and the customer support team was highly responsive. I would love to see more 
transparency in product specifications and a simpler return process. Overall, a balanced experience with clear potential for enhancement."""

# Dictionary of keywords
feedback_keywords = {
    0: 'honest',
    1: 'impressive',
    2: 'punctual',
    3: 'confusing',
    4: 'tutorials',
    5: 'responsive',
    6: 'transparent',
    7: 'return',
    8: 'enhancement',
    9: 'potential'
}

# Write your code here to populate location_list

#define the words words that im locating in variables target1 and target2

target1 = 'impressive'
target2 = 'tutorials'

#find the first and last position of target one and target 2 using .find and .rfind respectively
start1  = customer_review.find('impressive')
end1 = customer_review.rfind('impressive')

start2 = customer_review.find('tutorials')
end2 = customer_review.rfind('tutorials')


#create tuples for each target word in the form (start, end)

tup1 = (start1, end1)
tup2 = (start2, end2)
location_list = [tup1, tup2]

print(location_list)

########################################################################################################################################################
# Question 2 - Metrics Function for Business Intelligence
# You work in a startup focused on digital health. Your manager wants reusable functions to calculate key performance metrics:
# Gross Profit Margin, Churn Rate, Customer Lifetime Value (CLV), and Cost Per Acquisition (CPA).
# Use the **first** and **last** digits of your student ID as sample numerical values to test your function outputs.

# Insert first digit of SID here:7
# Insert last digit of SID here:9

# Write a function for Gross Profit Margin (%) = (Revenue - COGS) / Revenue * 100

def GPM_calc(Revenue, COGS): #define the function for GPM with args Revenue and cogs
    if Revenue == 0: #check that it is not being divided by 0 if so return none to avoid error 
        return None 
    GPM = (Revenue - COGS)/Revenue*100 #calculate the GPM using the arguments Revenue and COGS.
    return GPM #return GPM



# Write a function for Churn Rate (%) = (Customers Lost / Customers at Start) * 100
def churn_rate_calc(CL, CS): #define function with args customers lost(CL) and customers at start(CS)
    if CL == 0: # check CL is not zero to prevent an error
        return None
    churn_rate = (CL/CS)*100 #calculate the churn_rate
    return churn_rate #return churn rate 


# Write a function for Customer Lifetime Value = Average Purchase Value × Purchase Frequency × Customer Lifespan

def CLV_calc(APV, PF, CLS): #define function for Customer Lifetime Value with args APV, PF, CLS
    CLV = APV * PF * CLS #Calculate CLV 
    return CLV #return CLV 


# Write a function for CPA = Marketing Cost / Number of Acquisitions

def CPA_calc(MC, NoA): #define the funtion for calculating CPA using args Marketing cost and Number of Acquisitions.
    if NoA == 0: # check NoA is not zero 
        return None
    CPA = MC/NoA #calcualte CPA
    return CPA  #return CPA

# Test your functions here

GPM_calc(7, 9)
churn_rate_calc(7, 9)
CLV_calc(7, 9, 7)
CPA_calc(7, 9)



########################################################################################################################################################
# Question 3 - Linear Regression for Pricing Strategy
# A bakery is studying how price affects cupcake demand. Below is a table of past pricing decisions and customer responses.
# Using linear regression:
# 1. Estimate the best price that maximises demand.
# 2. Predict demand if the bakery sets price at £25.

"""
Price (£)    Demand (Units)
---------------------------
8            200
10           180
12           160
14           140
16           125
18           110
20           90
22           75
24           65
26           50
"""


# Write your linear regression solution here
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#create 2d numpy array for price and np array for demand
price = np.array = ([[8], [10],[12], [14], [16], [18], [20], [22], [24], [26]])
demand = np.array = ([200, 180, 160, 140, 125, 110, 90, 75, 65, 50])

#create the model object
model = LinearRegression()

#train the data using the model
model.fit(price, demand)

#set new price
new_price = [[25]]

#predict demand at new price

predicted = model.predict(new_price)

# answer for part .2 print the predicted demand

print(predicted)

#answer for part .1 use a graph to find the best price that maximises demand

plt.scatter(price, demand)
plt.plot(price, model.predict(price))
plt.show()




########################################################################################################################################################
# Question 4 - Debugging and Chart Creation
# The following code is intended to generate 100 random integers between 1 and your SID, and plot them as a scatter plot.
# However, the code contains bugs and lacks contextual annotations. Correct the code and add appropriate comments and output.

#import the relevant modules
import random
import matplotlib.pyplot as plt
import numpy as np 

# Accept student ID as input
sid_input = input("Enter your SID: ")
sid_value = int(sid_input) #converted to integer

# Generate 100 random values
random_values = np.random.randint(1, sid_value + 1, size = 100) #generates a numpy array of random values between 1 and my student id

# Plotting as scatter plot
plt.figure(figsize=(10,5))
plt.scatter(range(100), random_values, color='green', marker='x', label='Random Values')
plt.title("Scatter Plot of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

########################################################################################################################################################
