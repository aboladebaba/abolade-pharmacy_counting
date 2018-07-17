# Introduction

This contibution documents and explains the approach I had taken to solve the given problem in this competition. I did not see any necessity to change the name of the source file, I made annotations in respective places I felt I need to add a line to indicate what was going through my mind when I was creating my solution.

# Abolade's Approach

The approach I adopted in crafting code response to this competition problem was to use python's in-built data structures such as dictionary, list and tuple.
* I used a dictionary to build a collection of drug names and nested lists to collect their associated values. This reduced my collection space from over 24 million rows less than 3000 elements that I can access in costant time by indexing into the resulting dictionary.
* One of the nested lists mentioned above was used to collect prescriber IDs, the ID uniquely identifies a prescriber. This made it easier to call ***SET*** function and subsequently finding the length of the result to arrive at number of unique prescribers. 
* I also called ***SUM*** function on the second list collection to obtain the total costs for each drug name.
* I created a tuple of drug_name, num_prescriber and total_costs, which I collected in a list to implement the sorting requirement for the file output.

***Note***: Please see my source file for further annotations.

# Abolade's Test

Here is directory what my directory structure looked like before I started running the test:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── pharmacy-counting.py
    ├── input
    │   └── itcont.txt
    ├── output
    |   └── top_cost_drug.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── itcont.txt
            |   |__ output
            |   │   └── top_cost_drug.txt
            ├── abolade-test_1
                ├── input
                │   └── itcont.txt
                |── output
                    └── top_cost_drug.txt 

I retained the `itcont.txt` filename in my test folder `abolade-test_1`. I reused the original test script that came with the competition.



