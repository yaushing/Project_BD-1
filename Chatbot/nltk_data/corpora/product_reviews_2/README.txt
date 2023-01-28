Product Reviews (9 products)

Available as ‘Additional Review Datasets (9 products)’ from
http://www.cs.uic.edu/~liub/FBS/FBS.html

Source:
http://www.cs.uic.edu/~liub/FBS/Reviews-9-products.rar

NB: Line-endings have been converted from DOS to Unix, and some
control characters and extended ASCII characters have been converted
to UTF-8.


*****************************************************************************
* Contact: Bing Liu, liub@cs.uic.edu 
*          http://www.cs.uic.edu/~liub
*****************************************************************************

                            README file

This folder contains annotated customer reviews of 9 products. 


All the reviews were from amazon.com. The data was used in the following 
paper:

Xiaowen Ding, Bing Liu and Philip S. Yu. 
	“A Holistic Lexicon-Based Approach to Opinion Mining." 
	Proceedings of First ACM International Conference on Web Search and Data Mining 
	(WSDM-2008), Feb 11-12, 2008, Stanford University, Stanford, California, USA.



Symbols used in the annotated reviews: 

  [t]: the title of the review: Each [t] tag starts a review. 
       We did not use the title information in our papers.
  xxxx[+|-n]: xxxx is a product feature. 
      [+n]: Positive opinion, n is the opinion strength: 3 strongest, 
            and 1 weakest. Note that the strength is quite subjective. 
            You may want ignore it, but only considering + and -
      [-n]: Negative opinion
  ##  : start of each sentence. Each line is a sentence. 
  [u] : feature not appeared in the sentence.
  [p] : feature not appeared in the sentence. Pronoun resolution is needed.
  [s] : suggestion or recommendation.
  [cc]: comparison with a competing product from a different brand.
  [cs]: comparison with a competing product from the same brand.


Finally, tagging is a hard task. Errors and inconsistencies are inevitable.
If you see some problems, please let us know. We also welcome your comments.


