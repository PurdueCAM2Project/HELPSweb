People and Topics
-----------------

|cam2logo|

.. |cam2logo| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/cam2logo4v2.jpg
   :width: 100%

These projects form the CAM2 (Continuous Analysis of Many CAMeras) family.	   


2020 Spring Schedule
~~~~~~~~~~~~~~~~~~~~

All meetings are held in EE 013.

=========== ========== ==================== ==================== 
Time        Monday     Tuesday              Wednesday            
=========== ========== ==================== ==================== 
09:00-10:00            
10:00-11:00            Software Engineering 
11:00-12:00 
12:30-13:30 Forest     
13:30-14:30 Drone                           Human Behavior        
14:30-15:30 Embedded 1                      Crowdsourcing
15:30-16:30 Leaders
16:30-17:30                                 Embedded 2
17:30-18:20                                 VIP lecture (EE 129)
=========== ========== ==================== ==================== 

Due to the large number of team mebers, it is not possible changing
the regular meeting time. If your schedule does not fit into a
particular team, you have to move to another team.


Topics
~~~~~~

Low-Power Computer Vision
^^^^^^^^^^^^^^^^^^^^^^^^^

Many applications of computer vision runs on battery-powered systems,
susch as mobile phones, drones, IoT (Internet of Things), and edge
devices.  This project investigates how to reduce the energy
consumption of computer vision.  The project uses many methods to achieve
better energy efficiency, such as

- Restructure neural networks. Commonly adopted neural networks are
  large complex models. Many connections among neurons, however, are
  not necessary and can be removed. By restructuring the networks, it
  is possible avoiding large amounts of compuation and save energy.

- Reduce the input space. Many machine learning models are designed
  for general purposes and can recognize objects of hundreds of
  classes.  Many applications, however, have only a few classes of
  objects. For example, it is not possible seeing an elephant in a
  classroom. Thus, the machine models do not have to detect elephants.

- Utilize hardware features. Transform the mathematical equations for
  machine models in order to map to hardware features (such as memory
  hierarchies) efficiently.


This project is supported by Facebook, Google, and Xilinx.  

Readings for new members:

- `Low-Power Computer Vision: Status, Challenges, Opportunities <https://engineering.purdue.edu/HELPS/Publications/papers/2019JESTCS.pdf>`__

- `Three Years of Low-Power Image Recognition Challenge: Introduction to Special Session <https://engineering.purdue.edu/HELPS/Publications/papers/2018DATEGauen>`__
  
	   
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

- `The ParallelEye Dataset: A Large Collection of Virtual Images for Traffic Vision Research <https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8451919>`__


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


Forest Inventory Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^

Forest inventory analysis is time consuming and expensive to do manually. The team is researching the use of stereo cameras and video footage to obtain individual tree information efficiently and at a low cost. Our goals this semester are as follows:
- Generate a 3D reconstruction of a forest plot from video footage
- Uniquely identify each tree in the 3D reconstruction with a diameter. 
- Compute the taper of a tree using stereo video
- Compute the crown height of a tree using stereo video

The following images show the result from a distance sensor and the tree image (before and after denoising).

|forest03| |forest04| |forest05|

.. |forest03| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/distanceimage01.png
   :width: 59%

	   
.. |forest04| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/treeimage02.png
   :width: 18%

   
.. |forest05| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/treeimage01.png
   :width: 18%

The following images are snapshots of 3D digital reconstructions of trees from video.

|forest06|

.. |forest06| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/martell_pointcloud_snap_annotated.png
   :width: 100%


Readings for new members:

- `Forest Inventory and Analysis (FIA) Program of the U.S. Forest Service <https://www.fia.fs.fed.us/>`__

- `Forest Data Collection Using Terrestrial Image-Based Point Clouds From a Handheld Camera Compared to Terrestrial and Personal Laser Scanning <https://ieeexplore.ieee.org/abstract/document/7109840>`__

- `Estimation of Tree Stem Attributes Using Terrestrial Photogrammetry with a Camera Rig <https://www.mdpi.com/1999-4907/7/3/61>`__

- `Development and Testing of a New Ground Measurement Tool to Assist in Forest GIS Surveys <https://www.mdpi.com/1999-4907/10/8/643/htm>`__

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

Crowdsourcing utilizes the knowledge of humans to complete a task. In the scope of research, we are using the crowd to handle specific tasks that may be hard for a machine to do or improve the work of a machine. This may include tasks such as detecting bias within image datasets using human knowledge rather than machines, since humans are better at distinguishing features within images. This semester, we are utilizing crowdsourcing to help select the most suitable machine model to use for unsupervised domain adaptation. We use the crowd to classify images to datasets and generate a confusion matrix detailing the similarity of images across several datasets.

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

   * - .. image:: https://drive.google.com/uc?id=1rtNrB-sPUJ6gllceGkgXex4gH11xZBmu
     - Caleb Tung: Doctoral Student, Using Contextual Information from Network Cameras to Improve and Evaluate Computer Vision Solutions

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/shreya_ghosh.jpg
     - Shreya Ghosh: Master Student, Data-Driven Civil Infrastructure Decision Making for Improved Citizen Safety, Accessibility, and Economic Opportunity


Undergraduate Students and 2019 Fall Teams
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Image Database - Suspended for Spring 2020
##########################################

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_male.jpg
     - `Sripath Mishra`

     - .. image:: https://drive.google.com/uc?id=1TfZn-I0Mk_lvY-cMontY8f1u9o5Zvc-y
     - `Akshay Pawar`

   
Drone Video
###########

Create datasets of drone video, recognize objects, estimate the sizes.


.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://i.ibb.co/4SB910F/20190617-180018.jpg
     - `Avanish Subbiah`

       Leader

     - .. image:: https://drive.google.com/uc?id=1BgdG9XYcrmdMtdSbePpp324jwdnwl_7p
     - `Xiao Hu`

       Co-leader

   * - .. image:: https://drive.google.com/uc?id=1Yv1UB8v2LEjDsRCaCDilNzI68hoDAOXf
     - `Katherine Sandys`

     - .. image:: https://i.imgur.com/c2lePxA.jpg
     - `Justin Qualley`

   * - .. image:: https://drive.google.com/uc?id=1M3PTWnGPrRkv2ntr_Furr-gh1VezKSL_
     - `Victor Oduduabasi`

     - .. image:: https://drive.google.com/uc?id=1t-krvZinKrSk1YT8MRl8R6xoPUHpF8H7
     - `Haobo Wang`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_male.jpg
     - `Nathan Gizaw`

     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_male.jpg
     - `Karthik Maiya`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_male.jpg
     - `Rushabh Ramesh Ranka`

     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_tuhin_sarkar.jpg
     - `Tuhin Sarkar`

   * - .. image:: https://drive.google.com/uc?id=1YunKydNN7OS_vvBubbME4UykfjNh1CgA
     - `Abhinav Goel`

     -
     -


Embedded Vision 1
#################

Detect and encrypt faces to protect privacy using embedded computer.


.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_vaastav_arora.jpg
     - `Vaastav Arora`

       Leader
     - .. image:: https://drive.google.com/uc?id=1RUriBMS5XchLbjWiRWTwOO2XHCpCrf1R
     - `Siddharth Srinivasan`

       Co-leader

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_rufat_imanov.jpeg
     - `Rufat Imanov`

     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_female.jpg
     - `Asa Cutler`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_xin_wang.jpeg
     - `Xin Wang`

     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_xin_du.jpeg
     - `Xin Du`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_male.jpg
     - `Seyram Samuel Mortoti`

     -
     -

   
Embedded Vision 2
#################

Identify the specific features (called distinctiveness) of
different visual dataset. Use one dataset with many labels to help
train machine models for another datasets with few labels.

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://drive.google.com/uc?id=1db-0VtllDb1sU5MeqnmOT9WKNMYsPy5z
     - `Li Yon Tan`

       Leader

     - .. image:: https://drive.google.com/uc?id=1RbbxJV5LEmUpPmfMcUU9V457Ww4wtN2t
     - `Isha Ghodgaonkar`

       Co-leader

   * - .. image:: https://drive.google.com/uc?id=1TfZn-I0Mk_lvY-cMontY8f1u9o5Zvc-y
     - `Akshay Pawar`
     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_female.jpg
     - `Damini Rijhwani`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_male.jpg
     - `Hojoung Jang`
     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_male.jpg
     - `Aditya Chakraborty`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_female.jpg
     - `Shristi Saraff`
     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_female.jpg
     - `Meenakshi Pavithran`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_male.jpg
     - `Zach Berg`

     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_jackson_moffet.jpg
     - `Jackson Moffet`

   * - .. image:: https://drive.google.com/uc?id=1rtNrB-sPUJ6gllceGkgXex4gH11xZBmu
     - `Caleb Tung`

       Doctoral Student

     -
     -
   
Crowdsourcing for Data Bias
###########################

Use crowdsourcing to identify unintended bias in visual data and label data.


.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_gore_kao.jpg
     - `Gore Kao`

       Leader

     - .. image:: https://drive.google.com/uc?id=1Pik3biv3epBSKMobHHiqH8FcG9679ZSu
     - `Kaiwen Yu`
       Co-leader

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_female.jpg
     - `Yukyung Lee`
     - .. image:: https://drive.google.com/uc?id=1t-krvZinKrSk1YT8MRl8R6xoPUHpF8H7
     - `Haobo Wang`

   * - .. image:: https://drive.google.com/uc?id=1BgdG9XYcrmdMtdSbePpp324jwdnwl_7p
     - `Xiao Hu`

       CAM² Co-leader

     - .. image:: https://drive.google.com/uc?id=1u5dbejyw-62y5x6UPKEtPo3DFd4AtYCc
     - `Anirudh Vegesana`

   * - .. image:: https://drive.google.com/uc?id=1yUr73JBTlTG0LMew8pqVXA5csNggmuOX
     - `Ashley Kim`
     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_esteban_gorostiaga.png
     - `Esteban Gorostiaga`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_male.jpg
     - `Phillip Andrew Archuleta` 
     - .. image:: https://drive.google.com/uc?id=1Y7Ew3_OUSKDagQ7nOkRKOpYV1DhrPdi7
     - `Fischer Bordwell`
	 
   * - .. image:: https://www.cs.purdue.edu/people/images/small/faculty/mingyin.jpg
     - `Ming Yin`

       Advisor
	   
     - 
     -
   
Forest Inventory
################

Use computer vision to recognize tree species and estimate their sizes.


.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://i.ibb.co/y5GW8Hk/Selfie-2.jpg
     - `David Jarufe`
     
       Leader

     - .. image:: https://drive.google.com/uc?id=1WrLZtXkzgHDQbCC0XLX92C8a8rgS6yMd
     - `Yezhi Shen`

       CAM² Leader

   * - .. image:: https://drive.google.com/uc?id=1GeeVgSnl4Fwf-rlIFlG5LuSohcMMIpTi
     - `Nick Eliopoulos`

       CAM² Co-leader
     - .. image:: https://i.ibb.co/Jxfdyb8/IMG-9250.jpg
     - `Ya Ling Tsai`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_justin_hsiung.png
     - `Yi-Fang Hsiung`

     -
     -

Human Behavior in Video
#######################

Understand human behavior and obtain aggregate information from video.


.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://drive.google.com/uc?id=15MjIOEr5k1XvctTmnAM3yzy3JduC0MJm
     - `Taher Dohadwala`

       Leader

     - .. image:: https://avatars3.githubusercontent.com/u/20303922?s=460&v=4
     - `Moiz Rasheed`

       Co-leader

   * - .. image:: https://drive.google.com/uc?id=1wzCPewNOxMyl3QBXAuwVUN_jeLqL8hnK
     - `Wenxi Zhang`

     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_ethan_glaser.png
     - `Ethan Glaser`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_nour_hendy.jpeg
     - `Noureldin Hendy`
     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_siddhartha_kumar.jpg
     - `Siddhartha Kumar Senthil Kumar`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_mert_zamir.jpg
     - `Mert Zamir`

     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_male.jpg
     - `Tong Wang`

   * - .. image:: https://ag.purdue.edu/ProfileImages/dbarbara.jpg
     - `David Michael Barbarash`
	 
       Advisor

     - .. image:: image:: https://drive.google.com/uc?id=1GzpDueX6W2e4sx0OGfKm51cru34jyEvp
     - `Sara Aghajanzadeh`
	 
       Masters Student
       
   
Software Engineering
#######################

Create procedure for developing high-quality and reproducible software.


.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_akhil_channakotla.jpg
     - `Akhil Chinnakotla`

       Leader

     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_connor_chadwick.jpg
     - `Connor Chadwick`

   * - .. image:: https://i.postimg.cc/VkM4Gjjj/ezgif-com-crop.jpg
     - `Ryan Firestone`
     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_stephen_davis.jpg
     - `Stephen Davis`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_seoyoung_lee.jpg
     - `Seoyoung Lee`
     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_amogh_shanbag.jpg
     - `Amogh Shanbag`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_ryan_chen.jpg
     - `Ryan Chen`
     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_male.jpg
     - `Ved Dave`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_jack_lecroy.jpg
     - `Jack LeCroy`
     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_rohit_tokala.jpg
     - `Rohit Reddy Tokala`

   * - .. image:: https://drive.google.com/uc?id=1p5Ad8doE42SN57LXYTdsDtKOjmgGbPfG
     - `Noah Curran`
     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_vishnu_banna.jpeg
     - `Vishnu Banna`
     
   * - .. image:: https://avatars1.githubusercontent.com/u/651504?s=460&v=4
     - `George K. Thiruvathukal`

       Advisor

     -
     -
     
   
     
Alumni
~~~~~~

.. list-table::
   :widths: 20 20 20

   * - Achinthya Soordelu
     - James Lee
     - He Li
   * - Anthony Fennell
     - Jenil Patel
     - Ehren Marschall
   * - Fengjian Pan
     - Nirmal Asokan
     - Sanghyun Cho
   * - Shengli Sui
     - Woojin Kim
     - Ajay Gopakumar
   * - Jiancheng Wang
     - Sitian Lu
     - Juncheng Tang
   * - Milos Malesevic
     - Mina Guo
     - Hanyang Liu
   * - Zhenming Zhang
     - Zaiwei Zhang
     - Jiaju Yue
   * - Huanyi Guo
     - Jeanne Deng
     - Zhenming Zhao
   * - Anthony Kang
     - Qingshuang Chen
     - Yuhao Chen
   * - Borui Chen
     - Sriram Rangaramanujan
     - James Tay
   * - Kyle Mcnulty
     - Seth Bontrager
     - Pranjit Kalita
   * - Subhav Ramachandran
     - Everett Berry
     - Erik Rozolis
   * - Bolun Zhang
     - Andrew Green
     - Yukun An
   * - Daniel Dilger
     - Yexin Wang
     - Zhifan Zeng
   * - Joseph Sweeney
     - Ryan Schlueter
     - John Laiman
   * - Jay Patel
     - Yutong Huang
     - Yuxiang Zi
   * - Zhanxiang Hua
     - Weizhi Li
     - Yash Pundlik
   * - Ramyak Singh
     - Nanxin Jin
     - Kyle Martin
   * - Hao Zou
     - Sam Yellin
     - Wenzhong Duan
   * - Aparna Pidaparthi
     - Changyu Li
     - Deepika Aggrawal
   * - Hanwen Huang
     - Hussni Mohd Zakir
     - Sihao Yin
   * - Weiqing Huang
     - Christopher Jovanovic
     - Ahmed Kaseb
   * - Wengyan Chan
     - Meera Haridasa
     - Deeptanshu Malik
   * - Vadim Nikiforov
     - Matthew Fitzgerald
     - Youngsol Koh
   * - Mehmet Alp Aysan
     - Cailey Farrell
     - Yifan Li
   * - Lucas Neumann
     - Robert Gitau
     - Zhi Kai Tan
   * - Spencer Huston
     - Mohamad Alani
     - Lucas Wiles
   * - Yuxin Zhang
     - Chau Minh Nguyen
     - Shunqiao Huang
   * - Minh Nguyen
     - Dhruv Swarup
     - Ryan Dailey

Video by Current and Former Members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


  .. raw:: html

    <iframe width="600" height = "400" src="https://www.youtube.com/embed/7Ao2zCYV9I8" frameborder="0" allowfullscreen></iframe>


  .. raw:: html

    <iframe width="600" height = "400" src="https://www.youtube.com/embed/1LGjSqQ953A" frameborder="0" allowfullscreen></iframe>

  .. raw:: html

    <iframe width="600" height = "400" src="https://www.youtube.com/embed/oPeKHUHpU2c" frameborder="0" allowfullscreen></iframe>

	   
    

