<h1 align="center">Nonsense generator</h1>  

### What Is This?

Here I tried to make a word generator based on [Markov's chains](https://youtu.be/QI7oUwNrQ34?is=i0-eFHqMbeuu5OPh). The creator of the idea is [Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon) (if I understood it correctly).

### How Does It Work?

**Firstly**, the program reads very huge text with lots of words.  
**Secondly**, for each set of characters, it calculates the probability which particular letter will be next. For convenience, I will call this set of characters a token.  
**The last step** - for each token generate one of the most likely chars.

### Experiment N°1

![Experiment_1](Experiment_1.png)
As the text I took the work of Alexander Sergeevich Pushkin "Eugene Onegin". Then I formatted it (removed unnecessary symbols like '!', ';' and more). The result I received consists of 30 most likely characters (File: [generator1.py]()).

### Experiment N°2

![Experiment_2](Experiment_2.png)
Here I added the initial token, which will be used to generate the next letter. On the next step, as a token my program will take the first one without the first character + new letter.  
* Old token: onegin  
* Next letter: t  
* New token: negint  

### Experiment N°3

![Experiment_3](Experiment_3.png)
Here I have added the work "Sherlock Holmes" for more possible tokens. Also, I left whitespaces in the text. File: [generator2.py]().

### Conclution

* I was able to make a program that anticipates subsequent characters!

* I realized what Shannon did: the longer the length of the initial token, the more meaningful the answer will be.

### Special Thanks

I would like to thank [Vert Dider](https://youtube.com/@vertdiderscience?si=dzxT4tMADPAR1VDg) very much for the [video](https://youtu.be/QI7oUwNrQ34?is=i0-eFHqMbeuu5OPh) about Markov's chains.  
Also thanks to  [Royallib](https://royallib.com/) for literature.

