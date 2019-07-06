Progress Reports
-----------------

This is `the template <https://engineering.purdue.edu/HELPS/Management/progress.pptx>`__ for progress reports.

Four Essential Elements in Progress Reports

- What problem you are solving?
- Why are you solving this problem? How is it relevant to the team's purpose?
- What have you done? What is the result? What is the evidence?
- Why do you do it this way?

You need to provide details. Use figures, drawings, photos, equations, screenshots, source code ... to explain.

Honesty, Integrity, and Trust
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Honesty, integrity, and trust are the foundation of research. Never lie. Never fake data.

It is understandable that you encounter problems that are harder than expected. It is understandable that your other commitment may prevent you from making enough progress. It is understandable that unexpected things happen. Be honest. If you have not made progress, tell the truth. If something does not work, explain what happens. 

Common Mistakes
~~~~~~~~~~~~~~~~

The undergraduate program at Purdues does not require research. Hence, you should join a research team only if you want to solve research programs. You need to make progress in solving research problems. 

One of the most difficult parts of being a beginning researcher is to understand how progress is measured. Let's first review what students typically do in classrooms: attend lectures, take notes, submit homework assignments, answer exam questions. In many (probably most) cases, all students in the same classes have the same homework assignments and the same exam questions. This is the source of a lot of confusion for many students: they think everyone in the world is solving exactly the same problem described in the homework or the exams. The implication is that many students deeply believe that everyone in the world is solving exactly the same problem. Everyone knows the problem. Everyone has read the same textbooks. Everyone has seen the same exam questions. Also, professors are supposed to know the answers because professors write the homework assignments and the exam questions. 

No organization will put 100 people sitting together solving the same problem and the answer is already known by the "instructor". 

In many cases, students can get good grades without speaking a word in class. In fact, some students think speaking (asking questions or answering questions) disrupt lectures and should be discouraged.

"Classroom environment is not real." Please read it 10 times and understand the implications. 

Many students never realize that classroom environment is not real. Many students would be completely surprised that other people solve different problems and that professors do not have answers ready for research problems.

If you are in a research team, you must become an expert in the problem you are solving and nobody else should know as much as you do. If someone else knows as much as you (or more than you), by definition, you are unnecessary and should solve a different problem.

Good Progress Presentations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Here is a list of suggestions about giving good presentations:
- Know the audience.
- Practice. Make sure all content can be explained clearly. The connections among different materials need to be logic and smooth.
- Meaure time. A speech should uses approximatley 80% total time and leave 20% for QA. If the presentation is 15 minutes, speak for 12 minutes and leave 3 minutes for QA. 
- Start with a clear title and your name. The title should be the problem you are solving.
- Explain details. You must be an expert in solving the specific problems. Provide details so that others can learn from you.
- Use visual aids effectively. Use figures, drawings, photos, equations, screenshots, source code ... to explain. DO NOT USE A LOT OF WORDS.
- Remove all irrelevant decoration (anything that is irrelevant to the research problem or your contributions). 

Poster Examples
~~~~~~~~~~~~~~~~~~~

`example 1 <https://engineering.purdue.edu/HELPS/Management/poster1.pptx>`__


`Checklist <https://docs.google.com/document/d/12ecufv-G6tC-hanfg0Gwb 
i02lBDuNEkNWO0wZFm5DCM/edit?usp=sharing>`__\ \ of
skills needed for new members.


Set up Development Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is recommended that you create a Linux virtual machine for the
development environment. A virtual machine allows you to experiment
different settings (such as different versions of software packages)  
without affecting your real machine. You have several options for
creating virtual machines. One of them
is\ \ `Virtualbox <https://www.virtualbox.org/>`__\ \ . It supports
Windows, Mac, and Linux.

 
Learn git
~~~~~~~~~~~~~

A new member needs to learn many tools for communication and
collaboration. One of the most important is git and the GitHub platform.
 
#. Please create an account in github. Your account should include
   your first name and last name (no exception).

#. Upload your photograph to github.

#. Do not create any funny namethat is different from your real name. 
   This is a large team and nobody has time connecting a funny
   account name with the real person.

See https://guides.github.com/.
 
.. todo:: George, add info on distributed workflows.

Please understand how to use branches and merge correctly. There are  
three types of branches

#. Master branch. It is used to release software. It should be the
   most stable version.

#. Development branch: It should contain everything in the master
   branch and additional features. It should be usually stable. This  
   branch serves as the staging area for integration tests. This
   branch should not be too far ahead of the master branch. After a
   (or a few) feature is added and tested, this branch and the master 
   branch should merge and the new feature (or features) should be
   released.

#. Feature branches: These branches are created to adding new
   features. Each feature branch should have a short life-span: a
   branch is created for a feature, the feature is tested, and then
   the branch is merged into the development branch.

Please understand that the purposes of the branches are to stage
changes into the master branch. Each branch should last only a few
days. A common problem among students is that they do not merge
quickly. As time passes, the differences among branches become
greater and the chances of merge conflict increase. If a branch is
not merged within two weeks, the branch may have too many conflicts
and cannot be merged. As a result, the branch has to be abandoned and 
all efforts making that branch is lost.

 
Learn Python
~~~~~~~~~~~~~~~

You can find many tutorials online. This is\ \ `an
example <https://docs.python.org/3/tutorial/>`__\ \ . If you want
practice problems, Consider to solve\ \ `these
problems <https://github.com/yunghsianglu/IntermediateCProgramming>`_ 
_\ \ using
Python. If you want to understand objects, please watch\ \ `my
lectures for ECE
30862 <https://engineering.purdue.edu/OOSD/F2009/Lectures/lecture.htm 
l>`__\ \ (called
ECE 462 earlier).

Learn OpenCV (for Image Team)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
If you are in the image team, please
learn\ \ `OpenCV <http://docs.opencv.org/2.4/doc/tutorials/tutorials. 
html>`__\ \ .


Teamwork
--------
 

One of the most important difference between doing class homework and 
research is the need of “team thinking”. You are part of a team and
your must contribute to the team. Many students make significant
progress in their computers but they do not share what they have done 
with the team. As a result, whatever they have done is restricted to  
themselves.

What does it mean sharing work with the team? At the minimum, each
member should document contributions

Document Your Work
~~~~~~~~~~~~~~~~~~~~~~
 
You need to clearly document everything you want to do, you have
done, and the results. One of the most common mistakes when students  
start doing research is that “student thinking”: as long as I have
learned, I don’t need to document. This is wrong.

You are responsible explaining to the other group members that you
are doing. Your document must provide enough details so thatother
people can reproduce your work.

Sample Interview Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Joining Yung-Hsiang Lu’s research group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
Dr. Lu’s research is computer systems. He does not conduct research
in the following topics: device physics, laser, optics, electric
motor, hybrid vehicles, renewable energy, mix-signal circuits, and
many other topics. Reading his recent papers (at least the titles) is 
a good way to understand his research topics. Students in his group
should have good programming skills. The following are sample
questions for interviews to join his research group.

These interview questions emphasize understanding, thinking, and
creativity,not memorization. “Why” is much more important than “what” 
and “how”.  If you do not know the answers, explain how you would
find the answers.

 
Communication and Team Interaction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 
Do you understand that participation in discussion is extremely
important in a research project?

 

When you do not understand the content of a discussion, do you ask
questions or keep quiet? If you prefer silence, you are not ready to  
join a research project.

 


Project Management and Team
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Describe the tools, procedures, and methodologies you use for project 
management

