rem Levanta container Docker
set OLD_CD=%CD%
cd ..
docker run --name avl-tree-container -p 8501:8501 avl-tree -d
cd %OLD_CD%