'''
#EQUIVALENCE PARTITIONING
- Valid input range from 1 to 100)
- (Any invalid input where x is less than 1)
- (Any invalid input where x is greater than 100)

# BOUNDARY VALUE ANALYSIS
- Minimum value
- Just above minimum value
- Maximum value
- Just below maximum value
- Nominal (Average) value

#ROBUSTNESS TESTING

- Minimum value
- Just above minimum value
- Just below minimum value
-  Just above maximum value
- Just below maximum value
- Maximum value
- Nominal (Average) value

def check_pwd(pwd):
  if len(pwd)< 6 or len(pwd)>12 :
    return "Invalid"
  else:
    return "Valid"

#1.
tc_equals_6={"input":"abcdef","expected":"Valid"}
tc_equals_12={"input":"abcdefabcdef","expected":"Valid"}
tc_1_below_1={"input":"abcde","expected":"Invalid"}
tc_1_below_2={"input":"abcdefabcde","expected":"Valid"}
tc_1_above_1={"input":"abcdefa","expected":"Valid"}
tc_1_above_2={"input":"abcdefabcdefg","expected":"Invalid"}

test_cases=[tc_equals_6,tc_equals_12,tc_1_below_1,tc_1_below_2,tc_1_above_1,tc_1_above_2]

table=[]
for i in test_cases:
  
  row=[]
  input=i["input"]
  actual=check_pwd(i["input"])
  expected=i["expected"]
  if actual==expected:
    res="Pass"
  else:
    res="Fail"
  row.append(input)
  row.append(len(i["input"]))
  row.append(actual)
  row.append(expected)
  row.append(res)
  table.append(row)

import pandas as pd
df=pd.DataFrame(table,columns=["input","length","actual","observed","status"])
print(df)

#2.

def check_disc(bill_amt):
  if bill_amt<=50:
    return 0.00
  elif bill_amt>50 and bill_amt<=200:
    return 0.05
  elif bill_amt>=201 and bill_amt<=500:
    return 0.10
  elif bill_amt>=501:
    return 0.15

tc_eq_1={"input":1,"discount":0.00}
tc_eq_50={"input":50,"discount":0.00}
tc_eq_0={"input":0,"discount":0.00}
tc_eq_49={"input":49,"discount":0.00}
tc_eq_2={"input":2,"discount":0.00}
tc_eq_51={"input":51,"discount":0.05}

tc_eq_200={"input":200,"discount":0.05}
tc_eq_201={"input":201,"discount":0.10}
tc_eq_198={"input":198,"discount":0.05}
tc_eq_500={"input":500,"discount":0.10}
tc_eq_499={"input":499,"discount":0.10}

tc_eq_501={"input":501,"discount":0.15}
tc_eq_502={"input":502,"discount":0.15}

test_cases=[tc_eq_1,tc_eq_50,tc_eq_0,tc_eq_49,tc_eq_2,tc_eq_51,tc_eq_200,tc_eq_201,tc_eq_198,tc_eq_500,tc_eq_499,tc_eq_501,tc_eq_502]

table=[]
for tc in test_cases:
  row=[]
  row.append(tc["input"])
  row.append(tc["discount"])
  row.append(check_disc(tc["input"]))
  if tc["discount"]==check_disc(tc["input"]):
    row.append('pass')
  else:
    row.append('false')
  
  table.append(row)

import pandas as pd
df=pd.DataFrame(table,columns=["input","expected discount","actual discount","status"])
print(df)
                                

#3.

def calc_grade(m1, m2, m3):
  avg = (m1+m2+m3)/3
  # print("Average : ", avg)
  if (90<=avg<=100):
    return "First class Distinction"
  elif (75<=avg<=89):
    return "First Class"
  elif (60<=avg<=74):
    return "Second Class"
  elif (50<=avg<=59):
    return "Third Class"
  elif (0<=avg<50):
    return "Fail"
  else:
    return "Invalid Input"

test_cases = [
    (89,90, 91, "First class Distinction"),
    (93,94,95, "First class Distinction"),
    (99,100,101, "Invalid Input"),

    (74,75,76, "First Class"),
    (81,82,83, "First Class"),
    (88,89,90, "First Class"),

    (59,60,61, "Second Class"),
    (66,67,68, "Second Class"),
    (73,74,75, "Second Class"),

    (49,50,51, "Third Class"),
    (53.5,54.5,55.5,"Third Class"),
    (58,59,60, "Third Class"),

    (48,49,50, "Fail"),
    (0,1,2, "Fail"),
    (101,102,103, "Invalid Input"),
    (100,99,101, "Invalid Input"),

]
res = []
for mark1, mark2, mark3, expected_grade in test_cases:
  row = []
  grade = calc_grade(mark1, mark2, mark3)
  row.append(mark1)
  row.append(mark2)
  row.append(mark3)
  row.append(expected_grade)
  row.append(grade)
  if grade == expected_grade:
    row.append('Pass')
  else:
    row.append('Fail')
  res.append(row)
res


#4.
#4
def valid_pizza_order(num):
  if (1<=num<=10):
    return "Valid"
  elif (num>10):
    return "Invalid"

test_cases = [
    [1, "Valid"],
    [2, "Valid"],
    [5, "Valid"],
    [10, "Valid"],
    [11, "Invalid"],
    [100, "Invalid"],

]
res = []
for num_pizzas, expected in test_cases:
  row = []
  result = valid_pizza_order(num_pizzas)
  row.append(num_pizzas)
  row.append(expected)
  row.append(result)
  if result == expected:
    row.append('Pass')
  else:
    row.append('Fail')
  res.append(row)
  
#5. 
#5
def calc_tax(salary):
  if not(12000 <= salary <= 35000):
    print(salary, " - Inavlid salary range")
  else:
    if (salary <= 15000):
      return 0
    elif (15001 <= salary <= 25000):
      return 18
    elif (25001 <= salary):
      return 20

test_cases = [
    [12000, 0],
    [12000, 0],
    [15000, 0],
    [15001, 18],
    [25000, 18],
    [25001, 20],
    [35000, 20],
    [35001, 20]]
ls_salary = [12000, 12001, 15000, 15001, 15002, 25000, 25001, 35000, 35001]
res = []
for salary,expected_tax in test_cases:
  row = []
  result = calc_tax(salary)
  row.append(salary)
  row.append(expected_tax)
  row.append(result)
  if result == expected_tax:
    row.append('Pass')
  else:
    row.append('Fail')
  res.append(row)
res
'''