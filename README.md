# Subtitle File Convertor
Use Python to write a program that converts a .srt subtitle file to our own
JavaScript format that we can plug into our Subtvtle program. Your program
should read each line of a subtitle file to gather information and it should
build up it's own strings in the new format and write the result out to a file.

```
python3 process_subtitles.py
```

Your program should create a new file called `output.js`.

## File Formats
The original .srt format isn't in JavaScript. The instructional team has
converted the .srt file to JavaScript for you.

If you're curious, you can read more about the original file format here:
https://en.wikipedia.org/wiki/SubRip#SubRip_text_file_format

### Original .srt Format
```
0
00:00:36,830 --> 00:00:39,430
Act as normal and calm
as you can.

0
00:00:40,470 --> 00:00:42,550
I'll see if
he has time for you.

0
00:00:40,470 --> 00:00:42,550
Careful

0
00:00:40,470 --> 00:00:42,550
Some subtitles only
have only one line.

```

### Translated JavaScript Objects
```js
var SUBTITLES = [
  {
    duration: "00:00:36,830 --> 00:00:39,430",
    line1: "Act as normal and calm",
    line2: "as you can.",
  },
  {
    duration: "00:00:40,470 --> 00:00:42,550",
    line1: "I'll see if",
    line2: "he has time for you.",
  },
  {
    duration: "00:00:40,470 --> 00:00:42,550",
    line1: "",
    line2: "Careful",
  },
  {
    duration: "00:00:40,470 --> 00:00:42,550",
    line1: "Some subtitles only",
    line2: "have only one line",
  }
];
```
