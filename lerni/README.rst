Lerni - learn everything reasonably, not irrationally
-----------------------------------------------------

Taking Learning How to Learn made me aware of many new (to me) learing strategies and tactics. Through this project, I hope to assemble the best of these to create a new learning system.


Review of Previous Work
-----------------------

Hypercard
	perhaps the seminal work, primitive by today's standards, but it was good for its time.

Supermemo
	the first (that I know of) flashcard program that used spaced repetition. supermemo.com presents a lot of useful research.

Anki
	an opensource replacement?? for supermemo. quite mature and flexible, but in need of refactoring to grow beyond a flash-card program. Useful as is in a larger system.

Mnemosyne
	similiar to Anki, with a better interface, but less flexible. publishing anonymous statistics is an interesting idea. I want to look at the data.

edX
	an opensource platform for creating courses.

Coursera
	is coursera's platform open?

Udacity
	I think Udacity has the best UI of the BigThree. Is it open?

Kahn Academy
	very good testing component. presentation limited.


Epub
	would it be possible to package an entire course, including video and flashcards into a .epub container?

Rationale and System Analysis
-----------------------------


Goals and Objectives
--------------------


Guiding Principles
------------------

Start with these: 

    * It should run on a stock (no developer mode hacking) Chromebook. 
    * It should be reasonably simple to use productively without a network connection.
      Why: To me, the main reason for using a Chromebook is portability, and if you need a WIFI connection to study, you are limiting your location options.
      - be able to download most of a "module" in one action
      - transparently use this cached version whenever it is available
      - maintain usage data while offline for synchronizing when online.
    * It should record a lot of data about study events, in particular:
        - what activities were done, when, in what order, how much time was spent
        - what resources were accessed during the activities
    * This data should be used to improve the course, not to reward or punish students.
    * The learning process is collaborative: for a MOOC to be open should mean that any of the students should be free to become an author. Maintaining the course on Github seems to be a good way to accomplish this.
    * Because of "Do less" below, a "course" in this system is really metadata to package existing resources. If a course already exists on Coursera, edX, YouTube etc., do not reinvent it, reference it and integrate it into your materials.
    
Add the following:
  https://gist.github.com/adamwiggins/5687294

