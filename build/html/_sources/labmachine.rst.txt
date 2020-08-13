Lab Machines
============

.. https://engineering.purdue.edu/HELPS/Management/lab.html

*Last updated June 10, 2020 by Caleb Tung*

General
~~~~~~~
The HELPS Undergraduate Laboratory is open to all team members in EE 220C. The graduate student office is down the hall in EE 230.
Undergraduates can also use the VIP Research Lounge in the basement, EE 013, for meetings.

Machine List
~~~~~~~~~~~~
*This section is not yet complete.*

``ee220clnx1.ecn.purdue.edu`` -- *Suited for training deep learning models.*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* NVIDIA Titan Xp GPU - 12 GB graphics memory
* Intel Xeon W-2145 CPU
* 64 GB RAM
* 10 TB storage

ECN manages the computer for us. It runs Ubuntu 18.04 and has CUDA 10 installed. Undergraduates can do their deep learning work on this machine.

``ee220cpc4.ecn.purdue.edu`` -- *Graduate student machine.*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* NVIDIA Tesla K40c GPU - 11 GB graphics memory
* NVIDIA Titan X Pascal GPU - 12 GB graphics memory
* Intel Xeon E5-2623 CPU
* 32 GB RAM
* 1 TB storage

Abhinav Goel and Caleb Tung manage this computer. It runs Ubuntu 18.04 and has CUDA 10 installed.  Undergraduates that need to use this computer should message Abhinav or Caleb first.

Lab Machine Usage (Read Carefully)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. warning::

   Please read carefully. If you do not follow these guidelines, then your access may be revoked!

General Guidelines
^^^^^^^^^^^^^^^^^^

- Don't try to use the machines in person; ``ssh`` in instead from your personal computer.
- Do not turn off the machines under any circumstances, even if it's to "restart".
- Always be conscientious and courteous to others using the machine. Don't hog resources - always communicate with others who are using the machine! You can check what processes are running and who is running them using the ``htop`` command.
- If something is not clear, ask! Let Caleb know if there are any problems.

Accessing the Computers
^^^^^^^^^^^^^^^^^^^^^^^

Get access to the computers by `submitting this form <https://forms.office.com/Pages/ResponsePage.aspx?id=Ob0wQVN8nEGx5YdY1tY_Ifk2RneX-PJLjTakhteEDc5UMEJOR0tHMEQxWDBUV0VEWTlMWkdYM0Q1OS4u>`_. You'll need to sign into that form with your Purdue email and password.  This might take a day or so to approve via ECN. If it's taking too long, contact Caleb!

Test your login by logging into ``ee220clnx1.ecn.purdue.edu`` with your Purdue username and password: ``ssh <username>@ee220clnx1.ecn.purdue.edu``.

On Windows, the easiest way to use ``ssh`` is via Windows PowerShell. Alternatively, you could set up Windows Subsystem for Linux on your computer.

.. warning::

   You can only log into the lab computers if you're on the campus network! If you're not connected on campus, you'll need to either use `the Purdue VPN <https://engineering.purdue.edu/ECN/Support/KB/Docs/WebVPNforWindows>`_ or first ``ssh``-ing into ``ecegrid.ecn.purdue.edu`` or ``shay.ecn.purdue.edu`` and then using that shell to log into the lab computer.
   
Installing Stuff on the Computers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
Anything that requires super-user privileges (i.e. ``sudo``) will need to be installed by ECN. Message Caleb if you need this done!
 
Otherwise, you can install Python goodies into your own Anaconda environment or via ``pip install --user <packagename>``.

Using Anaconda
^^^^^^^^^^^^^^

- Do not download additional installations of Anaconda. This takes up a lot of space. The base Anaconda installation resides in ``/local/a/cam2/anaconda3/``.
- Use the Anaconda installations of packages when available. Do not download or attempt to compile packages outside your home directory without permission.

Login and add the following to your `~/.bashrc` on the computer:

.. code-block::

  __conda_setup="$('/local/a/cam2/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
  if [ $? -eq 0 ]; then
    eval "$__conda_setup"
  fi

Logout and log back into the machine you should see (base) prepended to your shell as shown below::

  ``(base) <username>@ee220clnx1:~$``

You now have access to Anaconda!

Data Management Guidelines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Important: If you download a new dataset, be sure to change the permissions using ``chmod -R 775 path/to/my/data/`` this allows others to modify your directories and add additional data. If you require a dataset to be locked you may request permission.
- The drive mounted to ``/local/a/`` is small. It is only for the Anaconda installation. Do not download data on this drive!
- The drive mounted to ``/local/b/`` is 10TB and is for scratch data and datasets.
- Do not download or store datasets to any directory outside ``/local/b/cam2/data/``. There is a link to this data directory in ``/local/a/cam2/data``.
- Before you download any datasets check to see if they already exist in the data directory. Downloading many copies of the same datasets should be avoided.
- If you do not want others to be able to modify your dataset while you work on a project you may lock the directory temporarily. When you are done using the data either unlock the directory or remove it! Do not waste space on the machine by keeping data you no longer need.

Additional Information for ECN managed computers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your home directory is not on the local machine. It is on shay.ecn.purdue.edu. Installing things in your home directory will quickly use up your allotted 5GB of space. Each team should set up their own shared Anaconda virtual environment with the packages they require (see below for options). Please remove any environment located on ``/local/a/anaconda3/`` when you are done using it by contacting Ryan.
