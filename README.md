# Gif_Metadata
This repository was created and published as part of the Program for Cultural Heritage class (F'18) at the Pratt School of Information. 

The goal of this project was to explore trends and patterns in the metadata tags of the Giphy trending page. 
In order to do so the first script, giphy.py uses Giphy's API to collect the URLs for individual Gif detail pages from the trending endpoint.
The second script, dryscape.py, then loops through the JSON output to collect tag information from the Javascript output on each Gif detail page.

The resultant collection of tags were used in a Tableau visualization and a Processing Gif ticker to visualize the information in new ways and examine it for trends and shifts in language. 
