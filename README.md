To run this app just execute "docker compose up"

Here is the task:

Attached is a csv file that contains image data referenced by the column depth. The rest of columns (200) represent image pixel values from 0 to 255 at each depth.

The challenge consists on the following requirements:

·       The image size is relatively big. Hence, there is a need to resize the image width to 150 instead of 200.

·       The resized image has to be stored in a database.

·       An API is required to request image frames based on depth_min and depth_max.  

·       Apply a custom color map to the generated frames.

·       The solution should be based on Python.

·       Bonus: deployment of the solution in a cloud service.
