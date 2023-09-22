# Mad Libs Generator

# Story template
story = "Most doctors agree that bicycle of __verb__ is a/an __adjective__ form of exercise. __verb__ a bicycle enables you to develop your __part_of_body__ muscles as well as __adverb__ increase the rate of a __part_of_body__ beat. More __noun__ around the world __verb__ bicycles than drive __animals__. No matter what kind of __noun__ you __verb__, always be sure to wear a/an __adjective__ helmet. Make sure to have __color__ reflectors too!"

# Prompting the user for inputs
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
part_of_body = input("Enter a part of body: ")
adverb = input("Enter an adverb: ")
noun = input("Enter a noun: ")
animals = input("Enter an animal (plural): ")
color = input("Enter a color: ")

# Filling in the blanks
story = story.replace("__verb__", verb)
story = story.replace("__adjective__", adjective)
story = story.replace("__part_of_body__", part_of_body)
story = story.replace("__adverb__", adverb)
story = story.replace("__noun__", noun)
story = story.replace("__animals__", animals)
story = story.replace("__color__", color)

# Displaying the final story
print(story)