# ACM Research Coding Challenge (Fall 2021)

## Explanation

I assigned sentiment values to various keywords throughout the provided text. Each of these keywords' values would be multiplied by a constant based on whether it showed a strong or weak expression of sentiment, as well as whether or not it invoked a positive or negative connotation. From there, I was able to calculate an overall score based on the sum of these sentiment scores. 

I used encapsulation to call a repeating Python function for each of the aforementioned steps. This enabled me to do the same for each sentence individually while simultaneously improving the readability of the program. 

I found an overall positive sentiment score of 4.5 for the given input. I expected a greater score of 10, so this result came as a surprise. I conclude that this must indicate that the positive second paragraph skewed my views of the text to more positive values or that more precision is needed in order to effectively process the keywords I found. 

The individual sentence scores were more or less consistent with what I expected. I'm glad I decided to include them because it justified my suspicion that the second paragraph was for more "positive" than the first, which shows me an example of using sentiment analysis to make reasonable albeit elementary conclusions from text. 

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

