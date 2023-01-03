# wave-function-collapse
this program uses the wave function collapse to generate different maps

change the string in variable 'image_folder' to the name of the folder with different images
to change what type of map loads

to make your own tiles you can!

just remember the json file is ordered like this 

{
  'image-name': {
    sides: ['','','',''],
    rotations: [0, 90, 180, 270]
  }
}

for Sides:
  - starting at the topleft of the image add a charecter into each string
    as if you were going clockwize around the image, this can be any length
    but they all have to be the same length.
    
~~~text
  e.g: 
            a b c
        +-----------+
        |           |   
     c  |           |   a 
     b  |           |   b
     a  |           |   c
        +-----------+
            c b a 
~~~
            
for rotations:
  - this is where you ad the rotations of the image, if your image is symetrical
    you only need to rotate it in [0, 90], or if it is symetrical in all directions then [0]
    this will avoid duplicates of the same tile.
