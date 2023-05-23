echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.7"
conda create --prefix ./env python=3.7 -y
echo [$(date)]: "activate env"
conda activate env/
echo [$(date)]: "intalling dev requirements"
pip install -r requirements.txt
echo [$(date)]: "END"