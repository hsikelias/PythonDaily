# Match Case Statements

A match statement will compare a given variable's value to different shpes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

The match case consists of three main entities: 

1. The match keyboard
2. One or more case clauses
3. Expression for each case

        x = 4
        # x is the variable to match
        match x: 
        # if x is 0
           case 0: 
              print("x is zero")
        # case with if-condition
           case 4 if x % 2 ==0:
              print("x %2 == 0 and case is 4")
        # empty case with if-condition
           case _ if x < 10:
              print("x is <10>)            
        # default case(will only be matched if the above 
           cases were not matched.)
        # so it is basically just an else: 
           case _ :         

# Syntax : 

      match variable_name: 
               case 'pattern1' :
        // statement1
               case 'pattern2' :
        // statement2
               case 'pattern3' :
        // statement3                      

