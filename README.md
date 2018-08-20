# NewPathFinder
TDI CAPSTONE PROJECT

[![New Path Finder](https://img.youtube.com/vi/R4yNkrw5huM/0.jpg)](https://www.youtube.com/watch?v=R4yNkrw5huM "New Path Finder")
<br>
This video is an overview of the project with visualizations.
<br>
<br>
My TDI capstone project new path finder uses remote sensing and webscraping to help answer the question what happens to people’s daily lives when borders and boundaries change.  Particularly, how do new paths form when old paths are obstructed by new boundaries and moving borders.  
<br>
<br>
This project began by scraping news websites and international organization reports in multiple languages to identify hundreds of locations where borders and boundaries have moved in the last 10 years in Georgia and Ukraine.  Webscraping identified names and dates of border movement.  This was joined with regional geospatial data.  In Google Earth Engine, composite scenes were constructed from Landsat8 images for 3 months before and 3 months after noted border movement, 3KM in each direction from the point (6km squares).  Each scene prioritized landsat tiles based on a cloudiness index and were orthorectified accordingly. 
<br>
<br> 
For each post-border move composite, I ran an unsupervised classification to group pixels based on possible landcover types. I used K means clustering with weka inference to develope clusters of landcover types, taking into account the 7 most relevant bands. I then ran a supervised classification using the clusters from the unsupervised classification as training on the pre-border move composite.  These transformed composites were then used to deterimine landcover change. 
<br>
<br>
For the classified composites, I constructed a landcover change composite highlighting where pixel values differed between the two composites.  
<br>
<br>
Finally, in the landcover change composite, I performed edge transformations on each of the landcover change composites.  This reveal gradient shifts, but I need only the linear ones, which would mark paths.  To do this, I then performed a hughes tranformation to reveal the remaining lines.  These poly-line vectors are the predicted paths.
<br>
<br>
In the end, using google earth engine I’ve processed over 60 gb of time sequenced hyperspectral remotely sensed data for larger supervised and unsupervised classifications. Currently I am working to extract significant features of reflectance curves from the identified path to improve the ability to predict paths on unknown terrain. 
<br>
<br>
I've included snippets of code to give an example of the code I used in the various modules in Google Earth Engine.  For each location, a series (pipeline) of module were used to streamline the processing of the remotely sensed data.
