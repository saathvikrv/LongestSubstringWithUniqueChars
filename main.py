def FMLS(stri):
  max = 0
  i = 0
  j = 0
  substr = {}
  maxI=0
  maxJ=0
  while i<len(stri):
    if stri[i] in substr:
      while stri[i] in substr:  
        substr.pop(stri[j])
        j+=1
    substr[stri[i]] = stri[i]
    i+=1
    if len(substr)>max:
      max=len(substr)
      maxI=i
      maxJ=j
  return stri[maxJ:maxI]

# print("Starting...")
# print(FMLS("aaaaaabcabcdeabcdefabcdedddddddddddd"))

# "" - 0
# "aaaaaaaaaaaaaaaa" - 1
# "abcdefghijklmnopqrstuvwxyz" - 26
# "abccbabcabacbacbacbcabcacbaacbcabbacbacbcabacbbca" - 3
# "efefeefeffefeeffeefefefefee" - 2
# "8y3ceuc48n4n8c9" - 6
# "aaaaaabcabcdeabcdefabcdedddddddddddd"
#
#
#
#
#
#
#
#
#
#
#
