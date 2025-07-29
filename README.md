***animal-etl pipeline***
 Extract, Transform, Load script for animal API data processing.


***Requirements***  
- Python 3.8+
- Docker
- Virtual Environment (recommended)


1. Start the API Server via Docker

***Download the Docker image***  
   [Download from Google Drive](https://drive.google.com/file/d/1MNt0fBJAjOu7pODx0HsStDLBemhAgBuR/view)

***Load the Docker image***
docker load -i lp-programming-challenge-1-1625610904.tar.gz

***Run the Docker image***
docker run --rm -p 3123:3123 -ti lp-programming-challenge-1

***clone the repository***
git clone https://github.com/your-username/animal-etl.git

cd animal-etl

***Activate the Venv***
python -m venv venv
venv\Scripts\activate 

***Install the requirements***
pip install -r requirements.txt

***Run the ETL***
python -m animal_etl.main