def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "enter name"
    fo_f_name=f_name.title()
    fo_l_name=l_name.title()
    return f"{fo_f_name} , {fo_l_name}"



print(format_name(input("enter name"),input("enter last name")))

def choice_1(text):
    output= text + text
    return output
def choice_2(text):
    output=text.title()
    return output

print(choice_2(choice_1("hello")))
