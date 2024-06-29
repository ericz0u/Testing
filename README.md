# Testing dump
Random things I experiment with through summer 2024. Mostly testing out things for my main projects(Weiss Judge, Weiss Translate, Weiss Player). Langchain, BERT model fine-tuning, CNNs, etc.

### 6/29/2024

haven't been writing much, just dumping files but I might as well start. Today I was goofing around with autofocus and how that could be improved. I do a lot of photography as a hobby so I'm pretty interested in seeing if AI could make autofocus work better. What I wanted to try was seeing if I could have a model that guesses the size of something, then calcualtes how far the object is from the camera using the focal length. This example im particular I tried doing it for birds. I started with a model from huggingface to classify the bird species(then from there can make a map of species/sex -> rough size). Next I used yolo7 to draw a bounding box and find how big diagonally the bird was in the image. I did diagonally because bird length is from beak to tail, and birds usually sit in a way that their body is diagonal. After that I used a formula (real_size_mm * focal_length_mm) / apparent_size_mm to get the distance to the bird. I haven't had a chance to test it, but it outputs reasonably numbers using the images I had at least lol. Might test it later with something like this: https://openaccess.thecvf.com/content_CVPR_2020/papers/Herrmann_Learning_to_Autofocus_CVPR_2020_paper.pdf 

Something I was thinking about was maybe this model inititally to grab focus close-ish to a target, then PDAF or CBAF to get the focus nice and crispy. Then make that autofocus system not move too far from the initial point, then if needed I could a button that redoes the distancing -> lock on? idk, all just thinking lol

