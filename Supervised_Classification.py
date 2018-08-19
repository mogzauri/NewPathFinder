
# coding: utf-8

# # Supervised Classification

# In[ ]:


-#Use these bands for prediction.
var bands = ['B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B10', 'B11'];

# Load a Landsat 8 image to be used for prediction.
var image = ee.Image(LandSatScene) # or composite here
    .select(bands);

#    Load training points. The numeric property 'class' stores known labels.
var points = ee.FeatureCollection(Training_Feature)
    .remap([1, 2], [0, 1], 'class');

#  This Overlays the points on the imagery to get training.
var training = image.sampleRegions({
  collection: points,
  properties: ['class'],
  scale: 30
});

# Train a CART classifier with default parameters.
var trained = ee.Classifier.cart().train(training, 'class', bands);

# Classify the image with the same bands used for training.
var classified = image.select(bands).classify(trained);

# Display the inputs and the results.
Map.centerObject(image, 10);
Map.addLayer(image, {bands: ['B4', 'B3', 'B2'], max: 0.4}, 'image');
Map.addLayer(classified, {min: 0, max: 1, palette: ['00FF00', 'FF0000']},
  'classification');

