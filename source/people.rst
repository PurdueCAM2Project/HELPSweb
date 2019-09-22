People and Topics
-----------------

2019 Fall Schedule
~~~~~~~~~~~~~~~~~~

All meetings are held in EE 013.

=========== ========== ============== ==================== ==============
Time        Monday     Tuesday        Wednesday            Friday
=========== ========== ============== ==================== ==============
11:00-12:00 Forest                    Software Engineering Image Database
12:30-13:30            Human Behavior
13:30-14:30 Drone                     Crowdsourcing        Embedded 2
14:30-15:30 Embedded 1
15:30-16:30 
17:30-18:20                           VIP lecture (EE 129)
=========== ========== ============== ==================== ==============

Due to the large number of team mebers, it is not possible changing
the regular meeting time. If your schedule does not fit into a
particular team, you have to move to another team.

Topics
~~~~~~

Forest Inventory Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^

Use computer vision to calculate the sizes of trees (called diameter
at breath height, or DBH), recognize the species of trees, and their
locations.  For Fall 2019, the team has two major goals: (1) handle
multiple trees in a single frame and (2) handle trees in a nautral
forest.

The following images show the result from a distance sensor and the tree image (before and after denoising).

|forest03| |forest04| |forest05|

.. |forest03| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/distanceimage01.png
   :width: 59%

	   
.. |forest04| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/treeimage02.png
   :width: 18%

	   
.. |forest05| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/treeimage01.png
   :width: 18%

The following images show how the team measures the diameter at breath height.

|forest00| |forest01| |forest02|


.. |forest00| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/measuretree01.jpeg
   :width: 35%

.. |forest01| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/measuretree02.jpeg
   :width: 20%

.. |forest02| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/measuretree03.jpeg
   :width: 35%

Readings for new members:

- `Forest Inventory and Analysis (FIA) Program of the U.S. Forest Service <https://www.fia.fs.fed.us/>`__

- `Forest Data Collection Using Terrestrial Image-Based Point Clouds From a Handheld Camera Compared to Terrestrial and Personal Laser Scanning <https://ieeexplore.ieee.org/abstract/document/7109840>`__

- `Estimation of Tree Stem Attributes Using Terrestrial Photogrammetry with a Camera Rig <https://www.mdpi.com/1999-4907/7/3/61>`__

- `Development and Testing of a New Ground Measurement Tool to Assist in Forest GIS Surveys <https://www.mdpi.com/1999-4907/10/8/643/htm>`__

----
	   
Analysis of Drone Video
^^^^^^^^^^^^^^^^^^^^^^^

This project creates computer vision solutions recognizing objects
captured by cameras mounted on drones.  In Fall 2019, the team will
create a set of video clips for the following purposes:

- Construct three-dimensional geometries of objects: The video clips
  will capture cardboard boxes of different sizes, together with a
  wide range of objects and several with known sizes.

- Detect and track multiple moving objects: The clips include moving
  objects.  The drone itself is also moving. The purpose is to
  correctly identify these objects and track their movements.

- Segmentation: Create pixel-wise labels of different objects.

- Re-identify people: Determine whether the same person has been
  before.

This project is supported by `NSF CNS-1925713 <https://www.nsf.gov/awardsearch/showAward?AWD_ID=1925713>`__

Readings for new members:

- `Vision Meets Drones: A Challenge <https://arxiv.org/pdf/1804.07437.pdf>`__

- `Context Encoding for Semantic Segmentation <http://openaccess.thecvf.com/content_cvpr_2018/papers/Zhang_Context_Encoding_for_CVPR_2018_paper.pdf>`__

- `Vehicle Re-identification in Aerial Imagery: Dataset and Approach <https://arxiv.org/pdf/1904.01400.pdf>`__

- `Airborne visual tracking and reidentification system <https://www.spiedigitallibrary.org/journalArticle/Download?fullDOI=10.1117/1.JEI.28.2.023003&casa_token=Rs6JtKyTL6cAAAAA:_5C4cfQ5XkKqoeFqiyXl7r-xNdDH27PTYeq52ag1Va8udjeU3ykDF2-6B082Fdqt9JQHioCPXjE>`__


----  

Embedded Vision 1
^^^^^^^^^^^^^^^^^

Recent progress in computer vision has focused primarily in
general-purpose object detection using datasets with many (hundreds)
categories of objects (such as humans, dogs, vehicles, furniture,
buildings, etc.).  For many applications, however, the number of
possible objects can be limited. For example, inside an airport
terminal, elephants or eagles are not expected. This project will use
**computer graphics** to synthesize images and videos of these
scenarios. The synthesized data is used to train computer vision
running on embedded systems (also called **edge devices**).  Doing so
can reduce network traffic and make the system more
scalable. Moreover, sensitive information (such as human faces) may be
detected and protected before the data leaves the cameras.

Readings for new members:

- `Playing for Data: Ground Truth from Computer Games <https://arxiv.org/pdf/1608.02192.pdf>`__

- `Sim4CV: A Photo-Realistic Simulator for Computer Vision Applications <https://link.springer.com/content/pdf/10.1007%2Fs11263-018-1073-7.pdf>`__

- `The ParallelEye Dataset: A Large Collection of Virtual Images for Traffic Vision Research <https://www.researchgate.net/profile/Fei_Yue_Wang/publication/334390716_The_ParallelEye_Dataset_A_Large_Collection_of_Virtual_Images_for_Traffic_Vision_Research/links/5d270204a6fdcc2462d490c9/The-ParallelEye-Dataset-A-Large-Collection-of-Virtual-Images-for-Traffic-Vision-Research.pdf>`__


Analyze Human Behavior in Video
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The purpose of this team is to use real-time video analytics to detect
dangerous behavior or safety violation in workplace (such as
factories), raise alerts to prevent injury, or provide post-event
analysis to prevent future occurrences. In Fall 2019, the team will
focus on solving these problems in an indoor
environment with multiple cameras:

- Where are the people (including re-identifying the same person in different cameras)?

- Where does each person face?

Readings

- `Person Re-identification by Local Maximal Occurrence Representation and Metric Learning <https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Liao_Person_Re-Identification_by_2015_CVPR_paper.pdf>`__

- `An Improved Deep Learning Architecture for Person Re-Identification <http://openaccess.thecvf.com/content_cvpr_2015/papers/Ahmed_An_Improved_Deep_2015_CVPR_paper.pdf>`__

- `MARS: A Video Benchmark for Large-Scale Person Re-Identification <https://www.researchgate.net/profile/Liang_Zheng17/publication/308277502_MARS_A_Video_Benchmark_for_Large-Scale_Person_Re-Identification/links/5a1272daa6fdccc2d79b6da3/MARS-A-Video-Benchmark-for-Large-Scale-Person-Re-Identification.pdf>`__

- `Harmonious Attention Network for Person Re-Identification <http://openaccess.thecvf.com/content_cvpr_2018/papers/Li_Harmonious_Attention_Network_CVPR_2018_paper.pdf>`__
  

----  

Software Engineering for Machine Learning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This project creates a process for developing **reproducible**
software used in machine learning. In Fall 2019, the team's focus is
to create tools that faciliate code review. The tools analyze the
histories of version control repositories and automatically identify
possible defects within a pull request. The tools will also collect
metrics relating to the code review.

Readings

- `Explainable Software Bot Contributions: Case Study of Automated Bug Fixes <https://arxiv.org/pdf/1905.02597.pdf>`__

- `Automated Code Review via Software Repository Mining  <https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8330261>`__

- `(Patent)Automated program code analysis and reporting <https://patentimages.storage.googleapis.com/2a/da/ad/e8fa817408f010/US20180275989A1.pdf>`__

- `Software Engineering for Machine Learning: Code Review <https://se4ml.org/software/chapter_cr.html>`__

----

Crowdsourcing
^^^^^^^^^^^^^

Computer vision is still not perfect and humans outperform computers
in many situations. This team builds computer tools (human interfaces)
for humans to identify unexpected properties (called "bias") in data
used to train computer programs. These tools are computer games and
the players (crowds) describe the characteristics in the data.

Reading for new members:

- `Unbiased look at dataset bias <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.944.9518&rep=rep1&type=pdf>`__

- `Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations <https://arxiv.org/abs/1602.07332>`__

- `VQA: Visual Question Answering <https://arxiv.org/abs/1505.00468>`__

- `Crowdsourcing in Computer Vision (Chapters 1 and 2) <https://drive.google.com/file/d/1vuTRkuU9DLPI4zJvAWqRrYX2R7PlWUtS/view>`__

- `Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification <http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf>`__

|crowdsource03| |crowdsource02|

|crowdsource05| |crowdsource04|



.. |crowdsource02| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/crowdsourceexample.png
   :width: 45%


.. |crowdsource03| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/crowdsourcehome.png
   :width: 45%

	   
.. |crowdsource04| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/crowdsourceteam.jpg
   :width: 45%

	   
.. |crowdsource05| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/crowdsourceposter.jpg
   :width: 45%

----

Image Database
^^^^^^^^^^^^^^

This system integrates computer vision and database.  After the
objects in images are detected, the information is stored in a
database so that it is searchable.  The team has built a prototype of
the system processing multiple video streams simultaneously. The team
will focus on improving the performance (scalability) for lower
latency as well as investigating new storage systems.

Reading for new members:

- `Recent Advances in Convolutional Neural Networks <https://arxiv.org/abs/1512.07108>`__

- `You Only Look Once: Unified, Real-Time Object Detection <https://arxiv.org/abs/1506.02640>`__

- `YOLOv3: An Incremental Improvement <https://arxiv.org/abs/1804.02767>`__

----

Embedded Vision 2
^^^^^^^^^^^^^^^^^

This project investigates computer vision solutions that can perform
the following tasks in an embedded computer (small enough to be inside
a typical camera)

- Obtain aggregate information (such as the number of people and their genders)

- Detect faces

- Encrypt the faces before sending the data to storage

The sensitive data (faces) never leaves the camera.  Only authorized
people with the decryption key can see the faces. The concept is
illustrated below.

|embeddedprivacy|



.. |embeddedprivacy| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/embeddedprivacy.png
   :width: 90%

Readings for new members:

- `An Improved Neural Network Cascade for Face Detection in Large Scene Surveillance <https://www.mdpi.com/2076-3417/8/11/2222/htm>`__

- `WIDER FACE: A Face Detection Benchmark  <http://shuoyang1213.me/WIDERFACE/>`__

- `Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks <https://arxiv.org/abs/1506.01497>`__

- `SSD: Single Shot MultiBox Detector <https://arxiv.org/abs/1512.02325>`__

- `Optimizing the Trade-off between Single-Stage and Two-Stage Object Detectors using Image Difficulty Prediction <https://arxiv.org/abs/1803.08707>`__

- `PyramidBox: A Context-assisted Single Shot Face Detector <https://arxiv.org/abs/1803.07737>`__

- `Real-Time Multi-Scale Face Detector on Embedded Devices <https://www.mdpi.com/1424-8220/19/9/2158/pdf>`__

  
----


	   
Faculty
~~~~~~~

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://ag.purdue.edu/ProfileImages/dbarbara.jpg
     - `David Michael Barbarash
       <https://ag.purdue.edu/hla/LA/Pages/Profile.aspx?strAlias=dbarbara&intDirDeptID=24>`__
       
       Landscape Architecture, Purdue
     - .. image:: https://engineering.purdue.edu/ResourceDB/ResourceFiles/image92690
     - `Dave Cappelleri
       <https://engineering.purdue.edu/ME/People/ptProfile?id=92669>`__
       
       Mechanical Engineering, Purdue
     
   * - .. image:: https://shuohanchen.files.wordpress.com/2019/02/shuohan-eps-converted-to.png?w=220&h=300
     - `Shuo-Han Chen
       <https://shuohanchen.com/>`__
       
       Institute of Information Science, Academia Sinica
     - .. image:: https://drive.google.com/uc?id=1EqxgXBuEQNiQ5pNVvg42AfWMFKByjKh1
     - `Yung-Hsiang Lu
       <https://engineering.purdue.edu/ECE/People/ptProfile?resource_id=3355>`__
       
       Electrical and Computer Engineering, Purdue

   * - .. image:: http://www.stat.purdue.edu/images/Faculty/thumbnail/varao-t.jpg
     - `Vinayak Rao
       <http://www.stat.purdue.edu/people/faculty/varao>`__
       
       Statistics, Purdue
     - .. image:: https://drive.google.com/uc?id=19_-2sKwLTcjoBvjclB8tqlIA56k5QwUq
     - `Guofan Shao
       <https://ag.purdue.edu/fnr/Pages/profile.aspx?strAlias=shao>`__
       
       Professor,  Forestry and Natural Resources, Purdue

   * - .. image:: https://avatars1.githubusercontent.com/u/651504?s=460&v=4
     - `George K. Thiruvathukal
       <https://thiruvathukal.com>`__
       
       Computer Science, Loyola University Chicago.
     - .. image:: http://www.stat.purdue.edu/~mdw/images/WardMFO.jpg
     - `Mark Daniel Ward
       <http://www.stat.purdue.edu/~mdw/>`__
       
       Statistics, Purdue

   * - .. image:: https://ag.purdue.edu/ProfileImages/woeste.jpg
     - `Keith E. Woeste
       <https://ag.purdue.edu/fnr/Pages/profile.aspx?strAlias=woeste>`__
       
       Forestry and Natural Resources, Purdue
     - .. image:: https://www.cs.purdue.edu/people/images/small/faculty/mingyin.jpg
     - `Ming Yin
       <https://www.cs.purdue.edu/people/mingyin>`__
       
       Computer Science, Purdue


Members
~~~~~~~

Graduate Students
^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 10 30

   * - .. image:: https://drive.google.com/uc?id=1YunKydNN7OS_vvBubbME4UykfjNh1CgA
     - Abhinav Goel: Doctoral Student, Improve Neural Networks' Energy Efficiency

   * - .. image:: https://drive.google.com/uc?id=1GzpDueX6W2e4sx0OGfKm51cru34jyEvp
     - Sara Aghajanzadeh: Master Student, Detect Faces and Protect Privacy 

   * - .. image:: https://drive.google.com/uc?id=1kIYIrkXnICIb2odq5WWGlsdCYv4fTpVU
     - Ryan Dailey: Master Student, Discover Network Cameras

Undergraduate Students and 2019 Summer Teams
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Image Database
##############

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://drive.google.com/uc?id=1RWw0U_QwKhY8ZioiPdDmlN2_VEros3Zt
     - `Shunqiao Huang`
       
       Leader
     - 
     - `Hojoung	Jang`

   * -
     - `Akshay Pawar`
     -
     - `Aditya Chakraborty`

   * -
     - `Lucas Wiles`
     -
     -
   

Embedded Vision 2
#######################

Identify the specific features (called distinctiveness) of
different visual dataset. Use one dataset with many labels to help
train machine models for another datasets with few labels.



.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://drive.google.com/uc?id=1yUr73JBTlTG0LMew8pqVXA5csNggmuOX
     - `Ashley Kim`
     - .. image:: https://drive.google.com/uc?id=1db-0VtllDb1sU5MeqnmOT9WKNMYsPy5z
     - `Li Yon Tan`

   * - .. image:: https://drive.google.com/uc?id=1RbbxJV5LEmUpPmfMcUU9V457Ww4wtN2t
     - `Isha Ghodgaonkar`
     - .. image:: https://drive.google.com/uc?id=1Y7Ew3_OUSKDagQ7nOkRKOpYV1DhrPdi7
     - `Fischer Bordwell`

   * - .. image:: https://drive.google.com/uc?id=1PoRMRN5OFqoEFkuTo5IBZ3F1P07qDYBr
     - `Kirthi Shankar Sivamani`
     -
     - `Shuhao Xing`

   * -
     - `Ziyad Alajmi`
     -
     - `Jackson Moffet`

   * -
     - `Arnav Ballani`
     - .. image:: https://drive.google.com/uc?id=1bRRgMDNL1GA8tofA1orS_T47dp-thl4A
     - `Chiche Tsai`

   * - .. image:: https://1drv.ms/u/s!AvvT9f1RiwGbgYh0Q1zOsl1NMMv6mA?e=UdP08H
     - `Caleb Tung`
     - .. image:: https://drive.google.com/uc?id=12g4phl1MKM0ajAALyiChi91guQAG9HtJ
     - `Ryan Dailey`

Crowdsourcing for Data Bias
###########################

Use crowd (i.e., humans) to identify unintentional biases in visual
datasets.


.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://drive.google.com/uc?id=1BgdG9XYcrmdMtdSbePpp324jwdnwl_7p
     - `Xiao Hu`
       
       Co-Leader
     -  .. image:: https://drive.google.com/uc?id=1t-krvZinKrSk1YT8MRl8R6xoPUHpF8H7
     - `Haobo Wang`

       Co-Leader

   * - .. image:: https://drive.google.com/uc?id=1GSO6wVspOBuu881yg-5Bg2E5xEA1gSMJ
     - `Kaiwen Yu`
     - .. image:: https://drive.google.com/uc?id=1u5dbejyw-62y5x6UPKEtPo3DFd4AtYCc
     - `Anirudh Vegesana`

   * -
     - `Somesh	Dube`
     -
     -
     

Forest Inventory
################

Use computer vision to calculate the sizes of trees
(called diameter at breath height, or DBH).


.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://drive.google.com/uc?id=1WrLZtXkzgHDQbCC0XLX92C8a8rgS6yMd
     - `Yezhi Shen`
     -
     - `Minh Luong Nguyen`

   * - .. image:: https://drive.google.com/uc?id=1GeeVgSnl4Fwf-rlIFlG5LuSohcMMIpTi
     - `Nick Eliopoulos`
     -
     - `Ya Ling Tsai`

   * -
     - `Carolyn Tustin`
     -
     - `Zoe Yang`

   * -
     - `David Jarufe`
     -
     -

Human Behavior
##############

Track human activities and understand how they use designed space.


.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://drive.google.com/uc?id=14FxQ_dr9836vXFBx1YknDQ0rn-QVZHWy
     - `Mohamad Alani`
     - .. image:: https://drive.google.com/uc?id=1bZxvHiZ-H7ACq55FpJQqbJgj8NZjZlcb
     - `Peter Huang`

   * -
     - `Dhruv Swarup`
     -
     - `Chau Minh Nguyen`
   
     
Alumni
~~~~~~

Video by Current and Former Members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


  .. raw:: html

    <iframe width="600" height = "400" src="https://www.youtube.com/embed/7Ao2zCYV9I8" frameborder="0" allowfullscreen></iframe>


  .. raw:: html

    <iframe width="600" height = "400" src="https://www.youtube.com/embed/1LGjSqQ953A" frameborder="0" allowfullscreen></iframe>

  .. raw:: html

    <iframe width="600" height = "400" src="https://www.youtube.com/embed/oPeKHUHpU2c" frameborder="0" allowfullscreen></iframe>

	   
    

