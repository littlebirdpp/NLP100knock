#00
input_str="stressed"
print(0)
print(input_str[::-1])
print()

#01
input_str="パタトクカシー"
print(1)
print(input_str[::2])
print()

#02
input_str="パトカー"
input_str2="タクシー"
print(2)
ans=""
for i in range(4):
    ans+=input_str[i]+input_str2[i]
print(ans)
print()

#03
import re 
input_str="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
input_str_new= re.sub('[,\.]', '', input_str)
input_list=input_str_new.split()
ans=[]
for i in input_list:
    ans.append(len(i))
print(3)
print(ans)
print()

#04
input_str="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
input_str_new= re.sub('[,\.]', '', input_str)
input_list=input_str_new.split()
ans={}
for i in range(len(input_list)):
    if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        ans[i+1]=input_list[i][0]
    else:
        ans[i+1]=input_list[i][:2]
print(4)
print(ans)
print()

#05
def n_gram(target, n):
  # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
  return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]
target = "I am an NLPer"
print(5)
print(n_gram(target, 1))
# > ['I', ' ', 'a', 'm', ' ', 'a', 'n', ' ', 'N', 'L', 'P', 'e', 'r']
print(n_gram(target, 2))
# > ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
print(n_gram(target, 3))
# > ['I a', ' am', 'am ', 'm a', ' an', 'an ', 'n N', ' NL', 'NLP', 'LPe', 'Per']

words = target.split(' ')
print(n_gram(words, 1))
# > [['I'], ['am'], ['an'], ['NLPer']]
print(n_gram(words, 2))
# > [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
print(n_gram(words, 3))
# > [['I', 'am', 'an'], ['am', 'an', 'NLPer
print()

#06
print(6)
target="paraparaparadise"
target2="paragraph"
print(list(set(n_gram(target, 2))&set(n_gram(target2, 2))))
print(list(set(n_gram(target, 2))-set(n_gram(target2, 2))))
print(list(set(n_gram(target, 2))|set(n_gram(target2, 2))))
print()

#07
def templates(x,y,z):
    return(str(x)+"時の"+str(y)+"は"+str(z))

x=12
y="気温"
z=22.4
print(7)
print(templates(x,y,z))
print()

#08
def cipher(X):
    ans=""
    for x in X:
        if x.islower():
            ans+=chr(219-ord(x))
        else:
            ans+=x
    return ans
print(8)
print(cipher("KAUHGYJHKLK"))
print(cipher("aadK"))
print()

#09
import random
input_str="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
inputlist=input_str.split()
ans=""
for i in inputlist:
    if len(i)>4:
        sr = ''.join(random.sample(i[1:-1], len(i)-2))
        ans+=i[0]+sr+i[-1]+str(" ")
    else:
        ans+=i+str(" ")
print(ans)