def name(f_name, l_name):
  if f_name == "" or l_name == "":
    print("Plase type a name and last name!")
    return
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"
  
print(name(input("What's your name?: "), input("What's your last name?: ")))
