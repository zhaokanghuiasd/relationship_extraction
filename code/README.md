# Triplet Extraction
## File structure
### EntityExtraction.py
This file extract the entities from sentences. 
Three rules show in three functions. 
Finally, they will be merged into a entity list.
This file has a main function, and you can do some test in it.

### RelationExtraction.py
We define three patterns to find the relationship of a sentence.
Three patterns will also be merged in the merge_relationship function.
This file has a main function, and you can do some test in it.

### CleanBrandModel.py
This file handles the dirtiness of brand and model.

### CleanCommentInfo.py
This file handles the dirtiness of comment information.

### Write2Neo.py
This file will complement the task that write the extracted triplet into database.

### info
info is a folder that we use to crawl the data from e-commerce platform.
You can get the data directly from the raw_data folder in dataset.
You can also get the preprocessed data in preprocessed_data folder in dataset.

## How to start
This project use python3.6, the libraries used are list in the requirements.txt.
run main.py using python main.py command. 
You can also change the test sentence in this file.