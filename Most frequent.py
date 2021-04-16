def Sorted_list(count): #we define the function sorted list and assign "count" to return the count
    sorted_count={}      #blank dictionary
    sorted_keys = sorted(count, key = count.get, reverse= True) #this enables us to get the value of each count while converting them to keys and allowing us to display it in descending order              
    for i in sorted_keys:
        sorted_count[i] = count[i]  #we have defined the count for each letter
    return sorted_count          

def most_frequent(word):
    Count = {}
    for i in word:
        if i in Count:
            Count[i] += 1        #this counts the increment and will check for each value that is repeated                         
        else:
            Count[i] = 1         #if recurrrence is 1
    Sorted_Count = Sorted_list(Count)
    return Sorted_Count


word = input("Enter a word or sentence of your choice : ") 
letter = most_frequent(word)
print("The number of times each letter in '",word, "'has recurred is :")
for i in letter:
 print( "The letter""(",(i),")""was repeated - ",letter[i],"times")

