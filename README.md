## Mood for Zoom

## Inspiration
As universities and high schools shut down indefinitely, college professors and educators the world over have been **forced to abruptly move their lectures to the online medium of Zoom**. One of the most jarring shifts is **the loss of the ability to "read the room"**; most professors and public speakers actively gauge the mood of their audience based on body language and facial cues in the classroom and adjust accordingly to speed up, slow down, or pause for questions. 

On a Zoom call, however, the professor must focus on sharing their own screen and moving around the elements of their digital presentations. Even if they choose to view all the students' webcams, **it is unrealistic for a professor to quickly and accurate gauge the mood of 49 webcam feeds on one screen.**

In general, professors and educators have expressed unease and a lack of comfort with the new medium of lecturing, leading some to lecture to stuffed animals (https://i.imgur.com/bzmS2ls.jpg) just to have some sort of method of reading the room, no matter how inaccurate. **We wanted to do anything we could to help our professors and give them the tools to teach most comfortably and effectively.**

## What it does
With this in mind, we made Mood for Zoom, a Python program that deploys emotion recognition and **displays a live _ Mood Meter _ of the proportions of the class feeling angry, happy, surprised, sad, or neutral.** The data visualization is extremely compact and can easily fit in the corner of a screen, allowing a professor running a lecture over Zoom to glance at it periodically to have **a sense of the mood of the audience**. We also built an Arduino implementation of _ Mood Lighting _ which displays a **color-coded visualization through mini LED lights** of the classroom mood. This information helps professors to see when they should pause the lecture to allow for questions, speed up the lecture if students appear too bored, or throw in some humor to wake up sleepy Zoomers. 

In essence, Mood for Zoom "reads the room" for professors, **empowering them to lecture more naturally, adaptively, and impactfully.** 

## How we built it
The first part of our task involved going into Gallery View and building in the capability to **screenshot continuously throughout a Zoom call** to feed that information into our Google Vision API implementation. To do this, we used PyAutoGUI and wrote a program in Python to take screenshots and save them periodically. 

Next, we used Google Vision API to take in a picture, then **detect faces and store their emotions.** We then translated the Vision API's output, which rated each emotion from "very unlikely" to "very likely", into numerical data. This mostly involved successfully implementing the Vision API and reading the manuals to write a program fitting our specifications.

With these two parts in place, we used TkInter's visualization tools to generate the Mood Meter's visualization and update it in real time. We also used serial to send the data to arduino and implement Mood Lighting. 

## Challenges we ran into
Our original plan was to use the Zoom API, but we quickly realized it has no support for real-time access to webcams during a meeting, so we had to scrap that and move to workarounds. The problem was nontrivial to solve, and it took us some time to develop a complete mechanism for our solution. 

As we are all freshmen, many of us are beginner hackers and it was new ground to make anything new without starter code. The digital medium is also not as conducive to efficient working; while at most hackathons we would be together 24 hours a day, we had to coordinate schedules for it.

## Accomplishments that we're proud of
We were able to learn multiple new libraries of Python from nothing, and implement a cool use case of Google Cloud Vision API! In all, we are most proud of the chance to help our professors and educators; we really just want the chance to give back to those who have already given so much. 

## What we learned
We learned a lot about TkInter, PyAutoGUI, and Zoom. Again, since we are all beginner hackers, it was an exciting experience just to build something that works.

Even so, the real learning was the friends we made along the way <3

## What's next for Mood for Zoom
Google's emotion recognition only supports anger, joy, surprise, and sorrow; we would love to train a neural network to detect more classroom-relevant emotions like boredom, attentiveness, excitement, and more. More intuitive, scannable visualizations like heatmaps or word clouds are also in the pipeline. For our endgame, we want to fold our capabilities into a Zoom Marketplace app so that our universities can install it for our professors to use. We are thinking of using Google AppEngine for this implementation. 

Thank you so much for this exciting opportunity! We hope you have had a great weekend!
