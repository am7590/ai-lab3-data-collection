# Lab 3 Data Collection

## Setup:
```pip install wikipedia```

## To use:
1) Run the program
2) Input language (en/nl)
3) Input the path of the output file (a .txt file)
4) Enter topics to search wikipedia for
     - Please note that I did not test searching multiple topics at a time
  
## Example output:
- language = 'en', output = 'output.txt', topic = 'Python Programming Language'
 ```
en|Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the
en|use of significant indentation.Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including
en|structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included"
en|language due to its comprehensive standard library.Guido van Rossum began working on Python in the
en|late 1980s as a successor to the ABC programming language and first released it in
...
 ```

- language = 'nl', output = 'output.txt', topic = 'Amsterdam'
 ```
nl|Amsterdam is de hoofdstad van Nederland. De stad ligt aan het IJ, het Noordzeekanaal en
nl|de monding van de Amstel in de gelijknamige gemeente Amsterdam in de provincie Noord-Holland. Qua
nl|inwoneraantal is Amsterdam met 873.338 inwoners (1 januari 2021) de grootste stad van Nederland. De
nl|metropoolregio Groot-Amsterdam telt 1.459.402 inwoners.Amsterdam dankt zijn naam aan de ligging bij een in de
nl|13e eeuw aangelegde dam in de Amstel. De stad wordt in het Amsterdams ook Mokum
...
 ```
