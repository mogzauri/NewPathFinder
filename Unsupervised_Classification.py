
# coding: utf-8

# / Unsupervised Classification / Clustering
# This is the base code derived from google's EE.cluster
# This is the base of the code I used to first make clustering decisions for the supervised classification. 
# 

# In[ ]:


## Load a pre-computed Landsat composite for input.
var input = ee.Image(LandSatScene);

## Define a region in which to generate a sample of the input.
var region = ee.Geometry.Rectangle(29.7, 30, 32.5, 31.7);

## Display the sample region.
Map.setCenter(31.5, 31.0, 8);
Map.addLayer(ee.Image().paint(region, 0, 2), {}, 'region');

## Make the training dataset.
var training = input.sample({
  region: region,
  scale: 30,
  numPixels: 5000
});

## Instantiate the clusterer and train it.
var clusterer = ee.Clusterer.wekaKMeans(15).train(training);

## Cluster the input using the trained clusterer.
var result = input.cluster(clusterer);

## Display the clusters with random colors.
Map.addLayer(result.randomVisualizer(), {}, 'clusters');

