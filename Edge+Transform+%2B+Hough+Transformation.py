
# coding: utf-8

# In[ ]:


# Canny Edge transformation ()

var image = ee.Image(LandSatScence).select(Bands);
var canny = ee.Algorithms.CannyEdgeDetector({
  image: image, threshold: 10, sigma: 1
});
Map.setCenter(Coordinates, 10);
Map.addLayer(canny, {}, 'canny');

# Hough transformation to identify lines/paths. This transformation removes the none line features due to continual gradient shifts in landscape
var hough = ee.Algorithms.HoughTransform(canny, 256, 600, 100);
Map.addLayer(hough, {}, 'hough');

