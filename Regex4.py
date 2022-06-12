import re
message= 'Yo Hello matt'
beginswithHelloRegex= re.compile(r'^Hello')
mo= beginswithHelloRegex.search(message)
if mo == None:
    print('The phrase dosent start with Hello')
# when you put ^ before anything else= phrase starts with... $ and the end of the phrase = inverse


endswithHelloRegex= re.compile(r'Hello$')
emo= endswithHelloRegex.search(message)
if emo == None:
    print('The phrase end  with Hello')


digitsRegex= re.compile(r'^\d$')
dmo= digitsRegex.search(message)
if dmo == None:
    print('The phrase end & start with a number')

series= "4545x454"
alldigitsRegex= re.compile(r'^\d+$')
smo= alldigitsRegex.search(series)
if smo == None:
    print('The phrase end & start with a number')#returns this because with the "+" = all the number has to be digits the "x" makes it fuck up

story='The cat in the hat ate at the mat that was flat'
atRegex= re.compile(r'.at')# .= anything that ...
atRegex2=re.compile(r'.{1,2}at')# bcuz its anything this returns "' 'cat" becuz space counts as a caracter

print(atRegex2.findall(story))

nameRegex = re.compile(r'First Name:(.*) Last Name: (.*)')
mo=nameRegex.findall('First Name: Al Last Name: Sweigart') # (.*) = greedy(most possible caracters,   (.*?)= non greedy
print(mo)


serve=' < to serve humans> for dinner.>'
nongreedy= re.compile(r'<(.*?)>')
print(nongreedy.findall(serve)) # if it was greedy would do everything biggest possible

serve2=' < to serve humans> for dinner>.\n tommorow>'
greedy= re.compile(r'<(.*)>')
print(greedy.findall(serve2))# here you could see becuz of the \n (new line) only thing(.*) dosent count

greedy =re.compile(r'<(.*)>', re.DOTALL)# the dot all functions print likes it is
print(greedy.findall(serve2))
#if you add a re.I it makes cases not matter

message= 'Agent Alice and Agent Bob are safe, agent Bargos is the bad guy'
namesRegex= re.compile(r'Agent \w+', re.I)
print(namesRegex.sub('Redacted', message))

message= 'Agent Alice and Agent Bob are safe, agent Bargos is the bad guy'
namesRegex2= re.compile(r'Agent (\w)\w*',re.I)
print(namesRegex2.sub(r'Agent \1****', message))

#verbose re.verbose use in likre.I or re.Dotall lets u use # in re compile just add '''

# if you want to use 2 of them use,     re.I | re.Verbose| ...
