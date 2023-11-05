# FindIt

Starting from 2D graphs to 3D meshes representing trees.
Two approaches:

* Using ML algorithms (openCV) to detect patterns on a image and return the center point of each tree.

* Send the image to our API running Meta AI Segment Anything Model(SAM)

Both procedures result in very capable tree detection (80% accuracy).

![Segmentation](docs/segment.png)

# How to
### ML Approach
1. Install [GH Python remote](https://github.com/pilcru/ghpythonremote)
1. Open the GH script
1. Import an satellite image and the template image (snip of the tree you want to detect)

1. Run the script and new trees will placed on Rhino

### AI Approach

1. Clone this repository 
1. Run ```pip -r requirements.txt```
1. Run the SAM model from the sample inside the main.py file. Remember to store the image you want to detect to the same folder under the name ```input.png```
1. The script will export a CSV file with name.
1. Use the csv as in put for the Grasshopper file


## Presentation


<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSV6cUZms1wENgwxeoc-QKmOsyPmN34CTDBhYT4XpVvdQYInBM4UboOhdazcPtqfcaKj7JLt-59oNVy/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

# License

The MIT License (MIT)
Copyright © 2023 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
