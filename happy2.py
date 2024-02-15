# happy_stubs.py
#This program gives different outputs from country happiness, population, and GDP

#main function that calls on the other functions in this program
def main():

    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()
    

    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    # lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    #read_gdp_data(happy_dict)


 #This function makes a dictionary of countries with a happiness index
def make_happy_dict():
    #opens the happiness data file
    file = open("happiness.csv", "r")
    #This reads and skips the first line
    file.readline()
    #This creates an empty dictionary
    happy_dict = {}
    #This FOR loop adds country with happiness index in a dictionary
    for line in file:
        #This removes whitespace
        line = line.strip()
        #This splits the line by commas
        country, year, happy_index = line.split(",")
        #This adds the country and happiness index to the dictionary
        happy_dict[country] = happy_index
    #for country in happy_dict:
        #print(country, happy_dict[country])
    return happy_dict
    
def read_gdp_data(happy_dict):
    return

def lookup_happiness_by_country(happy_dict):
    return

# Function prints all the values in a dictionary d sorted by key
def print_sorted_dictionary(happy_dict):
    if type(happy_dict) != type({}):
        print("Dictionary not found")
        return
    print("Contents of dictionary sorted by key.")
    print("Key","Value")
    for key in sorted(happy_dict.keys()):
        print(key, happy_dict[key])
        
main()
