People and Topics
-----------------
|cam2logo|

.. |cam2logo| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/cam2logo4v2.jpg
   :width: 100%

These projects form the CAM2 (Continuous Analysis of Many CAMeras) family.	   


2020 Fall Schedule
~~~~~~~~~~~~~~~~~~~~

All meetings are held online

=========== ============== ============== ============== ============
Time        Monday         Tuesday        Wednesday      Thursday
=========== ============== ============== ============== ============
12:00-13:00                                              Solar Sail
13:00-13:30
13:30-14:30 Drone Video
14:30-15:00
15:00-16:00                Fair Vision
16:00-16:30
16:30-17:30 TensorFlow
17:30-18:30 COVID-19
=========== ============== ============== ============== ============

Due to the large number of team mebers, it is not possible changing
the regular meeting time. If your schedule does not fit into a
particular team, you have to move to another team.


Topics
~~~~~~

Analysis of Drone Video
^^^^^^^^^^^^^^^^^^^^^^^

The lack of diverse and advanced training and test drone video data
is a critical problem for the development of computer vision technology.
To solve this issue, our team aims to introduce a high-quality
annotated drone video database for low power computer vision tasks
like multiple-object detection, tracking and semantic segmentation.

In Fall 2020, the team will create a set of video clips for the following purposes:

- Detect and track multiple moving objects: The clips include moving
  objects.  The drone itself is also moving. The purpose is to
  correctly identify these objects and track their movements.

- Segmentation: Create pixel-wise labels of different objects.

- Re-identify people (optional): Determine whether the same person has been
  before.

This project is supported by `NSF CNS-1925713 <https://www.nsf.gov/awardsearch/showAward?AWD_ID=1925713>`__

Readings for new members:

- `Vision Meets Drones: A Challenge <https://arxiv.org/pdf/1804.07437.pdf>`__

- `Context Encoding for Semantic Segmentation <http://openaccess.thecvf.com/content_cvpr_2018/papers/Zhang_Context_Encoding_for_CVPR_2018_paper.pdf>`__

- `Vehicle Re-identification in Aerial Imagery: Dataset and Approach <https://arxiv.org/pdf/1904.01400.pdf>`__

- `Airborne visual tracking and reidentification system <https://www.spiedigitallibrary.org/journalArticle/Download?fullDOI=10.1117/1.JEI.28.2.023003&casa_token=Rs6JtKyTL6cAAAAA:_5C4cfQ5XkKqoeFqiyXl7r-xNdDH27PTYeq52ag1Va8udjeU3ykDF2-6B082Fdqt9JQHioCPXjE>`__


----


COVID-19
^^^^^^^^^^^^^

COVID-19 examines social distancing over time in countries around the world.
Currently, there is no existing method to utilize real-world visual data to
observe social distancing at a worldwide scale. Using people and traffic
detecting artificial intelligence (computer vision techniques), our team
analyzes large amounts of data from public cameras around the world to make
useful descriptive statements about how people are social distancing in response
to the COVID-19 pandemic. We also count number of vehicles on the road over 
time to examine traffic patterns as an indirect measure of social distancing.

Our next steps include analyzing cameras at Purdue to see how well students
are maintaining social distancing, as well as if students arewearing their
masks or not. You can find more information at https://covid19.purduehelps.org/

Reading for new members:

- `Context-Aware Crowd Counting <https://arxiv.org/abs/1811.10452>`__

- `The Visual Social Distancing Problem <https://arxiv.org/abs/2005.04813>`__

|covid01| |covid02|

     |covid03|


.. |covid01| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/covid19peopledetect.png
  :width: 45%

.. |covid02| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/covid19vehicledetect.png
  :width: 45%

.. |covid03| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/covid19detectionsovertime.png
  :width: 80%

----


Fair Vision
^^^^^^^^^^^^^

We use crowdsourcing to utilizes the knowledge of humans to complete a task.
In the scope of research, we are using the crowd to handle specific
asks that may be hard for a machine to do or improve the work of a machine.
This may include tasks such as detecting bias within image datasets
using human knowledge rather than machines, since humans are better
at distinguishing features within images. This semester, we are utilizing
crowdsourcing to help select the most suitable machine model to use for
unsupervised domain adaptation. We use the crowd to classify images to
datasets and generate a confusion matrix detailing the similarity of
images across several datasets.

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

Solar Sail
^^^^^^^^^^^^^

The Solar Sail Team is soon to be in collaboration with the NASA Marshall Center
to work on the proposed Solar Cruiser Mission (Oct 2024). The team was started
in May 2020 and official collaboration is expected to begin January 2021.
The team is currently working on the imaging of a quadrant of the spacecraft.

The main objective of the team is to design the imaging subsystem of the spacecraft,
from both a hardware and software perspective. This comprises of the camera,
lens, mounts, heat transfer system and software interfacing. Understanding of
optics, space environments, and image processing will prove to be a useful
tool when working on this team.

The current progress of the team has been camera selection and a functioning
blur-classification algorithm. Future accomplishments will include lens selection,
prototyping, testing and component integration.

Reading for new members:

- `Deep Residual Learning for Image Recognition <https://arxiv.org/abs/1512.03385>`__
- `SpineNet: Learning Scale-Permuted Backbone for Recognition and Localization <https://arxiv.org/abs/1912.05027>`__


----

TensorFlow
^^^^^^^^^^^^^

We are a team that is working to recreate important research works using
TensorFlow. Our goal is to make sure their results and code are reproducible,
replicable, and accessible for usage in industry. Our current focus is
state of the art computer vision technology, and new members will feel
right at homeif they take the time to understand cutting edge computer
vision research. Therefore, we suggest new and prospective members to
use MIT's Intro to `Deep Learning course <http://introtodeeplearning.com>`__ as a refresher.

Reading for new members:

- `Deep Residual Learning for Image Recognition <https://arxiv.org/abs/1512.03385>`__
- `SpineNet: Learning Scale-Permuted Backbone for Recognition and Localization <https://arxiv.org/abs/1912.05027>`__

	   
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

     - .. image:: https://drive.google.com/uc?id=1_wPHRuqeORLuPRjgoyYW1t7JpMzJHMfF
     - `Tianhui Chen`

   * - .. image:: https://drive.google.com/uc?id=1i9ugADcOvo2qYEj1_EbYGjH9cuP3YAqM
     - `Moya Zhu`

     - .. image:: https://drive.google.com/uc?id=1_ecXQKrjpla0Uh449IqZTwlRWK6um7oo
     - `Weiyan Hu`

   * - .. image:: https://drive.google.com/uc?id=1wkP5v4eNjSN7mMAv-ic4uPZMCXIrlevF
     - `Vincent Chen`

     - .. image:: https://www.cs.purdue.edu/people/images/small/faculty/mingyin.jpg
     - `Ming Yin`

        Advisor
        

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
     

TensorFlow
##########

Reconstruct models for the TensorFlow 2.x Model Garden

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_vishnu_banna.jpeg
     - `Vishnu Banna`

        Leader

     - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_akhil_channakotla.jpg
     - `Akhil Chinnakotla`

   * - .. image:: https://drive.google.com/uc?id=15MjIOEr5k1XvctTmnAM3yzy3JduC0MJm
     - `Taher Dohadwala`
        
     - .. image:: https://drive.google.com/uc?id=1u5dbejyw-62y5x6UPKEtPo3DFd4AtYCc
     - `Anirudh Vegesana`

   * - .. image:: https://drive.google.com/uc?id=1-40Gr0dYHokW-8YCb4WtvBLXXAp81ac0
     - `Naveen Vivek`
        
     - .. image:: https://drive.google.com/uc?id=1IwwbzzztxC6Drdmk8eHEzCAerk742G6i
     - `Tristan Yan`

   * - .. image:: https://avatars1.githubusercontent.com/u/651504?s=460&v=4
     - `George K. Thiruvathukal`

        Advisor

     -
     -


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
     - Ved Dave
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

Video by Current and Former Members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


  .. raw:: html

    <iframe width="600" height = "400" src="https://www.youtube.com/embed/7Ao2zCYV9I8" frameborder="0" allowfullscreen></iframe>


  .. raw:: html

    <iframe width="600" height = "400" src="https://www.youtube.com/embed/1LGjSqQ953A" frameborder="0" allowfullscreen></iframe>

  .. raw:: html

    <iframe width="600" height = "400" src="https://www.youtube.com/embed/oPeKHUHpU2c" frameborder="0" allowfullscreen></iframe>

	   
    

