from turtle import forward, left, right, shape, speed, Screen, color as tcolor, home, width as twidth, penup, pendown, goto

from colorama import init;
from termcolor import colored;

init();

def turtle_movement_group(*group:list, color="black"):
   '''
   This function takes in a dictionary comprising of 1 group of turtle movments.
   Parameters:
   group: An array of movents with each value being a dictionary of movement type as key and number of paces as value. (e.g.[{forward=90}, {forward=35}, {right=90}, ...]).
   '''
   TurtleMovementMap = dict(forward=forward, right=right, left=left);

   try:
      for entry in group:
         if not TurtleMovementMap.get(tuple(entry)[0]): raise Exception;
   except Exception:
      print(f"Error!!! The movements entered in the parameters MUST be one of these: {list(TurtleMovementMap.keys())}.\n{Exception}.")
      return Exception;
   
   try:
      if color not in ['black', 'red', 'pink', 'green']: raise Exception
   
   except Exception:
      print(f"Please enter ['black', 'red', 'pink', 'green'] as colors. You entered{color}.");
      return Exception;

   tcolor(color)
   
   for i in group:
      MovementDict = tuple(i.items())[0]
      TurtleMovementMap[MovementDict[0]](MovementDict[1])

def turtle_design(*turtle_movement_groups):
   '''
   This function takes in a LIST of 'turtle_movement_group' function declarations (UNCALLED) and then loops through each function in the list. 

   When it reaches that particular function in the loop, THAT is when that function will be called. 

   This contunues till the loop ends, resulting in a design.

   parameters:
   turtle_movement_groups: a list of turtle_movment_group DECLARATIONS [turtle_movment_group1, turtle_movement_group2, turtle_movement_group3, etc...]
   '''
   try:
      NotAFunction = list(filter(lambda x: type(x).__name__!= 'function', turtle_movement_groups));

      if (len(NotAFunction)) > 0: 
         WrongTypes = list(map(lambda x: type(x).__name__, NotAFunction));
         raise TypeError(f"Wrong datatypes entered: {WrongTypes}")
   
      for i in turtle_movement_groups:
         i()
   except TypeError as type_err:
      print(f"Each argmument you add inside this function {colored(f'must be a function declaration', attrs=['bold', 'underline'])} (function that is NOT called). It must be a type {colored('function', color='red', attrs=['bold'])}.\n{colored('DO NOT CALL THAT FUNCTION INSIDE THE ()', color='red', on_color='on_light_yellow', attrs=['bold'])}.\nJust provide the name.\n\nAlso, make sure the {colored('type', attrs=['bold', 'underline'])} for each argument is a function. Right now, at least one of those datatypes you entered is/are {colored(f'{WrongTypes}', on_color='on_light_yellow', attrs=['bold'])}.\n{dict(errorCode=type_err)}.")

