"""
The Pirates of Silicon Valley file contains an encoding
error. Run the program to find the error and manually look
in the file to find out what the problem is.

filename = "pirates_of_silicon_valley.srt"
"""
filename = "small_subtitles.srt"
my_file = open(filename)
for line in my_file:
  line = line.strip()
  print(line)
