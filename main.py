if __name__ == "__main__":
   from folder.functions import *

   shape("turtle"); #optional.
   speed(0); #optional.

   Screen();

   twidth(5)
   # group1 & group2 will be used in the square function call below.
   group1 = lambda: turtle_movement_group(dict(forward=90), dict(left=90), color="red");
   group2 = lambda: turtle_movement_group(dict(forward=90));

   square = turtle_design(*[group1 for i in range(3)], group2);

   home()

   Screen().exitonclick()
