# InbreedingAndDNA
This code is a simplification of DNA. It simulates breeding, mutations, and inbreeding thanks to a family tree. It connects DNA to specific attributes and its highly scalable.

# Dog Class

This code is a class called Dog. The Dog class can be initialized with various attributes such as name, dna, mother, father, color_coat, color_eyes, and coat_type. If no dna is specified, it will randomly generate dna. The Dog class also has a function called attribute_score that calculates the attribute score of the dog based on the dog's color_coat, color_eyes, and coat_type. The Dog class also has a generate_dna function that can determine the dog's dna based on the dna of its mother and father or randomly generate the dna if no mother or father is specified.

# Custom Dog Class

This code creates a function that allows the user to customize a dog by specifying the coat color, eye color, and coat type. The user is given options to choose from for each of these categories and can input the number of the desired option.

The function then uses the random library to generate a DNA code for each of the categories. Each option for the coat color, eye color, and coat type has a specific set of choices for the DNA code. For example, the DNA code for black coat color could be "BBb", "BbB", "bBB", "BBB", "BBY", "BYB", or "YBB".

Once the DNA codes are generated, they are all combined to form the final DNA code for the custom dog. The final DNA code can then be used to create a dog object using the Dog class from the dogclass library.

# Genetic Algorithm

The code implements a Genetic Algorithm (GA) to simulate the evolution of dogs over multiple generations. It starts by importing the required modules, including the Dog class from the dogclass module and the matplotlib library.

The GeneticAlgorithm class defines the main structure of the GA. It has an init method that initializes the population size and creates an empty list for the population. The generate_population method creates a population of random dogs using the Dog class. The rank_dogs method ranks the dogs based on their attribute score, which is calculated using the attribute_score method of the Dog class. The breed_top_dogs method breeds the top 10 dogs in the population to create new offspring. The run method runs the GA for a specified number of generations, calling the rank_dogs and breed_top_dogs methods at each generation.

Finally, the code creates an instance of the GeneticAlgorithm class, with a population size of X, and runs the GA for Z generations. The top Y dogs after the specified number of generations are then printed, along with their attribute scores and DNA information.
