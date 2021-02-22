People and Topics
-----------------
|cam2logo|

.. |cam2logo| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/cam2logo4v2.jpg
   :width: 100%

These projects form the CAM2 (Continuous Analysis of Many CAMeras) family.	   


2021 Spring Schedule
~~~~~~~~~~~~~~~~~~~~

All meetings are held online (1 Hour, Eastern Time)

======= ============== ============== ============== ============ =================
Time    Monday         Tuesday        Wednesday      Thursday     Friday
======= ============== ============== ============== ============ =================
13:00
13:30    Drone Video
14:00
14:30    COVID-19
15:00                   Auto Drone
15:30                                                              Program Analysis
16:00    TensorFlow     Solar Sail
16:30 
======= ============== ============== ============== ============ =================

Due to the large number of team members, it is not possible changing
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

|dronevideo01| |dronevideo02|

.. |dronevideo01| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/dronevideosample.png
  :width: 45%

.. |dronevideo02| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/dronevideosegmentation.png
  :width: 45%

----


Autonomous Drones
^^^^^^^^^^^^^^^^^
Although there are more and more simulators coming out there, which can help researchers
test functionalities of their drones in a virtual environment, experiments in the real 
environment are still needed since some of the conditions that drones may encounter with 
cannot be simulated, at least for now. Our team is working to create a competition where 
drones are designed to perform autonomous flying, tracking targets, identifying information, 
and reidentification after losing target.

Specifically, the competition will be on a field where there are miniature cities built with
cardboard boxes and Legos. There are multiple programmable mobile robots moving in a pre-designed 
pattern in the mini-city. There will be QR codes displayed by screens on stationary “buildings” 
and on one of the mobile robots. QR codes will change for every certain amount of time. Only the 
robot with QR code shown is the target that the drone is supposed to track, and the other robots 
are distractors. The drone need to fly autonomously, tracking the robot with QR codes, and identify 
as many QR codes as possible in given time. After the target robot goes through a “tunnel”, gets
obstructed by “buildings”, or get together with other distractor robots, the drone needs to perform 
reidentification to continue tracking.

For this semester, our team is doing preparation work for the competition including improving 
details of the rules, designing referee system, doing prototype experiments with hardware (eg. robots, screens) 
involved in the competition.

Related readings:

- `Any Object Tracking and Following by a Flying Drone <https://ieeexplore-ieee-org.ezproxy.lib.purdue.edu/stamp/stamp.jsp?tp=&arnumber=7429411>`__

- `Autonomous Tracking of Hexacopter on Moving Mobile Robot Using Gazebo ROS Simulation <https://dl-acm-org.ezproxy.lib.purdue.edu/doi/pdf/10.1145/3055635.3056657>`__

- `PX4 Architectural Overview | PX4 User Guide <https://docs.px4.io/master/en/concept/architecture.html>`__

- `docs.px4.io <https://docs.px4.io>`__

PX4 is the Professional Autopilot. Developed by world-class developers from industry and academia, 
and supported by an active world wide community,it powers all kinds of vehicles from racing and
cargo drones through to ground vehicles and submersibles.

|AutoDrone1|

.. |AutoDrone1| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/AutonomousDrones1.png
  :width: 45%
  
----

COVID-19 (Not recruiting)
^^^^^^^^^^^^^^^^^^^^^^^^^^

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

- `Status of Solar Sail Technology Within NASA <https://reader.elsevier.com/reader/sd/pii/S0273117710007982?token=384C3A9171020945A1733E3F7E1E42455105A1F18146EAAA367F2534B504F6213FE01754897F2428E0DB9EAF0B5B9C81>`__

- `Image Blur Classification and Parameter Identification using Two-stage Deep Belief Networks <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.671.962&rep=rep1&type=pdf>`__

- `Solar Sail Halo Orbit Control using Reflectivity Control Devices <https://www.jstage.jst.go.jp/article/tjsass/57/5/57_279/_pdf/-char/ja>`__

|solarsail01| |solarsail02|

.. |solarsail01| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/solarsailmain.png
  :width: 45%

.. |solarsail02| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/solarsailkeyfeature.png
  :width: 45%

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

|tensorflow01|

.. |tensorflow01| image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/tensorflowyolov3.png
  :width: 70%

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
     - .. image:: https://engineering.purdue.edu/ResourceDB/ResourceFiles/image109726
     - `Yung-Hsiang Lu
       <https://engineering.purdue.edu/ECE/People/ptProfile?resource_id=3355>`__
       
       Electrical and Computer Engineering, Purdue

   * - .. image:: https://www.stat.purdue.edu/images/Faculty/thumbnail/varao-t.jpg
     - `Vinayak Rao
       <https://www.stat.purdue.edu/people/faculty/varao>`__
       
       Statistics, Purdue
     - .. image:: https://ag.purdue.edu/ProfileImages/shao.png
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

     - .. image:: https://engineering.purdue.edu/ResourceDB/ResourceFiles/image242327/alter?width=180&height=270
     - `James Davis
       <https://davisjam.github.io>`__

       Electrical and Computer Engineering, Purdue


Members
~~~~~~~

Graduate Students
^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 10 30

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-UCD5G5V9U-02f69f6dff32-512
     - Abhinav Goel: Doctoral Student, Improve Neural Networks' Energy Efficiency

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U4TRCF5J9-d2a18a0710be-512
     - Caleb Tung: Doctoral Student, Using Contextual Information from Network Cameras to Improve and Evaluate Computer Vision Solutions

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-UAA4XRCDD-6551ccfac7cb-512
     - Xiao Hu: Master Student

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-UCDFV8J1W-3a9e8b006ec4-512
     - Haobo Wang: Master Student


Undergraduate Students and Spring 2020 Teams
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   
Drone Video
###########

Create datasets of drone video, recognize objects, estimate the sizes.

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-UM4QYMK1R-ab6c02aa8446-512
     - `Justin Qualley`

       Leader

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U019C530LEP-84e277558738-512
     - `Ayden Kocher`

       Co-Leader

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01A1PRB3AL-7a046e1fbcef-512
     - `Indraadityan Logamurugan`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01JJ4UJS6Q-180225892e5d-512
     - `Matthew Wen`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01HE082H34-1ab906ff5d81-512
     - `Anand Chari`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01HSJSEFA5-b8232fab637f-512
     - `Yasin Kubilay Sahin`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01JC623C83-e8218d4332bf-512
     - `Gary Zancanelli`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01H784TRC6-e30798075603-512
     - `Ziteng Jiao`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-UAA4XRCDD-6551ccfac7cb-512
     - `Xiao Hu`

        Master

     - .. image:: https://libapps.s3.amazonaws.com/accounts/103752/profiles/94752/Zakharov__Wei_2016.jpg
     - `Wei Zakharov`

        Advisor

   * - .. image:: https://web.ics.purdue.edu/~qqiu/images/Qiang-Qiu.jpg
     - `Qiang Qiu`

        Advisor

     -
     -

Program Analysis
################

Placeholder Description

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01J807GM1V-11caa664a5b6-512
     - `Shan Huang`

        Leader

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01JG04C7DL-1a21863d0333-512
     - `Jonathan Doorn`

        Co-Leader

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01JKLE5SCD-29088d17c7c4-512
     - `Yu Liang`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01JNNYU9MY-f563fafb9fdb-512
     - `Brandon Wolter`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01JNV0QFEF-8588bc42e1c5-512
     - `Jake Kisabeth`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01KCJB9C4Q-20b09220615a-512
     - `Xinyuan Cai`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01JS37G3U3-609304665e10-512
     - `Yinhan Chen`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01GZ6WTLNT-78ef311ce5ac-512
     - `Daniel Chun`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01JUN55Q9K-fdd6ac829f14-512
     - `Zhaoyu Jin`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01JVEE1P54-891c74aa1d68-512
     - `Aravind Kumar Machiry`

        Advisor

Autonomous Drone
################

Placeholder Description

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U019QHF87PB-5818a3130c9f-512
     - `Hongjiao (Oliver) Qiang`

        Leader

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01HL51N3SQ-34361b9eeb9a-512
     - `Justin Chan`

        Co-Leader

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01JC008RQS-9aee006575e0-512
     - `Riya Mehta`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01J8SV746R-0bbc30244390-512
     - `Advait Mallela`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U019KST5ALC-f9c8b48afba1-512
     - `Razan Alkawai`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01LXA6F6BW-37ea71ee3893-512
     - `Alex Ishac`

COVID-19
########

Analyze how crowd densities change in public places over time and due to government policies.

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_mohammed_metwaly.png
     - `Mohammed Metwaly`

        Leader

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U013R9FA8N7-0e0cc785a59d-512
     - `Shane Allcroft`

        CAM2 Co-Leader

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01484WN7GT-d89f8b3f0d2b-512
     - `XinXin (Ellen) Zhao`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-USCB3AJTS-1a3919e466a2-512
     - `Jiahao(Jacob) Xu`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_zach_berg.jpg
     - `Zachery Peter Berg`


     - .. image:: https://ca.slack-edge.com/T02T4RJGC-UCD5G5V9U-02f69f6dff32-512
     - `Xinglei Liu`


   * - .. image:: https://avatars1.githubusercontent.com/u/651504?s=460&v=4
     - `George K. Thiruvathukal`

        Advisor

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01956Z1Q3G-17f338cca6d2-512
     - `Wei Zakharov`

        Advisor

Solar Sail
##########

Use computer vision and image processing techniques to analyze the pictures taken by the camera on the proposed NASA Solar Cruiser Mission spacecraft.

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01M68G4L93-638bba07b1c9-512
     - `Diego Avila Garcia`

        Leader

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01M2HL6Y22-3ea1c8995c60-512
     - `Jack Myers`

        Co-Leader

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01LUHNR91V-d8481a8330a2-512
     - `William Joseph Oberley`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01A1PR4DHN-b6f2e2f6e3e5-512
     - `Maria Soare`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01M68G3813-6b87d692690a-512
     - `Hamzah Kamel Ayman`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01MN036BA5-95146071e1e2-512
     - `Pume Tuchinda`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01KP571NTB-4d0871831d94-512
     - `Greivin Mauricio Martinez`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01L0BEHNN4-7e5579ae3054-512
     - `Grace Marie Yeh`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U0146F0GEQ3-945adcebb0ba-512
     - `Naveen Vivek`

        CAM2 Leader

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01KLJYMULQ-gb53d13fc6d1-512
     - `Katherine L Fowee`

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

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01956YPQ6S-b93c0a5803d7-512
     - `Kruthi Krishnappa`

        Co-Leader

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U0146F0GEQ3-945adcebb0ba-512
     - `Naveen Vivek`

        CAM2 Leader

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-UD8PE6F2Q-695570338839-512
     - `Anirudh Vegesana`

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_akhil_channakotla.jpg
     - `Akhil Chinnakotla`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U015ZLR3ZEU-7875ae9ce6d5-512
     - `Zhengxin (Tristan) Yan`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U0146900S66-58d54e1e8cd1-512
     - `Kayla Seeley`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-UFCA3E0LE-b0ad9b003454-512
     - `Hojoung (Brian) Jang`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-USEH5LK2S-87c49595361d-512
     - `Jack Lecroy`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-USWRHNBN0-fe512d0636ea-512
     - `Ved Dave`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01A1PRA2F2-ea577c6acc44-512
     - `Allen Liu`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U019J4HFCP6-4a8ce3b6b874-512
     - `David Li`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01A1PR1P9N-917c9a9a443e-512
     - `Thrishna Bhandari`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01GZ6WT3CP-6aab525cd2bc-512
     - `KyungMin Ko`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01J3R05M32-781e460f9513-512
     - `Jacob Zietek`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01HE6A2DA7-c422322087f2-512
     - `Abhirakshak Raja`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01HE086TNW-58117ee95bb7-512
     - `Siyu Wu`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01GZ6WNUJK-a54d62ef320f-512
     - `Feny Patel`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U01HAT2GNFP-b1a235f23cd2-512
     - `Ethan Suleman`

     - .. image:: https://engineering.purdue.edu/ResourceDB/ResourceFiles/image242327/alter?width=180&height=270
     - `James Davis`

        Advisor

   * - .. image:: https://avatars1.githubusercontent.com/u/651504?s=460&v=4
     - `George K. Thiruvathukal`

        Advisor

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U016USXHYKA-g11319b75bac-512
     - `Jaeyoun Kim`

        Advisor

Fair Vision (Suspended)
###########################

Use crowdsourcing to identify unintended bias in visual data and label data.

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_phillip_archuleta.jpeg
     - `Phillip Andrew Archuleta`

        Leader

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U011WSAPLD8-931afd7bfc91-512
     - `Moya Zhu`

        Co-Leader

   * - .. image:: https://raw.githubusercontent.com/PurdueCAM2Project/HELPSweb/master/source/images/member_gore_kao.jpg
     - `Gore Kao`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-UFA7C9PND-474757f75640-512
     - `Kaiwen Yu`


   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-UD8PE6F2Q-695570338839-512
     - `Anirudh Vegesana`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U011X32ML4B-87f1ade71550-512
     - `Tianhui Chen`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U012AJR0Q94-6591de67c426-512
     - `Weiyan Hu`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-UCDFV8J1W-3a9e8b006ec4-512
     - `Haobo Wang`

        Master

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-UAA4XRCDD-6551ccfac7cb-512
     - `Xiao Hu`

        Master

     - .. image:: https://avatars1.githubusercontent.com/u/651504?s=460&v=4
     - `George K. Thiruvathukal`

        Advisor


Solar Sail (Camera Project)
###########################

.. list-table::
   :widths: 10 20 10 20

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U015SC4P6J0-6470d09a4f65-512
     - `Connor David Proudman`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U015L8QM2CT-fb7768acdfd5-512
     - `Shashwat Punjani`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U014W4727JL-4b797562f800-512
     - `Mark Kosmerl`

     - .. image:: https://ca.slack-edge.com/T02T4RJGC-U015UA3ASF5-c8435de59c71-512
     - `Jinit Gandhi`

   * - .. image:: https://ca.slack-edge.com/T02T4RJGC-U015C1KGJF9-f86c7860476b-512
     - `Riley Harwood`

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
     - Stephen Davis
   * - Ashley Kim
     - Meenakshi Pavithran
     - Connor Chadwick
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
     - Jack Lecroy
   * - Xin Du
     - Avanish Subbiah
     - Vaastav Arora
   * - Tuhin Sarkar
     - Noureldin Hendy
     - Siddhartha Kumar Senthil Kumar
   * - Noah Curran
     - Nathan Gizaw
     - Subhankar Chakraborty
   * - Aditya Chakraborty
     - Christopher D. Trippel
     - Nick	Eliopoulos
   * - Justin Hsiung
     - David Jarufe
     - Yezhi Shen
   * - Shiqi Wang
     - Shreya Misra
     - Moiz Rasheed
   * - Mihir Abhyankar
     - Russell Kim
     - Darrell Dai
   * - Apoorva Gupta
     - Colin Witt
     - Swapnil Milind Kelkar
   * - Brandon Xu
     - Jakob Harbers
     - Kyler Harrison
   * - Mohammed Afolabi Fashola
     - Chibuzo Ufomba
     - Alan Jeffrey Gelman
   * - Trang (Rosie) Tran
     - Qingyang Wang
     - Jason Bagnara
   * - Tianhui Chen
     - Akshay Pawar
     - Minghao Xue
   * - Minjun (Jess) Zhang
     - Fischer Bordwell
     - Seoyoung Lee
   * - Katherine Sandys
     - Jacob Harmon
     - Dante Danaei
   * - Isha Ghodgaonkar
     - David Barbarsh
     - Alexander Leven
   * - Rthvik Raviprakash
     - Kohsuke Kimura
     - Esteban Gorostiaga
   * - Phillip Andrew Archuleta
     - Moya Zhu
     - Gore Kao
   * - Kaiwen Yu
     - Shreya Ghosh
     -


Video by Current and Former Members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


  .. raw:: html

    <iframe width="600" height = "400" src="https://www.youtube.com/embed/7Ao2zCYV9I8" frameborder="0" allowfullscreen></iframe>


  .. raw:: html

    <iframe width="600" height = "400" src="https://www.youtube.com/embed/1LGjSqQ953A" frameborder="0" allowfullscreen></iframe>

  .. raw:: html

    <iframe width="600" height = "400" src="https://www.youtube.com/embed/oPeKHUHpU2c" frameborder="0" allowfullscreen></iframe>

	   
    

