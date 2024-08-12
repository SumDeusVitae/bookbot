path = "books/frankenstein.txt"
def main():
    with open(path) as f:
        file_contents = f.read()
        print(f"--- Begin report of {path} ---")
        words = file_contents.split()
        print(f"{len(words)} words found in the document")
        print()
        lower_content = file_contents.lower()
        d = {}
        for each in lower_content:
            if each in d:
                d[each] += 1
            else:
                d[each] = 1
        sorted_d = sorted(d.items(), key = lambda x: x[1], reverse= True)
        for each in sorted_d:
            if each[0].isalpha():
                print(f"The '{each[0]}' character was found {each[1]} times")
        print("--- End report ---")

main()