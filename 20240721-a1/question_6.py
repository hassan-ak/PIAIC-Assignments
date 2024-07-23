s: str = "  Python is fun!  "


stripped_s = s.strip()
print(stripped_s) 

left_justified = stripped_s.ljust(20, "*")
print(left_justified)  


right_justified = stripped_s.rjust(20, "*")
print(right_justified)  
