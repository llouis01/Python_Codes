# A program that writes to a file. Py2.7 (@roiminuit)

from sys import argv
script, filename = argv

print "\nWe are going to select a pre-existing file and edit it."
print """
\nWhich file would you like to delete?
"""
altered_file = raw_input("\n--> ") # prompts user for file to edit
print "\nAre you sure you want to edit %r\'s content?" % altered_file
print "\nHit RETURN for yes and CTRL -C to cancel."
raw_input("\n--> ")
print "\nDeleting content of %r now. Ciao!" % altered_file
altered_file = open(filename, 'w') # open b4 truncate.
altered_file.truncate() # need to open b4 truncate.

print """
\nAlright, here we go! Story time!
I will start the story and you complete it!
"""
print "Once upon a time in Skyrim..."
altered_file.write("Once upon a time in Skyrim...")
altered_file.write("\n")
user_line1 = raw_input("Your turn: ")
altered_file.write(user_line1)
altered_file.write("\n")
print "Dragons were still roaming the sky,"
altered_file.write("Dragons were still roaming the sky,")
altered_file.write("\n")
user_line2 = raw_input("Your turn: ")
altered_file.write(user_line2)
altered_file.write("\n")
print """\nALright now! You're crashing my system :D
What a storyteller you are! Good Job!
I will save our little story and you can read it
whenever you want to remember me! See you next time!
 """
altered_file.close()
