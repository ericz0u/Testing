# Testing dump
Random things I experiment with through summer 2024. Mostly testing out things for my main projects(Weiss Judge, Weiss Translate, Weiss Player). Langchain, BERT model fine-tuning, CNNs, etc.

### 7/02/2024
Followed a two hour video guide for terraform. A lot less intimidating than I thought it would be, it's just some simple code and commands. Hardest part is probably just figuring out which resources to provision in the first place.

Read a little about RT-DETR which seems like a promising new thing, might have to try and apply it for my bird af tracking side project lol
### 6/29/2024

haven't been writing much, just dumping files but I might as well start. Today I was goofing around with autofocus and how that could be improved. I do a lot of photography as a hobby so I'm pretty interested in seeing if AI could make autofocus work better. What I wanted to try was seeing if I could have a model that guesses the size of something, then calcualtes how far the object is from the camera using the focal length. This example im particular I tried doing it for birds. I started with a model from huggingface to classify the bird species(then from there can make a map of species/sex -> rough size). Next I used yolo7 to draw a bounding box and find how big diagonally the bird was in the image. I did diagonally because bird length is from beak to tail, and birds usually sit in a way that their body is diagonal. After that I used a formula (real_size_mm * focal_length_mm) / apparent_size_mm to get the distance to the bird. I haven't had a chance to test it with actual specific numbers, but it outputs reasonable numbers using the images I had at least lol. Might test it later with something like this: https://openaccess.thecvf.com/content_CVPR_2020/papers/Herrmann_Learning_to_Autofocus_CVPR_2020_paper.pdf 

Something I was thinking about was maybe this model inititally to grab focus close-ish to a target, then PDAF or CBAF to get the focus nice and crispy. Then make that autofocus system not move too far from the initial point, then if needed I could a button that redoes the distancing -> lock on? idk, all just thinking lol

also at the moment it doesn't work with images of flying birds, since their wingspans are so long. I've been thinking of ways to correct it, maybe do a ML model to draw a line along the bird's body? I could fine-tune yolo to do that and the data wouldn't be too hard to make. I could just spend a couple hours drawing a line across birds and get a couple hundred test images. That way I could get rid of the bounding box math too, just compare the length of the line to any one side of the image for percent. 

