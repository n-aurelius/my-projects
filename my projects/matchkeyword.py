#this is another approach for the if elif else 
name = input("what is your name? ")
match name:
    case "Harry" | "Hermione"| "ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")        

  #the ||||| that we used are another way of writing OR