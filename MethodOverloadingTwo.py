class Marks:
    def enter(self, *args):
        if len(args) == 1:
            return f"Entered marks: {args[0]}"
        elif len(args) == 2:
            return f"Marks in {args[0]}: {args[1]}"

m = Marks()
print(m.enter(85))                  
print(m.enter("Math", 92))         
