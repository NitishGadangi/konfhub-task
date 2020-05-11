
## konfhub-task
Solution for the task allotted by konfhub using python
**Task to complete:** 
* Extract contents from given Api link
* Print the contents in a human readable format, e.g.: `“San Antonio CyberSecurity Conference”,  November 6th, 2019, San Antonio, TX, US, Paid. https://futureconevents.com/events/san-antonio/”` 
* Identify exact duplicates (if any)
* Identify semantic duplicates (i.e., the conferences are same but the details provided are slightly different, e.g., “React Conference 2019” in one entry and “ReactConf ‘19” in another entry but the other fields are same or similar). 

**Technology used:** `python`

## Code Explanation

 - Used `requests` library to get the json response from given API link
 - `print_content(all_conferences)` prints all the content from the API response in human readable format
 - `generate_csv(all_conferences)` generates a csv file of content fetched
 - `remove_exact_and_semantic_duplicates(all_conferences)` removes all exact and semantic duplicates
 - The process used here for identifying `semantic duplicates` is a general approach where each json object is compared with all other objects in the list and differences are extracted. If there are <=3 differences it is considered to be duplicate.
 - However, there several other efficient methods to achive this. But they involve machine learning approch which seemed to a way bigger and complecated. So, I went with current layman approach
 - Refer comments within the code to get a better idea of each defination

## Execution Instructions
- Clone or download the repository
- For first time, run this in Powershell
```
pip install requests
```
- Next do this to execute
```
python task.py
```
- follow on screen instructions for further process

## Demo Output

    PS G:\aaKonfHub\github\konfhub-task> python .\task.py
    Hello World
    
    ....Fetching Json Response from the API...
    
    ....103 paid conferences
    ....28 free conferences
    
    ....searching exact and semantic duplicates...
    
    ....1 duplicates found
    ....131 total conferences
    
    ....Filtering Done......
    
    
    ---Select an Option--
    -> 1. Print the contents in a human readable format
    -> 2. Print Duplicates
    -> 3. Export the contents to csv
    option(1/2/3): 1





**by Nitish  Gadangi visit https://nitishgadangi.github.io/ to know more about me**
