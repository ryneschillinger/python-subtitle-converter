"""
The Pirates of Silicon Valley file contains an encoding
error. Run the program to find the error and manually look
in the file to find out what the problem is.

"""

filename = "pirates_of_silicon_valley.srt"
# filename = "small_subtitles.srt"
my_file = open(filename, encoding="ISO-8859-1")

# Compile list of all lines in subtitles file
all_lines = []

for line in my_file:
	line = line.strip()
	if "\"" in line:
		line = line.replace("\"", "\\\"")
	all_lines.append(line)


# Output to JS file
open("output.js")
output = open("output.js", "a")
output.write("var SUBTITLES = [\n")

line_count = 1
for line in all_lines:

	if line.isdigit():
		output.write("  {\n")

	elif '-->' in line:
		output.write(f"    duration: \"{line}\"\n")

	elif line == '':
		output.write("  },\n")
		line_count = 1

	else:
		output.write(f"    line{line_count}: \"" + line + "\"\n")
		line_count += 1

output.write("];")
