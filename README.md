# agsmaxid
Find the current maximum Layer ID for an ESRI Map Service. This is helpful when you are numbering your layers manually (using the Layer ID option in Layer Properties > General). As services grow the layers may no longer be in numeric order, so this script can help you identify the next highest number available. 

Note that it doesn't look for gaps in the numbers, it only returns the highest number.

## Usage
```shell
agsmaxid <url to MapServer>
```

## Example
```shell
agsmaxid http://sampleserver1.arcgisonline.com/ArcGIS/rest/services/PublicSafety/PublicSafetyOperationalLayers/MapServer
```
