% ***************************************************************
% *** Help file for running all codes
% *** Source Code is mainly written for research purposes. The codes are
% *** having copyrights and required proper citations whenever it is used.
% *** Originated by:
% ***       Dr. Chandra Prakash Dubey (email:p.dubey48@gmail.com)
% ***       Ms. Gayatri Ashok Mokashi (email:@gmail.com)
% ***       
% ****************************************************************
This is a help file for a description of all Data and Source Code used for the implementation of our present paper 
"Voxel-Based Magnetic Inversion Using Elastic Net Optimization: A Computational Framework with Applications to Mineral Exploration"
      
1. PREREQUISITES

Install the following Python packages:

    numpy
    matplotlib
    plotly
    scipy
    scikit-learn

Install using:

    pip install numpy matplotlib plotly scipy scikit-learn



2. REQUIRED FILES

Make sure the following structure exists:

    project_folder/
        main_script.py
        codes/
            prism.py
            auxiliars.py


The files prism.py and auxiliars.py are required.
They contain the forward modelling and helper functions.



3. SETUP

Ensure Python can access the "codes" folder.

Either:

(A) Keep folder structure as above and run script from project_folder

OR

(B) Add to Python path inside script:

    import sys
    sys.path.append("path_to_codes_folder")

