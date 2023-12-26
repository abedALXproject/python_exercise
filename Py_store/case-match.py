#my_case = ["nandom", "john"]

"""
def my_case(value):
    match value:
        case "nandom":
           # return 1
        #case "john":
       #     return 2
#value = "john"
#my_case(value)
"""
"""
def weekday(n):
   match n:
      case 0: return "Monday"
      case 1: return "Tuesday"
      case 2: return "Wednesday"
      case 3: return "Thursday"
      case 4: return "Friday"
      case 5: return "Saturday"
      case 6: return "Sunday"
      case _: return "Invalid day number"
print (weekday(3))
print (weekday(6))
print (weekday(7))
"""

def f(x):
    match x:
        case ['a']:
            print("a and !")
        case ['b']:
            print("b and !")

#if __name__ == "__main__":
  #  f(["a"])

#x = ["a", "b"]
#f(x)
