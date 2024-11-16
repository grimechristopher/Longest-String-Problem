"""
Finding the Longest String Chain 
You are presented with a string chain, defined as follows: let string A be a string in the initial array.  
If removing any single character from string A yields a new string B that is contained in the initial  array of strings, 
then strings A and B form a string chain of length 2. Similarly, if removing any  single character from string B yields a new string C that is contained in the initial array of strings,  
then strings A , B , and C form a string chain of length 3.  
Given this list of strings, design an algorithm that returns the longest possible string chain, that  may be built from the given strings. 
The algorithm should return the string chain in descending  order (i.e., from the longest string to the shortest one). 
Note that string chains of length 1 are not  acceptable; if the list of strings does not contain any string chain formed by two or more strings,  
the function should return an empty array. You may assume that there will only be one longest  string chain.  
"""

# Time Complexity O(n^2 * m)
def find_longest_chain(strings):
    # Sort by length in descending order, longest first
    strings.sort(key=len, reverse=True) # O(n log n)
    
    longest_chain = []
    for string in strings: # O(n)
        current_chain = [string]
        found_next = True
        
        while found_next: # O(m)
            found_next = False
            
            # Try removing each character one at a time
            for i in range(len(current_chain[-1])): # O(m)
                # Wow learned some new Python syntax here
                # [-1] is the last element in a list
                # [:i] is a slice from the beginning to i
                # [i:] is a slice from i to the end
                new_string = current_chain[-1][:i] + current_chain[-1][i+1:] # slice sting happens in O(m)
                # If we find this shorter string in our list, add it to the current chain
                if new_string in strings: # O(n)
                    current_chain.append(new_string)
                    found_next = True
                    break
        
        # Update longest chain if this one is longer
        if len(current_chain) > len(longest_chain):
            longest_chain = current_chain[:] # O(1)
            
    return longest_chain

# O(n log n) + O(n) * O(m) * O(n) + O(1) = O(n^2 * m)
# n is the number of strings
# m is the length of the string

# Test
strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]
print(find_longest_chain(strings))
