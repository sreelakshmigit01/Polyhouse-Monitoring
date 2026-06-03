Environment Setup



1\. Create a virtual environment named `venv` inside the project folder:



&nbsp;  python -m venv venv



2\. Activate the virtual environment:



&nbsp;  venv\\Scripts\\activate



&nbsp;  Successful activation displays:



&nbsp;  (venv) C:\\Users\\Lenovo\\MyProject>



3\. Install the required packages:



&nbsp;  pip install pandas numpy matplotlib scikit-learn jupyter



4\. Verify the installed packages:



&nbsp;  pip list



5\. Run the smoke test:



&nbsp;  python smoke\_test.py



Smoke Test



The smoke test loads a sample sensor dictionary and prints formatted sensor values.



Expected output:



Polyhouse sensor snapshot:

date: YYYY-MM-DD

temperature\_c: 22.4

humidity\_pct: 88.5

co2\_ppm: 950

yield\_kg: 12.3



Environment OK.



If "Environment OK." is displayed, the Python environment and project setup are functioning correctly.



