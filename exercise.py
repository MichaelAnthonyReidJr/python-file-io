import re, string

def main():
    
    heritableWord = input("Please enter the root of the word: ")
    
    with open("origin.txt", "r") as file:
        
        line_count = 0
    
        for eachLine in file:
            line_count += 1  
            line = eachLine.strip()
            words = line.replace("--", " ").split()

            for eachWord in words:
                eachWord = eachWord.translate(str.maketrans('', '', string.punctuation))
                #While ignoring the case, search each word for a match to input 
                if re.search(heritableWord, eachWord, flags=re.IGNORECASE):
                    with open("line-numbers_and_words.txt", "a") as new_file:
                        new_file.write(f"{line_count}   {eachWord}\n")

if __name__=='__main__':
    main()