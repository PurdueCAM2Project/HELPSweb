Lab Machines
============

.. https://engineering.purdue.edu/HELPS/Management/lab.html

General
~~~~~~~

The Lab is EE 220C. EE 230 is an office. You can also use EE 013C for meetings.

Lab Machine Policy (Read Carefully)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. warning::

   These are general Guidelines for ECN managed computers.
   Please read carefully. If you do not follow these guidelines then your access may be revoked!

General Policy
^^^^^^^^^^^^^^^

- Do not go to ee220c and login to the machine in person.
- Do not turn off the machine under any circumstances.
- Always be conscientious and courteous to others using the machine. Do not hog resources always communicate with others who are using the machine. You can check what processes are running and who is running them using the ``htop`` command.
- If something is not clear ask! If you do not ask questions, your privileges for the machines may be revoked. Let Ryan know if there are any problems.

Anaconda Environment Guidelines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Do not download additional installations of Anaconda. This takes up a lot of space. Use the Anaconda installation resides in ``/local/a/cam2/anaconda3/``.
- Use the Anaconda installations of packages when available. Do not download or attempt to compile packages outside your home directory without permission.
- If you are not using an Anaconda virtual environment on ``/local/a/cam2/anaconda3/`` anymore, ask Ryan to remove it!

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

Available Lab Machines
~~~~~~~~~~~~~~~~~~~~~~~~

ee220clnx1.ecn.purdue.edu Specs
- 64 gb RAM
- nVidia Titan
- Intel Xeon W-2145 (3.7GHz, 4.5 GHz Turbo, 8C, 11MB Cache, HT, (140W))

Accessing and Using the Machines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connecting to the Machine
^^^^^^^^^^^^^^^^^^^^^^^^^^

- You must have an ECN account and be registered for the computer. If you do not have an ECN account you may request one here.
- SSH into the machine

  .. code-block::

     ssh <your ecn username>@ee220clnx1.ecn.purdue.edu

- Note you must be within the Purdue network. i.e. the IP address assigned to you must be a Purdue IP. You can use the Purdue VPN (Windows Only) or ssh into your shay account:

  .. code-block::

     ssh <your ecn username>@shay.ecn.purdue.edu

  - For Windows you can use Putty as an SSH client. Or you can install Windows Subsystem for Linux.

  - Linux and OS X have ssh client built in.

Accessing Anaconda
^^^^^^^^^^^^^^^^^^^^

Anaconda is a "open-source distribution of the Python and R programming languages for scientific computing". More information can be found here. You must set up your virtual environment variables to access the Anaconda Environment. The Anaconda installation resides in ``/local/a/cam2/anaconda3/``. Follow the instructions below to setup your environment for Anaconda.

- In your favorite editor (emacs, vim, nano, etc.) open ``~/.bash_profile`` and paste the following line::

  . /local/a/cam2/anaconda3/etc/profile.d/conda.sh

- Then logout and log back into the machine you should see (base) prepended to your shell as shown below::

  (base) <username>@ee220clnx1:~$

Creating Anaconda Environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two methods to create an Anaconda Environment. To see all available environments both on your local drive and on the shared drive you can run ``conda env list``.

- The first method will create an environment in your home directory on the shay.ecn.purdue.edu server. You should be careful when using this method, your home directory has a 5GB limit. This method should not be used for installing large packages or packages that will be used by several members of your team.

  - Send all members the location of where your envs are stored

  - For all users using your environments

    - ``conda create -n <env name>`` This creates conda env in your local
    - ``conda info --envs`` Lists the envs available
    - ``conda activate <env name>`` Activates the env
    - ``conda config --add <envs path>`` Creates condarc file and configures it to the shared envs
    - ``chmod -R 755 ~/.conda/envs/<env name>`` Gives permissions to your env

- The second method will create an environment that is available to everyone in the group. This can be done by filling out this form.

Note: Both methods will allow you to create conda environments usable by your team members. However, you have limited space in your home directory. If you download several packages, especially frameworks such as Tensorflow and Pytorch, it is best to save space in you local and use the first method. Method 2 will also gives all team members access to all of the owner's files. The owner needs to provide permissions to access the conda environment.

Setting up Linux on your Personal Machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As you work on the project it may be helpful to have your own personal installation of Linux for testing and running code. If you are not running a Unix based operating system such as BSD, Linux, or OS X is will make your life much easier to learn how to use these systems. My personal recommendation is to switch to using these operating systems full time. If you cannot do that there are several options available to run virtual machines.

We recommend that all students use a Debian-based Linux operating systems: Ubuntu, Ubuntu-Mate, Arch are all used in the reearch lab.

Even if you do not plan to use Linux as your day-to-day OS, you should set up a **virtual machine**. 
We recommend `Oracle Virtualbox (Recommended) <https://www.virtualbox.org/>`__, which can be installed from repository. The professional version is
also freely available and downloadable from the VirtualBox site.

Tutorials are available `for Windows <https://itsfoss.com/install-linux-in-virtualbox/>`__ and `for Mac <https://www.dev2qa.com/how-to-install-ubuntu-on-virtualbox-mac/>`__. And yes, you can virtualize Linux on a Linux host, too.

If you are a Mac user, you already have most of what you need to do work in the lab as OS X is based on Darwin, which is based on BSD Unix. However, if you want to run Linux side-by-side with OS X, you can instlall `Boot Camp (Mac) <https://support.apple.com/boot-camp>`__.  There is also a `BootCamp tutorial <https://www.macworld.co.uk/how-to/mac/how-install-linux-on-mac-3637265/>`__.

If you want to use OS X directly--which many Mac users prefer to do-- you should install `HomeBrew <https://brew.sh>`__. Homebrew provides a complete package management system for OS X, which gives you access to all of the latest/greatest tools (GNU, Python, Node, etc.). Prof. Thiruvathukal uses this on his Mac systems. Both Prof. Lu and Thiruvathukal use Linux and the command-line for their work. So please don't hesitate to contact us with questions. We prefer our students to spend less time on system adminsistration and more time on research.

