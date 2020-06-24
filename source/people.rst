People and Topics
-----------------
|cam2logo|

.. |cam2logo| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/cam2logo4v2.jpg
   :width: 100%

These projects form the CAM2 (Continuous Analysis of Many CAMeras) family.	   


2020 Summer Schedule
~~~~~~~~~~~~~~~~~~~~

All meetings are held online

=========== ================ ==================== ==================== ============
Time        Monday           Tuesday              Wednesday            Thursday
=========== ================ ==================== ==================== ============
09:00-10:00            
10:00-11:00 Human Behavior                        Human Behavior                           
11:00-12:00 Forest Inventory Embedded             Forest Inventory     Embedded 
12:00-13:00 
13:00-14:00 Crowdsourcing                         Crowdsourcing    
14:00-15:00 COVID-19         Drone Video          COVID-19             Drone Video                                  
15:00-16:00 Solar Sail                            Solar Sail
=========== ================ ==================== ==================== ============

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

Video Synthesis for Machine Learning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


Embedded Computer Vision
^^^^^^^^^^^^^^^^^^^^^^^^

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

   * - .. image:: https://www.stat.purdue.edu/images/Faculty/thumbnail/varao-t.jpg
     - `Vinayak Rao
       <https://www.stat.purdue.edu/people/faculty/varao>`__
       
       Statistics, Purdue
     - .. image:: https://drive.google.com/uc?id=19_-2sKwLTcjoBvjclB8tqlIA56k5QwUq
     - `Guofan Shao
       <https://ag.purdue.edu/fnr/Pages/profile.aspx?strAlias=shao>`__
       
       Professor,  Forestry and Natural Resources, Purdue

   * - .. image:: https://avatars1.githubusercontent.com/u/651504?s=460&v=4
     - `George K. Thiruvathukal
       <https://thiruvathukal.com>`__
       
       Computer Science, Loyola University Chicago.
     - .. image:: https://www.stat.purdue.edu/~mdw/images/WardMFO.jpg
     - `Mark Daniel Ward
       <https://www.stat.purdue.edu/~mdw/>`__
       
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


Undergraduate Students and Spring 2020 Teams
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   
Drone Video
###########

Create datasets of drone video, recognize objects, estimate the sizes.

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://drive.google.com/uc?id=1t-krvZinKrSk1YT8MRl8R6xoPUHpF8H7
     - `Haobo Wang`

        Leader
        Master

     - .. image:: https://drive.google.com/uc?id=1u5dbejyw-62y5x6UPKEtPo3DFd4AtYCc
     - `Anirudh Vegesana`

        Co-Leader

   * - .. image:: https://drive.google.com/uc?id=1BgdG9XYcrmdMtdSbePpp324jwdnwl_7p
     - `Xiao Hu`

        Master

     - .. image:: https://drive.google.com/uc?id=1RoEXTToeSx6yn4KfBGmXzAUTHW7O2tPS
     - `Nathan Gizaw`

        Graduate

   * - .. image:: https://drive.google.com/uc?id=13mtPxKNpSsbJYCq5z5U62GhrXdVXCUTd
     - `Jakob Harbers`

     - .. image:: https://drive.google.com/uc?id=1nIcAJM1CZ4VU0qgI4w0NpqRacCVnjlrL
     - `Qisen Ma`

   * - .. image:: https://drive.google.com/uc?id=19oIMMFOpQRUFNTuAb01PK_iLI1MQGuBq
     - `Russell Kim`

     - .. image:: https://drive.google.com/uc?id=1IfOXCEkFi3uSJK7rl9PO91wVdXSsYmTJ
     - `Trang (Rosie) Tran`

   * - .. image:: https://drive.google.com/uc?id=1lQXqYyzSJG3QxB8QE9EyDFLoIab8hgnX
     - `Qingyang Wang`

     - .. image:: https://drive.google.com/uc?id=1rk2DaPYBCpzBtOXgVMebUwmsrVddEcoh
     - `Wei Zakharov`

        Advisor


COVID-19
########

Analyze how crowd densities change in public places over time and due to government policies.

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://drive.google.com/uc?id=1RbbxJV5LEmUpPmfMcUU9V457Ww4wtN2t
     - `Isha Ghodgaonkar`

        CAM2 Leader

     - .. image:: https://drive.google.com/uc?id=1Y7Ew3_OUSKDagQ7nOkRKOpYV1DhrPdi7
     - `Fischer Bordwell`

        CAM2 Leader

   * - .. image:: https://drive.google.com/uc?id=1GqIgrombZqfiDhKiFHxKOu9GI4p02TlZ
     - `Mohammed Metwaly`

     - .. image:: https://drive.google.com/uc?id=16PmmIiHYpsMgD3nQEHKX2b2Jt07YOXTx
     - `Subhankar Chakraborty`

   * - .. image:: https://drive.google.com/uc?id=1qX7mOj6Cqhl7DhEap_8_VL028wbWlKmu
     - `Shane Allcroft`

     - .. image:: https://drive.google.com/uc?id=1Khq96EPWqdhb-3XlHDISqUSTFv8q_3TV
     - `Minghao Xue`

   * - .. image:: https://drive.google.com/uc?id=11_CQi-ZKxdAkc75aGd7KWCHzWqOG7SYn
     - `Kohsuke Kimura`

     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_vishnu_banna.jpeg
     - `Vishnu Banna`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_akhil_channakotla.jpg
     - `Akhil Chinnakotla`

     - .. image:: https://drive.google.com/uc?id=1MkJ737PpaPNk0K2V7H6baMLlGC0D3Jey
     - `XinXin (Ellen) Zhao`

   * - .. image:: https://drive.google.com/uc?id=1YunKydNN7OS_vvBubbME4UykfjNh1CgA
     - `Abhinav Goel`

        Doctoral

     - .. image:: https://avatars1.githubusercontent.com/u/651504?s=460&v=4
     - `George K. Thiruvathukal`

        Advisor

   * - .. image:: https://drive.google.com/uc?id=1rk2DaPYBCpzBtOXgVMebUwmsrVddEcoh
     - `Wei Zakharov`

        Advisor

     -
     -

   
Embedded Computer Vision
########################

Identify the specific features (called distinctiveness) of
different visual dataset. Use one dataset with many labels to help
train machine models for another datasets with few labels.

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_aditya_chakraborty.jpeg
     - `Aditya Chakraborty`

        Leader

     - .. image:: https://drive.google.com/uc?id=1TfZn-I0Mk_lvY-cMontY8f1u9o5Zvc-y
     - `Akshay Pawar`

        Co-Leader

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_zach_berg.jpg
     - `Zachery Peter Berg`

     - .. image:: https://drive.google.com/uc?id=12rvFZU_tTlGv1j80rsu-qzNliHma_ePJ
     - `Somesh Dube`

   * - .. image:: https://drive.google.com/uc?id=1cfTeOiESJLqN_OjClZoGAP3eQd78ZH1F
     - `Christopher D. Trippel`

     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_seoyoung_lee.jpg
     - `Seoyoung Lee`

   * - .. image:: https://drive.google.com/uc?id=1_r0Pc1UDKx5WCqPAKX3sUq-xRWuKXFu8
     - `Jason Bagnara`

     - .. image:: https://drive.google.com/uc?id=1rtNrB-sPUJ6gllceGkgXex4gH11xZBmu
     - `Caleb Tung`

        Doctoral
   
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

        Co-Leader

   * - .. image:: https://drive.google.com/uc?id=1u5dbejyw-62y5x6UPKEtPo3DFd4AtYCc
     - `Anirudh Vegesana`

     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_esteban_gorostiaga.png
     - `Esteban Gorostiaga`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_phillip_archuleta.jpeg
     - `Phillip Andrew Archuleta`

     - .. image:: https://drive.google.com/uc?id=1BgdG9XYcrmdMtdSbePpp324jwdnwl_7p
     - `Xiao Hu`

        Master

   * - .. image:: https://drive.google.com/uc?id=1t-krvZinKrSk1YT8MRl8R6xoPUHpF8H7
     - `Haobo Wang`

        Master

     - .. image:: https://drive.google.com/uc?id=1wkP5v4eNjSN7mMAv-ic4uPZMCXIrlevF
     - `Tianhui Chen`

   * - .. image:: https://drive.google.com/uc?id=1i9ugADcOvo2qYEj1_EbYGjH9cuP3YAqM
     - `Moya Zhu`

     - .. image:: https://drive.google.com/uc?id=1_ecXQKrjpla0Uh449IqZTwlRWK6um7oo
     - `Weiyan Hu`

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

   * - .. image:: https://drive.google.com/uc?id=1GeeVgSnl4Fwf-rlIFlG5LuSohcMMIpTi
     - `Nick Eliopoulos`

        Leader

     - .. image:: https://drive.google.com/uc?id=1TvC1Iv-ZqAmLfN7JlxWZsa0-PxDVvkLz
     - `Justin Hsiung`

        Co-Leader

   * - .. image:: https://i.ibb.co/y5GW8Hk/Selfie-2.jpg
     - `David Jarufe`

     - .. image:: https://drive.google.com/uc?id=1WrLZtXkzgHDQbCC0XLX92C8a8rgS6yMd
     - `Yezhi Shen`

   * - .. image:: https://drive.google.com/uc?id=1aM0I2cO8jJvLK6Np6HlOu8xXT3gBvhav
     - `Mimi Chon`

     - .. image:: https://drive.google.com/uc?id=1o14nh0DzvRxqAn2EX6b-1DSFPnhVLcAC
     - `Shiqi Wang`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_female.jpg
     - `Shreya Misra`

     - .. image:: https://drive.google.com/uc?id=19_-2sKwLTcjoBvjclB8tqlIA56k5QwUq
     - `Guofan Shao`

        Advisor

   * - .. image:: https://ag.purdue.edu/ProfileImages/woeste.jpg
     - `Keith Woeste`

        Advisor

     -
     -


Human Behavior in Video
#######################

Understand human behavior and obtain aggregate information from video.

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://drive.google.com/uc?id=1hqLbYByzVrojeUzDGqro2M2dqG3vITbs
     - `Siddhartha Senthil Kumar`

        Leader

     - .. image:: https://avatars3.githubusercontent.com/u/20303922?s=460&v=4
     - `Moiz Rasheed`

        Co-Leader

   * - .. image:: https://drive.google.com/uc?id=1V9msPZ7w8RYt3Vhkwa2clMWgrp0k8Ahr
     - `Mihir Abhyankar`

     - .. image:: https://drive.google.com/uc?id=19oIMMFOpQRUFNTuAb01PK_iLI1MQGuBq
     - `Russell Kim`

   * - .. image:: https://drive.google.com/uc?id=1JVh2-U7jyp-YWbG00DWICO2JP3nZwSC6
     - `Darrell Dai`

     - .. image:: https://drive.google.com/uc?id=1iJNUqW4Te-BAj5L35fmhPtDXEYeFus2k
     - `Apoorva Gupta`

   * - .. image:: https://drive.google.com/uc?id=1Y6FpralE7J6ctiz7MaRPbHQyxceV_ltC
     - `Colin Witt`

     - .. image:: https://ag.purdue.edu/ProfileImages/dbarbara.jpg
     - `David Barbarsh`

        Advisor
       
   
Solar Sail
##########

Use computer vision and image processing techniques to analyze the pictures taken by the camera on the proposed NASA Solar Cruiser Mission spacecraft.

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://drive.google.com/uc?id=1-40Gr0dYHokW-8YCb4WtvBLXXAp81ac0
     - `Naveen Vivek`

        Leader

     - .. image:: https://drive.google.com/uc?id=1t7UolOcoEZB2qhnlKls1CWSKQIwwNBPK
     - `Kayla Seeley`

   * - .. image:: https://drive.google.com/uc?id=1BszO_X7-KDGgBjBYPTa-X-B-3zcpKBw6
     - `Mark Kosmerl`

     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_female.jpg
     - `Vandana Prabhu`

   * - .. image:: https://engineering.purdue.edu/ResourceDB/ResourceFiles/image187718
     - `Anthony G Cofer`

        Advisor

     - .. image:: https://engineering.purdue.edu/ResourceDB/ResourceFiles/image214298
     - `Alina Alexeenko`

        Advisor
     
   
Autograding
###########

Create more generalized autograding scripts for grading software.

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_male.jpg
     - `Swapnil Milind Kelkar`

     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_placeholder_male.jpg
     - `Brandon Xu`

   * - .. image:: https://engineering.purdue.edu/~milind/images/me.jpeg
     - `Milind Kulkarni`

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
   * - Kyle McNulty
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
   * - Yukyung Lee
     - Seyram Samuel Mortoti
     - Asa Cutler
   * - Jack LeCroy
     - Victor Oduduabasi
     - Taher Dohadwala
   * - Jackson Moffet
     - Tong Wang
     - Katherine Sandys
   * - Ashley Kim
     - Meenakshi Pavithran
     - Justin Qualley
   * - Ryan Firestone
     - Yi-Fang Hsiung
     - Ryan Chen
   * - Amogh Shanbag
     - Siddharth Srinivasan
     - Karthik Maiya
   * - Li Yon Tan
     - Sara Aghajanzadeh
     - Ethan Glaser
   * - Xin Wang
     - Damini Rijhwani
     - Rohit Reddy Tokala
   * - Rushabh Ramesh Ranka
     - Ya Ling Tsai
     - Mert Zamir
   * - Shristi Saraff
     - Wenxi Zhang
     - Hojoung Jang
   * - Xin Du
     - Avanish Subbiah
     - Vaastav Arora
   * - Tuhin Sarkar
     - Noureldin Hendy
     - Siddhartha Kumar Senthil Kumar
   * - Noah Curran
     - Connor Chadwick
     - Stephen Davis
   * - Ved Dave
     -
     -

Video by Current and Former Members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


  .. raw:: html

    <iframe width="600" height = "400" src="https://www.youtube.com/embed/7Ao2zCYV9I8" frameborder="0" allowfullscreen></iframe>


  .. raw:: html

    <iframe width="600" height = "400" src="https://www.youtube.com/embed/1LGjSqQ953A" frameborder="0" allowfullscreen></iframe>

  .. raw:: html

    <iframe width="600" height = "400" src="https://www.youtube.com/embed/oPeKHUHpU2c" frameborder="0" allowfullscreen></iframe>

	   
    

