This directory contains the files to evaluate MT evaluation metrics,
it's not production standards data, neither will it be helpful in
shared task participation but it provides a good testbed for new metrics
implementation and comparison against metrics already available in
nltk.translate.*_score.py to validate the numbers.

It includes the first 100 sentences from the newstest 2015 development set
for the English-Russian language part, made available at Workshop for Machine
Translation 2016 (WMT16) and the Google Translate of the English source sentencs.

[Plaintext]

 - newstest-2015-100sents.en-ru.src.en
 - newstest-2015-100sents.en-ru.ref.ru
 - newstest-2015-100sents.en-ru.google.ru

[SGM]

 - newstest2015-100sents-enru-ref.ru.sgm 
 - newstest2015-100sents-enru-src.en.sgm
 - newstest2015-100sents-enru-google.ru.sgm

And the original ,sgm files from WMT16:

 - newstest2015-enru-ref.ru.sgm 
 - newstest2015-enru-src.en.sgm 


The plaintext are converted from the .sgm files from the development sets in WMT with 
the following command:

    sed -e 's/<[^>]*>//g; /^\s*$/d' newstest-2015.enru.src.en.sgm | head -n100 > newstest-2015-100sents.en-ru.src.en
    sed -e 's/<[^>]*>//g; /^\s*$/d' newstest-2015.enru.ref.ru.sgm | head -n100 > newstest-2015-100sents.en-ru.ref.en

The tokenized versions of the natural text files above are processed using Moses tokenizer.perl:

    ~/mosesdecoder/scripts/tokenizer/tokenizer.perl -l ru < newstest-2015-100sents.en-ru.ref.ru > ref.ru
    ~/mosesdecoder/scripts/tokenizer/tokenizer.perl -l ru < newstest-2015-100sents.en-ru.google.ru > google.ru
    ~/mosesdecoder/scripts/tokenizer/tokenizer.perl -l en < newstest-2015-100sents.en-ru.src.en > src.en

The Google translate outputs are created on 25 Oct 2016 10am. using the English source sentences.

The newstest2015-100sents-enru-google.ru.sgm is created using the wrap-xml.perl tool in Moses:

    ~/mosesdecoder/scripts/ems/support/wrap-xml.perl ru newstest2015-100sents-enru-src.en.sgm Google < google.ru > newstest2015-100sents-enru-google.ru.sgm


The BLEU scores output from multi-bleu.perl is as such:

    ~/mosesdecoder/scripts/generic/multi-bleu.perl ref.ru < google.ru 
    BLEU = 23.17, 53.8/29.6/17.6/10.3 (BP=1.000, ratio=1.074, hyp_len=1989, ref_len=1852)

The mteval-13a.output file is produced using the mteval-v13a.pl

    ~/mosesdecoder/scripts/generic/mteval-v13a.pl -r newstest2015-100sents-enru-ref.ru.sgm -s newstest2015-100sents-enru-src.en.sgm -t newstest2015-100sents-enru-google.ru.sgm  > mteval-13a.output
