# WAP to display the largest word from the String
string = "Passion fuels purpose"
string =list(string.split())
print(string)
sort_string = sorted(string, key=len)
print(sort_string)
print(sort_string[-1])